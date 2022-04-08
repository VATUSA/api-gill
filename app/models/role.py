import ormar

from app.models.base_model import BaseMeta


class Role(ormar.Model):
    class Meta(BaseMeta):
        tablename = "roles"
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.Text()
    name_long: str = ormar.Text()
