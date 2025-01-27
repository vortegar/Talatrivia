from app import db
from sqlalchemy import Column, ForeignKey

permisse_to_play = db.Table(
    "permiss_to_play",
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column("trivia_id", ForeignKey("trivia.id", ondelete="CASCADE"), primary_key=True),
)

question_trivia = db.Table(
    "question_trivia",
    Column("question_id", ForeignKey("question.id", ondelete="CASCADE"), primary_key=True),
    Column("trivia_id", ForeignKey("trivia.id", ondelete="CASCADE"), primary_key=True),
)
