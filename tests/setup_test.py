import os

import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.order(1)
def test_setup() -> None:
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))

    cursor = connection.cursor()

    sql = "TRUNCATE comments, facilities, policies, promotions, roles, \
        solo_certs, tickets, trainings, transfers, users, website_logs CASCADE;"

    cursor.execute(sql)

    connection.commit()

    cursor.close()
    connection.close()
