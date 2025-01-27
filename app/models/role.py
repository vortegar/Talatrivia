from app import db

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    user = db.relationship('User', backref='role', uselist=False) 

    def __repr__(self):
        return f"<Role(name={self.name})>"
