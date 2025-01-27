from flask import Blueprint, render_template, render_template, request, redirect, url_for
from app.controllers.trivia_controller import create_question

create_question_bp = Blueprint('create_question', __name__)

@create_question_bp.route('/create_question', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = create_question(request)
        if result:
            return redirect(url_for('create_question.index'))
        else:
            return render_template('create_question/index.html')
    return render_template('create_question/index.html')

