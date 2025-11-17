from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_DATABASE: str = "ppe_db"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = ""

    UPLOAD_DIR: str = "uploads"
    RESULT_DIR: str = "results"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
