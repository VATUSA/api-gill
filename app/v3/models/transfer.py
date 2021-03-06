import enum
from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta
from app.v3.models.facility import Facility
from app.v3.models.user import User


class TransferStatus(enum.Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DENIED = "Denied"


class Transfer(ormar.Model):
    class Meta(BaseMeta):
        tablename = "transfers"
    id: UUID = ormar.UUID(primary_key=True)
    user: User = ormar.ForeignKey(User, related_name="user_transfer")
    facility_from: Facility = ormar.ForeignKey(Facility, related_name="facility_from_transfer")
    facility_to: Facility = ormar.ForeignKey(Facility, related_name="facility_to_transfer")
    reasion: str = ormar.Text()
    status: TransferStatus = ormar.Text(choices=list(TransferStatus))
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
