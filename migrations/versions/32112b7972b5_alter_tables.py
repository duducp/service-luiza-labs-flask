"""alter_tables

Revision ID: 32112b7972b5
Revises: f28ddf147a18
Create Date: 2019-10-25 20:50:54.470652

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '32112b7972b5'
down_revision = 'f28ddf147a18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_favorite_products_product_id', table_name='favorite_products')
    op.drop_table('favorite_products')
    op.add_column('favorites', sa.Column('product_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_index(op.f('ix_favorites_product_id'), 'favorites', ['product_id'], unique=False)
    op.create_unique_constraint(None, 'favorites', ['client_id', 'product_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorites', type_='unique')
    op.drop_index(op.f('ix_favorites_product_id'), table_name='favorites')
    op.drop_column('favorites', 'product_id')
    op.create_table('favorite_products',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('favorite_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('product_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], name='favorite_products_favorite_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorite_products_pkey'),
    sa.UniqueConstraint('favorite_id', 'product_id', name='favorite_products_favorite_id_product_id_key')
    )
    op.create_index('ix_favorite_products_product_id', 'favorite_products', ['product_id'], unique=False)
    # ### end Alembic commands ###
