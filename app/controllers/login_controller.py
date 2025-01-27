from app.models.user import User
from flask import session
from app import db
from werkzeug.security import check_password_hash


def login_controller(email, password):
    user = User.query.filter_by(email=email).first()
    user_id = get_user_id_by_email(email)
    if not user_id:
        return False
    session['user_id'] = user_id  
    if user and check_password_hash(user.password, password):
        return True
    return False

def get_user_id_by_email(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user.id if user else None