# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Define variables and their expected types
    SECRET_KEY: str
    ALGORITHM: str = "HS256"  # You can provide default values
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    # Tell Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env")

# Instantiate the settings object to use across your app
settings = Settings()