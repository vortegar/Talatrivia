from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.models.associative_tables import permisse_to_play

# Modelo User
class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    role = Column(String, nullable=False)

    trivias = relationship("Trivia", secondary=permisse_to_play, back_populates="users")

    def __repr__(self):
        return f"<User(username={self.username})>"
