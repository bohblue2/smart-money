import os
from typing import Annotated, Any

from pydantic import PostgresDsn, AnyUrl, computed_field, BeforeValidator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class CrawlerSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    
    ALEMBIC_DB_URL: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    def __post_init__(self):
        def display_all_fields(self):
            """
            Display all configuration values.
            """
            for field_name, field_value in self.__dict__.items():
                print(f"{field_name}: {field_value}")
        display_all_fields()
    
    class Config:
        env_file = ".dev.crawler.env" if os.getenv("ENVIRONMENT") == 'DEV' else ".prod.crawler.env"
        env_file_encoding = "utf-8"

settings = CrawlerSettings() # type: ignore