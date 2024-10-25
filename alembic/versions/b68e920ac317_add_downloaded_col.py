"""empty message

Revision ID: b68e920ac317
Revises: e3eb1c02cb06
Create Date: 2024-10-24 22:38:50.293140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b68e920ac317'
down_revision: Union[str, None] = 'e3eb1c02cb06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('research_reports', sa.Column('downloaded', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('research_reports', 'downloaded')
    # ### end Alembic commands ###
