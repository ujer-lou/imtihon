"""initial migration

Revision ID: 644f25e23a14
Revises: None
Create Date: 2024-10-27 13:22:23.258193
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '644f25e23a14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fullname', sa.String(length=50), nullable=True),
        sa.Column('phone_number', sa.String(length=15), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Add more table creation or column additions here
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # Add more table dropping or column removals here
    # ### end Alembic commands ###
