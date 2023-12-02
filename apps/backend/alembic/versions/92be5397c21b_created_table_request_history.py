"""Created table request_history

Revision ID: 92be5397c21b
Revises: 
Create Date: 2023-12-02 16:13:19.831883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92be5397c21b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency_from', sa.String(), nullable=False),
    sa.Column('currency_to', sa.String(), nullable=False),
    sa.Column('request_date', sa.DateTime(), nullable=False),
    sa.Column('is_error', sa.Boolean(), nullable=False),
    sa.Column('exchange_rate', sa.DECIMAL(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_history')
    # ### end Alembic commands ###