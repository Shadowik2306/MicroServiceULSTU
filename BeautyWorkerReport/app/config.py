from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseSettings):
    DATABASE_URL: str

    @property
    def database_url(self):
        return self.DATABASE_URL

    model_config = SettingsConfigDict()


db_settings = DBSettings()
