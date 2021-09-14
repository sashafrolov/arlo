# pylint: disable=invalid-name
"""Background task progress

Revision ID: 971d6d153879
Revises: f400f19f7a35
Create Date: 2021-09-08 18:10:07.594503+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "971d6d153879"
down_revision = "f400f19f7a35"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "background_task", sa.Column("work_total", sa.Integer(), nullable=True)
    )
    op.add_column(
        "background_task", sa.Column("work_progress", sa.Integer(), nullable=True)
    )


def downgrade():  # pragma: no cover
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_column('background_task', 'work_progress')
    # op.drop_column('background_task', 'work_total')
    # ### end Alembic commands ###
