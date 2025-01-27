from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.register_contoller import register

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET'])
def index():
    return render_template('register/index.html')

@register_bp.route('/register', methods=['POST'])
def register_user():
    result = register(request)
    if result:
        return redirect(url_for('trivia.index')) 
    else:
        return render_template('register/index.html') 
