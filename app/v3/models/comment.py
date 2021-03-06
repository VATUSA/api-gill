from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta
from app.v3.models.user import User


class Comment(ormar.Model):
    class Meta(BaseMeta):
        tablename = "comments"
    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_comment")
    title: str = ormar.Text()
    description: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
