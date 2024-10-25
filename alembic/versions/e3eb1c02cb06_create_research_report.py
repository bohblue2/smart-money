"""empty message

Revision ID: e3eb1c02cb06
Revises: d97e0641bd1e
Create Date: 2024-10-18 20:03:45.199517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3eb1c02cb06'
down_revision: Union[str, None] = 'd97e0641bd1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('research_reports',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('file_url', sa.String(), nullable=False),
    sa.Column('issuer_company_name', sa.String(), nullable=False),
    sa.Column('issuer_company_id', sa.String(), nullable=False),
    sa.Column('report_category', sa.String(), nullable=False),
    sa.Column('report_id', sa.String(), nullable=False),
    sa.Column('target_company', sa.String(), nullable=True),
    sa.Column('target_industry', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('kosdaq_articles_last_year')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kosdaq_articles_last_year',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('article_id', sa.VARCHAR(), nullable=False),
    sa.Column('media_id', sa.VARCHAR(), nullable=False),
    sa.Column('media_name', sa.VARCHAR(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('link', sa.VARCHAR(), nullable=False),
    sa.Column('original_id', sa.VARCHAR(), nullable=True),
    sa.Column('is_origin', sa.BOOLEAN(), nullable=False),
    sa.Column('article_published_at', sa.DATETIME(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('latest_scraped_at', sa.DATETIME(), nullable=False),
    sa.Column('ticker', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('research_reports')
    # ### end Alembic commands ###
