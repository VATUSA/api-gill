import os

import loguru
from dotenv import load_dotenv

from app.v3.models.user import User

load_dotenv()


class UserRepository:

    def __init__(self) -> None:
        self.logger = loguru.logger
        self.debug = os.getenv("DEBUG", False)

    async def get_users(self) -> list[User | None]:
        users = await User.objects.all()
        if self.debug:
            self.logger.debug(f"{len(users)} users found.")
        return users
