import ormar
from dotenv import load_dotenv

from app.v3.database.connection import database
from app.v3.database.connection import metadata

load_dotenv()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
