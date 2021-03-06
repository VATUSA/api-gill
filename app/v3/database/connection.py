import os

import databases
import sqlalchemy

database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")
database_port = os.getenv("DATABASE_PORT")
database_database = os.getenv("DATABASE_DATABASE")

metadata = sqlalchemy.MetaData()
database = databases.Database(
    f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_database}",
)
