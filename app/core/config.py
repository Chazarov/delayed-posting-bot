import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Configs:
    PROJECT_NAME: str = "telethone_malling_bot"

    API: str = "/api"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    BACKEND_CORS_ORIGINS: List[str] = ["*"]


    BOT_TOKEN: str = os.getenv("BOT_TOKEN")


    DB_ENGINE_MAPPER: dict = {
        "postgresql": "postgresql+",
        "mysql": "mysql+pymysql",
    }

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_ENGINE: str = "postgresql+asyncpg"
    DB_NAME: str =  os.getenv("DB_NAME")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
    



configs = Configs()