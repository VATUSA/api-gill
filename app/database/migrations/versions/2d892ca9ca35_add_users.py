"""Add users

Revision ID: 2d892ca9ca35
Revises:
Create Date: 2022-04-04 12:38:06.933556

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '2d892ca9ca35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("cid", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(length=255)),
        sa.Column("last_name", sa.String(length=255)),
        sa.Column("email", sa.String(length=255)),
        sa.Column("rating", sa.Integer),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime, server_default=sa.text("now()")),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
