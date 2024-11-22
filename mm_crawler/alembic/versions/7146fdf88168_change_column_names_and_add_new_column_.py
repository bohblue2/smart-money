"""Change column names and add new column(latest_scraped_at)

Revision ID: 7146fdf88168
Revises: d7d3ec2878fc
Create Date: 2024-05-16 16:59:43.313550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7146fdf88168'
down_revision: Union[str, None] = 'd7d3ec2878fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_contents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('article_id', sa.String(), nullable=False),
    sa.Column('media_id', sa.String(), nullable=False),
    sa.Column('html', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('language', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('articles', sa.Column('latest_scraped_at', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'latest_scraped_at')
    op.drop_table('article_contents')
    # ### end Alembic commands ###