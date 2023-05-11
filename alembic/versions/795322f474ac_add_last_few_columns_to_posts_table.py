"""add last few columns to posts table

Revision ID: 795322f474ac
Revises: f3fb8b7e369b
Create Date: 2023-05-09 22:59:55.832236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795322f474ac'
down_revision = 'f3fb8b7e369b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
    ))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
