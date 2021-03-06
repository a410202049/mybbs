"""empty message

Revision ID: e26588e7509b
Revises: c1954956c974
Create Date: 2017-04-03 18:59:43.380000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e26588e7509b'
down_revision = 'c1954956c974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('is_removed', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.String(length=100), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('origin_comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['front_user.id'], ),
    sa.ForeignKeyConstraint(['origin_comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
