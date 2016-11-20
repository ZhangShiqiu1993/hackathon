"""empty message

Revision ID: 425583af851e
Revises: 7ad1612c2d07
Create Date: 2016-11-19 19:25:16.029874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425583af851e'
down_revision = '7ad1612c2d07'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
