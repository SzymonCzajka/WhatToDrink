"""empty message

Revision ID: 877a80ed0161
Revises: 1064f692d875
Create Date: 2021-01-09 17:22:03.482974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877a80ed0161'
down_revision = '1064f692d875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drink', sa.Column('drink_name', sa.String(length=200), nullable=True))
    op.drop_column('drink', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drink', sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('drink', 'drink_name')
    # ### end Alembic commands ###