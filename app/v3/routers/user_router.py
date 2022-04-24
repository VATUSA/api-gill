from fastapi import APIRouter

from app.v3.database.repositories.user_repository import UserRepository
from app.v3.models.user import User

user_router = APIRouter(
    prefix="/v3/users",
    tags=["users"],
)
user_repository = UserRepository()


@user_router.get("/", response_model=list[User])
async def get_users() -> list[User | None]:
    users = await user_repository.get_users()
    return users
