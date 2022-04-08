from datetime import datetime

import ormar

from app.models.base_model import BaseMeta
from app.models.rating import Rating
from app.models.user import User


class Promotion(ormar.Model):
    class Meta(BaseMeta):
        tablename = "promotions"
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_promotion")
    submitter: User = ormar.ForeignKey(User, related_name="submitter_promotion")
    old_rating: Rating = ormar.ForeignKey(Rating, related_name="old_rating_promotion")
    new_rating: Rating = ormar.ForeignKey(Rating, related_name="new_rating_promotion")
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
