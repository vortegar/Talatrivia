"""Create tables

Revision ID: 87bdab460637
Revises: a0fe34fb2bc3
Create Date: 2025-01-26 08:40:14.823178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87bdab460637'
down_revision = 'a0fe34fb2bc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=120), nullable=False),
    sa.Column('answer', sa.String(length=120), nullable=False),
    sa.Column('level', sa.String(length=120), nullable=False),
    sa.Column('option1', sa.String(length=120), nullable=False),
    sa.Column('option2', sa.String(length=120), nullable=False),
    sa.Column('option3', sa.String(length=120), nullable=True),
    sa.Column('option4', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_trivia',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('trivia_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['trivia_id'], ['trivia.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('question_id', 'trivia_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_trivia')
    op.drop_table('question')
    # ### end Alembic commands ###
