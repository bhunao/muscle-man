from typing import Any

from pydantic.fields import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings
from starlette.requests import Request


def app_context(request: Request) -> dict[str, Any]:
    """Add context to the template."""
    return {"test": "treco"}


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Microservice"

    DEV_MODE: bool = False

    # security
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = "OkfUZjfT-DEFINITLYATOTALSECUREKEYO_MJFtac50"

    # Templating
    TEMPLATE_FOLDER: str = "templates"

    DATABASE_URL: str = "sqlite:///bookkeeper.db"


settings = Settings()
