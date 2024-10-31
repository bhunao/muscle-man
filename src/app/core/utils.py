import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager, contextmanager
from typing import Any

from fastapi import FastAPI, Request
from sqlmodel import select

from app.core.config import settings
from app.core.database import engine, get_session

log = logging.getLogger(__name__)


def is_hx_request(request: Request):
    return request.headers.get("Hx-Request") == "true"


def database_connection() -> bool | Exception:
    try:
        with contextmanager(get_session)() as session:
            query = select(1)
            _ = session.exec(query).all()
    except Exception as e:
        return e
    return True


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[dict[Any, Any]]:
    log.debug(f"Starting lifespan event of {settings.APP_NAME}.")
    if database_connection() is False:
        log.error("Error trying to connect with the database.")
        # raise Exception("Database not connected.")
    assert app
    state: dict[str, Any] = dict()
    yield state
    log.debug(f"Finishing lifespan event of {settings.APP_NAME}.")


def is_db_connected():
    return True if database_connection() is True else False


def get_db_connection_msg():
    connected = database_connection()
    if connected is True:
        return str(engine.raw_connection())
    else:
        return str(connected)
