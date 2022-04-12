from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta
from app.v3.models.user import User


class Ticket(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tickets"
    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_ticket")
    description: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
