"""empty message

Revision ID: 58ad4df8583e
Revises: 198c3aca9d8d
Create Date: 2020-09-28 17:33:34.898353

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ad4df8583e'
down_revision = '198c3aca9d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authorized_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mailbox_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['mailbox_id'], ['mailbox.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mailbox_id', 'email', name='uq_authorize_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authorized_address')
    # ### end Alembic commands ###
