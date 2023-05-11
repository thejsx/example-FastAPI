"""add foreign-key to post table

Revision ID: f3fb8b7e369b
Revises: 3a3737ce3739
Create Date: 2023-05-09 22:36:45.970439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3fb8b7e369b'
down_revision = '3a3737ce3739'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="users", local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name="posts")
    op.drop_column('posts', 'owner_id')
