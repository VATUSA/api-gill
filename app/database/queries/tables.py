from datetime import datetime
from enum import Enum
from xmlrpc.client import DateTime

from pypika import Parameter as CommonParameter
from pypika import Query
from pypika import Table


class Parameter(CommonParameter):
    def __init__(self, count: int) -> None:
        super().__init__(f"${count}")


class TypedTable(Table):
    __table__ = ""

    def __init__(
        self,
        name: str | None = None,
        schema: str | None = None,
        alias: str | None = None,
        query_cls: Query | None = None,
    ) -> None:
        if name is None:
            if self.__table__:
                name = self.__table__
            else:
                name = self.__class__.__name__

        super().__init__(name, schema, alias, query_cls)


class TransferRequestStatus(Enum):
    PENDING = 0,
    APPROVED = 1,
    DENIED = 2


class Facility(TypedTable):
    __table__ = "facilities"
    id: int
    iata: str
    name: str
    url: str
    active: bool
    created_at: datetime
    updated_at: datetime


class Rating(TypedTable):
    __table__ = "ratings"
    id: int
    short: str
    long: str


class Role(TypedTable):
    __table__ = "roles"
    id: int
    short: str
    long: str


class UserRole(TypedTable):
    __table__ = "user_roles"
    id: int
    user_id: int
    role_id: int


class User(TypedTable):
    __table__ = "users"
    id: int
    first_name: str
    last_name: str
    email: str
    rating_id: int
    rating: Rating
    facility_id: int
    created_at: datetime
    updated_at: datetime


class SoloCert(TypedTable):
    __table__ = "solo_certs"
    id: int
    user_id: int
    submitter_id: int
    position: str
    end: DateTime
    timestamp: datetime


class TrainingTicket(TypedTable):
    __table__ = "training_tickets"
    id: int
    user_id: int
    submitter_id: int
    facility: str
    position: str
    start: datetime
    end: datetime
    comments: str
    created_at: datetime
    updated_at: datetime


class Comment(TypedTable):
    __table__ = "comments"
    id: int
    user_id: int
    submitter_id: int
    timestamp: datetime


class TransferRequest(TypedTable):
    __table__ = "transfer_requests"
    id: int
    user_id: int
    facility_to_id: int
    facility_from_id: int
    reason: str
    status: TransferRequestStatus
    created_at: datetime
    updated_at: datetime


facilities = Facility()
ratings = Rating()
roles = Role()
user_roles = UserRole()
users = User()
solo_certs = SoloCert()
training_tickets = TrainingTicket()
comments = Comment()
transfer_requests = TransferRequest()
