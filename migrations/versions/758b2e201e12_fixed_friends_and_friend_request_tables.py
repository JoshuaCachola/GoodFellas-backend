"""fixed friends and friend request tables

Revision ID: 758b2e201e12
Revises: 11d2e2439f98
Create Date: 2020-06-23 14:30:45.419077

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '758b2e201e12'
down_revision = '11d2e2439f98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('transactions')
    op.drop_table('group_users')
    op.drop_table('expenses')
    op.drop_table('groups')
    op.drop_table('friend_requests')
    op.add_column('friendships', sa.Column(
        'status', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('friendships', 'status')
    op.create_table('friend_requests',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('requestee_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('requester_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['requestee_id'], ['users.id'], name='friend_requests_requestee_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['requester_id'], ['users.id'], name='friend_requests_requester_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='friend_requests_pkey')
                    )
    op.create_table('groups',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        "nextval('groups_id_seq'::regclass)"), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.Column('image', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='groups_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('expenses',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        "nextval('expenses_id_seq'::regclass)"), autoincrement=True, nullable=False),
                    sa.Column('amount', postgresql.DOUBLE_PRECISION(
                        precision=53), autoincrement=False, nullable=False),
                    sa.Column('description', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('is_settled', sa.BOOLEAN(),
                              autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='expenses_user_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='expenses_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('comments',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('comment', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('transaction_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['transaction_id'], [
                        'transactions.id'], name='comments_transaction_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='comments_user_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='comments_pkey')
                    )
    op.create_table('group_users',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('group_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['group_id'], ['groups.id'], name='group_users_group_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='group_users_user_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='group_users_pkey')
                    )
    op.create_table('transactions',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('amount', postgresql.DOUBLE_PRECISION(
                        precision=53), autoincrement=False, nullable=False),
                    sa.Column('paid_on', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=True),
                    sa.Column('is_settled', sa.BOOLEAN(),
                              autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('expense_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['expense_id'], ['expenses.id'], name='transactions_expense_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='transactions_user_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='transactions_pkey')
                    )
    # ### end Alembic commands ###
