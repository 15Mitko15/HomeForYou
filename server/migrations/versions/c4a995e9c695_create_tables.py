"""Create a lot of tables"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c4a995e9c695"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply the migration: Create a lot of tables."""

    # pylint: disable=no-member
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(50), nullable=False, unique=True),
        sa.Column("email", sa.String(100), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
    )

    # pylint: disable=no-member
    op.create_table(
        "cities",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False, unique=True),
    )

    # pylint: disable=no-member
    op.create_table(
        "neighborhoods",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False, unique=False),
        sa.Column("city_id", sa.Integer, sa.ForeignKey("cities.id"), nullable=False),
    )

    # pylint: disable=no-member
    op.create_table(
        "properties",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("description", sa.String(), nullable=False, unique=False),
        sa.Column("price", sa.Integer(), nullable=False, unique=False),
        sa.Column("area", sa.Integer(), nullable=False, unique=False),
        sa.Column(
            "neighborhood_id",
            sa.Integer,
            sa.ForeignKey("neighborhoods.id"),
            nullable=False,
        ),
    )

    # pylint: disable=no-member
    op.create_table(
        "favorites",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "property_id", sa.Integer, sa.ForeignKey("properties.id"), nullable=False
        ),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
    )


def downgrade() -> None:
    """Rollback the migration: Drop the neighborhoods table."""
    # pylint: disable=no-member
    op.drop_table("users")
    op.drop_table("cities")
    op.drop_table("neighborhoods")
    op.drop_table("properties")
    op.drop_table("favorites")
