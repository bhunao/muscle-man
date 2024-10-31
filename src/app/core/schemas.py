from sqlmodel import SQLModel, Field

from app.core.config import Settings, settings
from app.core.main import templates, template_filters
from app.core.utils import (
    get_db_connection_msg,
    is_db_connected,
)


class DatabaseCheck(SQLModel):
    is_connected: bool = Field(default_factory=is_db_connected)
    connection: str = Field(default_factory=get_db_connection_msg)


CONTEXT_PROCESSORS = [cp.__name__ for cp in templates.context_processors]
FILTERS: list[str] = [fi.__name__ for fi in template_filters.values()]


class TemplateCheck(SQLModel):
    folder: str = Field(default=settings.TEMPLATE_FOLDER)
    context_processors: list[str] = Field(default=CONTEXT_PROCESSORS)
    filters: list[str] = Field(default=FILTERS)


class HealthCheck(SQLModel):
    if settings.DEV_MODE is True:
        settings: Settings | None = settings
    template: TemplateCheck = TemplateCheck()
    database: DatabaseCheck = DatabaseCheck()
