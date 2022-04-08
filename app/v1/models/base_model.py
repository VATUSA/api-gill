import os

import databases
import ormar
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()


class BaseMeta(ormar.ModelMeta):
    metadata = sqlalchemy.MetaData()
    database = databases.Database(os.getenv("DATABASE_URL"))
