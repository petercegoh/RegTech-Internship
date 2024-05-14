"""create restaurant table

Revision ID: 9bf6585b3128
Revises: 
Create Date: 2024-05-14 16:12:56.780951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bf6585b3128'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "indo_food_list",
    sa.Column("id", sa.Integer,primary_key=True),
    sa.Column("name", sa.String(20),unique=True, nullable=False),
    sa.Column("cuisine", sa.String(10),unique=False, nullable=False),
    sa.Column("google_rating", sa.Float,unique=False, nullable=False),
    sa.Column("budget", sa.String(10),unique=False, nullable=False),
    sa.Column("district_area", sa.String(10),unique=False, nullable=False)
    )



def downgrade() -> None:
    op.drop_table("indo_food_list")
