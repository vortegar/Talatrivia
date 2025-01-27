from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.models.associative_tables import permisse_to_play, question_trivia

# Modelo Trivia
class Trivia(db.Model):
    __tablename__ = "trivia"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    users = relationship("User", secondary=permisse_to_play, back_populates="trivias")
    question = relationship("Question", secondary=question_trivia, back_populates="trivias")

    def __repr__(self):
        return f"<Trivia(title={self.title})>"
