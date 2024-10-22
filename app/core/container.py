from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repositories import *
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

   