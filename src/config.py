from pydantic import EmailStr, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str
    FIRST_SUPERADMIN_EMAIL: EmailStr
    FIRST_SUPERADMIN_PASSWORD: SecretStr


config = Settings()  # type: ignore
