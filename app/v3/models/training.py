import enum
from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta
from app.v3.models.user import User


class TrainingType(enum.Enum):
    CLASSROOM = "classroom"
    LIVE = "live"
    SWEATBOX = "sweatbox"
    OTS_LIVE = "ots_live"
    OTS_SWEATBOX = "ots_sweatbox"


class Training(ormar.Model):
    class Meta(BaseMeta):
        tablename = "trainings"
    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_training")
    submitter: User = ormar.ForeignKey(User, related_name="submitter_training")
    type: TrainingType = ormar.Text(choices=list(TrainingType))
    facility: str = ormar.String(max_length=3)
    position: str = ormar.String(max_length=10)
    notes: str = ormar.Text()
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
