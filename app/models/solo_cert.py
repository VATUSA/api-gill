from datetime import datetime

import ormar

from app.models.base_model import BaseMeta
from app.models.user import User


class SoloCert(ormar.Model):
    class Meta(BaseMeta):
        tablename = "solo_certs"
    id: int = ormar.Integer(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_solo_cert")
    submitter: User = ormar.ForeignKey(User, related_name="submitter_solo_cert")
    position: str = ormar.Text()
    end: datetime = ormar.DateTime()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
