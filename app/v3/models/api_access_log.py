from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta


class ApiAccessLog(ormar.Model):
    class Meta(BaseMeta):
        tablename = "api_access_logs"
    id: UUID = ormar.UUID(primary_key=True)
    ip: str = ormar.Text()
    facility_id: int | None = ormar.Integer(nullable=True)
    facility_name: str | None = ormar.Text(nullable=True)
    action: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
