"""add house_id to spaces table

Revision ID: add_house_id_to_spaces
Revises: bedd5d16ba14
Create Date: 2026-01-21 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'add_house_id_to_spaces'
down_revision: Union[str, Sequence[str], None] = 'bedd5d16ba14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('spaces', sa.Column('house_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key('fk_spaces_house_id', 'spaces', 'houses', ['house_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_spaces_house_id', 'spaces', type_='foreignkey')
    op.drop_column('spaces', 'house_id')
