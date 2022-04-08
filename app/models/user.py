from datetime import datetime

import ormar

from app.models.base_model import BaseMeta
from app.models.facility import Facility
from app.models.rating import Rating
from app.models.role import Role


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    id: int = ormar.Integer(primary_key=True)
    first_name: str = ormar.Text()
    last_name: str = ormar.Text()
    preferred_first_name: str = ormar.Text()
    preferred_last_name: str = ormar.Text()
    full_name: str = f"{preferred_first_name} {preferred_last_name}"
    full_name_cid: str = f"{full_name} - {id}"
    email: str = ormar.Text()
    rating: Rating = ormar.ForeignKey(Rating, related_name="rating_user")
    discord: str = ormar.Text()
    transfer_override: bool = ormar.Boolean(default=False)
    is_home_region: bool = ormar.Boolean(default=True)
    email_opt_in: bool = ormar.Boolean(default=False)
    facility: Facility = ormar.ForeignKey(Facility, related_name="facility_user")
    visiting_facilities: list[Facility] = ormar.ManyToMany(Facility, related_name="visiting_facilities_user")
    roles: list[Role] | None = ormar.ManyToMany(Role)
    created_at: datetime = ormar.DateTime()
    updated_at: datetime = ormar.DateTime()
