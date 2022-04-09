from datetime import datetime

import ormar

from app.v1.models.base_model import BaseMeta


class Facility(ormar.Model):
    class Meta(BaseMeta):
        tablename = "facilities"
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.Text()
    url: str = ormar.Text()
    api_key: str = ormar.Text()
    sandbox_api_key: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
