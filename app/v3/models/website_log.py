from datetime import datetime
from uuid import UUID

import ormar
import pydantic

from app.v3.models.base_model import BaseMeta


class WebsiteLog(ormar.Model):
    class Meta(BaseMeta):
        tablename = "website_logs"
    id: UUID = ormar.UUID(primary_key=True)
    ip: str = ormar.Text()
    user_id: int | None = ormar.Integer(nullable=True)
    user_name: str | None = ormar.Text(nullable=True)
    action: str = ormar.Text()
    old_data: pydantic.Json = ormar.JSON()
    new_data: pydantic.Json = ormar.JSON()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
