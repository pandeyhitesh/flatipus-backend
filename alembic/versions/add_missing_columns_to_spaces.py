"""add missing columns to spaces table

Revision ID: add_missing_columns_to_spaces
Revises: add_house_id_to_spaces
Create Date: 2026-01-21 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'add_missing_columns_to_spaces'
down_revision: Union[str, Sequence[str], None] = 'add_house_id_to_spaces'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('spaces', sa.Column('name', sa.String(), nullable=False, server_default=''))
    op.add_column('spaces', sa.Column('created_at', sa.DateTime(), nullable=True, server_default=sa.func.now()))
    op.alter_column('spaces', 'name', server_default=None)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('spaces', 'created_at')
    op.drop_column('spaces', 'name')
