"""create user and team table

Revision ID: 9f7ea91d2267
Revises: 
Create Date: 2023-10-16 21:04:23.601932

"""
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.core.security import get_password_hash


# revision identifiers, used by Alembic.
revision: str = '9f7ea91d2267'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def insert_init_super_user(user_table,team_table):
    op.bulk_insert(
        user_table,
        [
            {
                "id": 1,
                "full_name": "admin",
                "email": os.getenv("FIRST_SUPERUSER"),
                "hashed_password": get_password_hash(os.getenv("FIRST_SUPERUSER_PASSWORD")),
                "is_active": True,
                "is_superuser": True,
                "team_id": 1,
            }
        ]
    )

    op.bulk_insert(
        team_table,
        [
            {
                "id": 1,
                "team_name": "플랫폼개발1팀",
                "manager_id": 1
            },
            {
                "id": 2,
                "team_name": "플랫폼개발2팀",
                "manager_id": 1
            },
            {
                "id": 3,
                "team_name": "플랫폼개발3팀",
                "manager_id": 1
            }
       ]
    )


def upgrade() -> None:
    user_table = op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.Column("team_id",sa.Integer(),nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_full_name"), "user", ["full_name"], unique=False)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)


    team_table = op.create_table(
        "team",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("team_name", sa.String(), nullable=False),
        sa.Column("manager_id", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    insert_init_super_user(user_table,team_table)

    op.create_index(op.f("ix_team_name"), "team", ["team_name"], unique=False)
    op.create_index(op.f("ix_team_manager_id"), "team", ["manager_id"], unique=False)
    op.create_index(op.f("ix_team_id"), "team", ["id"], unique=False)

    op.create_foreign_key("fk_user", source_table="team", referent_table="user", local_cols=["manager_id"], remote_cols=["id"], ondelete="CASCADE")
    op.create_foreign_key("fk_team", source_table="user", referent_table="team", local_cols=["team_id"], remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_full_name"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
