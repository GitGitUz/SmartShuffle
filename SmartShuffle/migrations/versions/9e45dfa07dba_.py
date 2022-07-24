"""empty message

Revision ID: 9e45dfa07dba
Revises: 63d86aa1b6a2
Create Date: 2022-07-23 21:42:34.208791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e45dfa07dba'
down_revision = '63d86aa1b6a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_reset_token', sa.String(length=100), nullable=True))
    op.drop_column('user', 'pwdreset_hashedtoken')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pwdreset_hashedtoken', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('user', 'password_reset_token')
    # ### end Alembic commands ###
