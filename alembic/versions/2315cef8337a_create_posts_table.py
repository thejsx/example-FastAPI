"""create posts table

Revision ID: 2315cef8337a
Revises: 
Create Date: 2023-05-09 20:08:30.771090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2315cef8337a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable = False, primary_key=True), sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
