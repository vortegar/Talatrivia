from flask import Blueprint, render_template, render_template, request, redirect, url_for
from app.controllers.trivia_controller import get_data_trivia
from app.controllers.trivia_controller import create_trivia_by_question

assign_trivia_bp = Blueprint('assign_trivia', __name__)

@assign_trivia_bp.route('/assign_trivia', methods=['GET', 'POST'])
def index():
    data = create_trivia_by_question()
    
    users = data.get('users', [])
    questions = data.get('questions', [])
    trivias = data.get('trivias', [])
    if request.method == 'POST':
        result = get_data_trivia(request)
        if result:
            return redirect(url_for('dashboard_admin.index'))
        else:
            return render_template('dashboard_admin/index.html')
    return render_template('assign_trivia/index.html' ,   users=users, questions=questions, trivias=trivias)

