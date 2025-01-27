from flask import Blueprint, render_template, render_template, request, redirect, url_for
from app.controllers.trivia_controller import get_all_trivias, get_questions_by_trivia
from app.controllers.trivia_controller import create_trivia_title

create_trivia_bp = Blueprint('create_trivia', __name__)

@create_trivia_bp.route('/create_trivia', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = create_trivia_title(request)
        if result:
            return redirect(url_for('trivia.index'))
        else:
            return render_template('create_trivia/index.html')
    trivia = get_all_trivias()
    questions_by_trivia  = get_questions_by_trivia()
    return render_template('trivia/index.html', trivias = trivia, questions_by_trivia = questions_by_trivia)

# @create_trivia_bp.route('/create_trivia/questions')
# def questions():
#     return render_template('create_questions/index.html')
