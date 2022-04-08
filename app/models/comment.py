from datetime import datetime

import ormar

from app.models.base_model import BaseMeta
from app.models.user import User


class Comment(ormar.Model):
    class Meta(BaseMeta):
        tablename = "comments"
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_comment")
    title: str = ormar.Text()
    description: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
