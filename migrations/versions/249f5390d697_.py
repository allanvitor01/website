"""empty message

Revision ID: 249f5390d697
Revises: 
Create Date: 2018-06-30 22:07:33.158349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '249f5390d697'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('website', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=120), nullable=False),
    sa.Column('bio', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bio'),
    sa.UniqueConstraint('email')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('abstract', sa.Text(), nullable=False),
    sa.Column('cover', sa.String(length=120), nullable=False),
    sa.Column('published_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=False),
    sa.Column('published', sa.String(length=6), nullable=False),
    sa.Column('slug', sa.String(length=300), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('abstract'),
    sa.UniqueConstraint('text')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paper')
    op.drop_table('category')
    op.drop_table('author')
    # ### end Alembic commands ###
