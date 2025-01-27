from app import db
from sqlalchemy.orm import relationship
from app.models.associative_tables import question_trivia

# Modelo Question
class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)   
    question = db.Column(db.String(120), nullable=False)
    answer = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(120), nullable=False)   
    option1 = db.Column(db.String(120), nullable=False)
    option2 = db.Column(db.String(120), nullable=False)
    option3 = db.Column(db.String(120), nullable=True)
    option4 = db.Column(db.String(120), nullable=True)

    trivias = relationship("Trivia", secondary=question_trivia, back_populates="question")

    def __repr__(self):
        return f"<Question(question={self.question})>"
