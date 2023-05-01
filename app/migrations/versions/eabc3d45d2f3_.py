"""empty message

Revision ID: eabc3d45d2f3
Revises: 938759a1df31
Create Date: 2023-05-01 23:09:57.377632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eabc3d45d2f3'
down_revision = '938759a1df31'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urls', sa.Column('redirect', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('urls', 'redirect')
    # ### end Alembic commands ###
