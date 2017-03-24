"""empty message

Revision ID: 5b7dddbe90a2
Revises: b81072caa61e
Create Date: 2017-03-20 13:33:35.215698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b7dddbe90a2'
down_revision = 'b81072caa61e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_name', sa.String(length=64), nullable=True),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('descr', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audit_object_id'), 'audit', ['object_id'], unique=False)
    op.create_index(op.f('ix_audit_table_name'), 'audit', ['table_name'], unique=False)
    op.create_foreign_key(None, 'dosage', 'medicine', ['medicine_id'], ['id'])
    op.create_foreign_key(None, 'dosage', 'unit', ['unit_id'], ['id'])
    op.create_foreign_key(None, 'dosage', 'dosage_type', ['dosage_type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dosage', type_='foreignkey')
    op.drop_constraint(None, 'dosage', type_='foreignkey')
    op.drop_constraint(None, 'dosage', type_='foreignkey')
    op.drop_index(op.f('ix_audit_table_name'), table_name='audit')
    op.drop_index(op.f('ix_audit_object_id'), table_name='audit')
    op.drop_table('audit')
    # ### end Alembic commands ###