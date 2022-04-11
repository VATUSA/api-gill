"""Add regions

Revision ID: aeba0b843ab0
Revises: 38eb795e2032
Create Date: 2022-04-11 01:27:23.530367

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'aeba0b843ab0'
down_revision = '38eb795e2032'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'regions',
        sa.Column('id', UUID(), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('name', sa.String(length=255)),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()')),
    )

    pass


def downgrade() -> None:
    op.drop_table('regions')
    pass
