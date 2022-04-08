from datetime import datetime

import ormar

from app.v1.models.base_model import BaseMeta
from app.v1.models.user import User


class Ticket(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tickets"
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_ticket")
    description: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
