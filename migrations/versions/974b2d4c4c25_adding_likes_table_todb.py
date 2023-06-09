"""Adding Likes table todb.

Revision ID: 974b2d4c4c25
Revises: 622866bf10dd
Create Date: 2023-03-12 03:51:26.920231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '974b2d4c4c25'
down_revision = '622866bf10dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
