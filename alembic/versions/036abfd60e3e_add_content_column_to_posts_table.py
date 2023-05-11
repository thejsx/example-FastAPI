"""add content column to posts table

Revision ID: 036abfd60e3e
Revises: 2315cef8337a
Create Date: 2023-05-09 22:19:15.117357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '036abfd60e3e'
down_revision = '2315cef8337a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
