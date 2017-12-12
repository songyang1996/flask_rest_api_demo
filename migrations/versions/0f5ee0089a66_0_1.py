"""0.1

Revision ID: 0f5ee0089a66
Revises: 
Create Date: 2017-12-09 21:00:19.011119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f5ee0089a66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.String(length=10), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_table('authors')
    # ### end Alembic commands ###
