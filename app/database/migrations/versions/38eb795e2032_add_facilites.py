"""Add facilites

Revision ID: 38eb795e2032
Revises: 2d892ca9ca35
Create Date: 2022-04-11 01:00:34.503173

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '38eb795e2032'
down_revision = '2d892ca9ca35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'facilities',
        sa.Column('id', UUID(), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('name', sa.String(length=255)),
        sa.Column('url', sa.String(length=255)),
        sa.Column('region', UUID()),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()')),
    )

    pass


def downgrade() -> None:
    op.drop_table('facilities')
    pass
