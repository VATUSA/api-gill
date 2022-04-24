from uuid import UUID

import ormar

from app.v3.models.base_model import BaseMeta


class Role(ormar.Model):
    class Meta(BaseMeta):
        tablename = "roles"
    id: UUID = ormar.UUID(primary_key=True)
    name: str = ormar.Text()
    name_long: str = ormar.Text()
