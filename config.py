from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
  DB_LOCATION: str
  DB_PORT: str
  DB_NAME: str
  DB_USERNAME: str
  DB_PASSWORD: str
  class Config:
      env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
  return Settings()