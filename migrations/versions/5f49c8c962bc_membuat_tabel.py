"""membuat tabel

Revision ID: 5f49c8c962bc
Revises: 5e290df55c45
Create Date: 2021-08-03 12:40:11.592623

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5f49c8c962bc'
down_revision = '5e290df55c45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('kode_kuliah', sa.String(length=30), nullable=False))
    op.drop_column('matakuliah', 'kode_kuliahh')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('kode_kuliahh', mysql.VARCHAR(length=30), nullable=False))
    op.drop_column('matakuliah', 'kode_kuliah')
    # ### end Alembic commands ###