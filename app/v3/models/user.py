import enum
from datetime import datetime
from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta
from app.v3.models.facility import Facility
from app.v3.models.role import Role


class Rating(enum.Enum):
    INAC = -1
    SUS = 0
    OBS = 1
    S1 = 2
    S2 = 3
    S3 = 4
    C1 = 5
    C2 = 6
    C3 = 7
    I1 = 8
    I2 = 9
    I3 = 10
    SUP = 11
    ADM = 12


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    id: UUID = ormar.UUID(primary_key=True)
    first_name: str = ormar.Text()
    last_name: str = ormar.Text()
    preferred_first_name: str = ormar.Text()
    preferred_last_name: str = ormar.Text()
    full_name: str = f"{preferred_first_name} {preferred_last_name}"
    full_name_cid: str = f"{full_name} - {id}"
    email: str = ormar.Text()
    rating: Rating = ormar.Integer(choices=list(Rating))
    discord: str = ormar.Text()
    transfer_override: bool = ormar.Boolean(default=False)
    is_home_region: bool = ormar.Boolean(default=True)
    email_opt_in: bool = ormar.Boolean(default=False)
    facility: Facility = ormar.ForeignKey(Facility, related_name="facility_user")
    visiting_facilities: list[Facility] = ormar.ManyToMany(Facility, related_name="visiting_facilities_user")
    roles: list[Role] | None = ormar.ManyToMany(Role)
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
