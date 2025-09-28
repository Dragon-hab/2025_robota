from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'Event Platform'
    SECRET_KEY: str = 'CHANGE_ME_IN_PRODUCTION'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7  # 7 days
    DATABASE_URL: str = 'sqlite:///./dev.db'

    class Config:
        env_file = '.env'

settings = Settings()
