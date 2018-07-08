"""empty message

Revision ID: 4b222e53257d
Revises: 249f5390d697
Create Date: 2018-07-07 22:22:39.956828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b222e53257d'
down_revision = '249f5390d697'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('paper', 'last_modified',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.alter_column('paper', 'published_date',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('paper', 'published_date',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('paper', 'last_modified',
               existing_type=sa.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
