import pathlib

from decouple import config
from pydantic import BaseSettings
from pydantic import PostgresDsn

# do not move file into another directory,
# or change the following name accordingly,
# it depends on a directory the file is in
DEFAULT_NAME = pathlib.Path(__file__).parent.parent.parent.name


class Settings(BaseSettings):
    PROJECT_NAME: str = config("PROJECT_NAME", DEFAULT_NAME)
    API_VERSION: str = config("API_VERSION", "/api/v1")
    BACKEND_CORS_ORIGINS: str = config("BACKEND_CORS_ORIGINS", "*")
    SQLALCHEMY_DATABASE_URI: str = PostgresDsn.build(
        scheme="postgresql",
        user=config("DATABASE_USERNAME", "user"),
        password=config("DATABASE_PASSWORD", "gibberish"),
        host=config("DATABASE_HOST", "127.0.0.1"),
        port=config("DATABASE_PORT", "5433"),
        path=f"/{config('DATABASE_NAME', 'user_service')}",
    )


class DataValidation(BaseSettings):
    # entities
    names_min_length = 1
    first_name_max_length = 100
    last_name_max_length = 50
    email_number_min_length = 7
    email_number_max_length = 320
    phone_number_min_length = 12
    phone_number_max_length = 22

    # functionality
    page_size = 25


settings = Settings()
data_validation = DataValidation()
