"""create user table

Revision ID: 194e68dac84e
Revises: 9bf6585b3128
Create Date: 2024-05-14 17:06:35.843179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '194e68dac84e'
down_revision: Union[str, None] = '9bf6585b3128'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "user_list",
    sa.Column("id", sa.Integer,primary_key=True),
    sa.Column("name", sa.String(20),unique=True, nullable=False),
    sa.Column("address", sa.String(10),unique=False, nullable=True),
    sa.Column("country", sa.String(2), unique=False, nullable=False),
    sa.Column("fav_restaurant", sa.String(20),unique=False, nullable=True),
    )
    op.create_foreign_key(
        "fk_user_fav_restaurant", 
        "user_list", "indo_food_list", 
        ["fav_restaurant"], ["name"]
    )


def downgrade() -> None:
    op.drop_table("user_list")
