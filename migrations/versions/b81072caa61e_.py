"""empty message

Revision ID: b81072caa61e
Revises: f05e04284523
Create Date: 2017-03-19 12:53:28.934582

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b81072caa61e'
down_revision = 'f05e04284523'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosage_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dosage_type_name'), 'dosage_type', ['name'], unique=True)
    op.create_table('dosage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('d_from', sa.Integer(), nullable=True),
    sa.Column('d_to', sa.Integer(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=True),
    sa.Column('dosage_type_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dosage_type_id'], ['dosage_type.id'], ),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicine.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('animal_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal_type',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.drop_table('dosage')
    op.drop_index(op.f('ix_dosage_type_name'), table_name='dosage_type')
    op.drop_table('dosage_type')
    # ### end Alembic commands ###
