import enum
from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta


class PolicyCategory(enum.Enum):
    GENERAL_DIVISION = "General Division"
    TRAINING_ADMINISTRATION = "Training Administration"
    INFORMATION_TECHNOLOGY = "Information Technology"
    MEDIA = "Media"


class Policy(ormar.Model):
    class Meta(BaseMeta):
        tablename = "policies"
    id: UUID = ormar.UUID(primary_key=True)
    title: str = ormar.Text()
    category: PolicyCategory = ormar.Text(choices=list(PolicyCategory))
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
