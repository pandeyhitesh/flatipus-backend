"""add chores column to spaces table

Revision ID: add_chores_to_spaces
Revises: add_missing_columns_to_spaces
Create Date: 2026-01-21 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'add_chores_to_spaces'
down_revision: Union[str, Sequence[str], None] = 'add_missing_columns_to_spaces'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('spaces', sa.Column('chores', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('spaces', 'chores')
