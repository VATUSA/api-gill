from datetime import datetime

import ormar

from app.v1.models.base_model import BaseMeta
from app.v1.models.user import Rating
from app.v1.models.user import User


class Promotion(ormar.Model):
    class Meta(BaseMeta):
        tablename = "promotions"
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_promotion")
    submitter: User = ormar.ForeignKey(User, related_name="submitter_promotion")
    old_rating: Rating = ormar.Integer(choices=list(Rating))
    new_rating: Rating = ormar.Integer(choices=list(Rating))
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
