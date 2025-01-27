from flask import Blueprint, render_template, render_template, request, redirect, url_for
from app.controllers.trivia_controller import get_all_trivias, get_questions_by_trivia
from app.controllers.trivia_controller import create_trivia_title

trivia_bp = Blueprint('trivia', __name__)

@trivia_bp.route('/trivia')
def index():
    trivia = get_all_trivias()
    questions_by_trivia  = get_questions_by_trivia()
    return render_template('trivia/index.html', trivias = trivia, questions_by_trivia = questions_by_trivia)

@trivia_bp.route('/create_trivia', methods=['GET', 'POST'])
def save_trivia():
    if request.method == 'POST':
        result = create_trivia_title(request)
        if result:
            return redirect(url_for('create_question.index'))
        else:
            return render_template('create_trivia/index.html', error='Error al crear la trivia.')
    else:
        return render_template('create_trivia/index.html')

@trivia_bp.route('/assign-trivia', methods=['GET', 'POST'])
def assign_trivia():
    if request.method == 'POST':
        result = create_trivia_title(request)
        if result:
            return redirect(url_for('create_question.index'))
        else:
            return render_template('create_trivia/index.html', error='Error al crear la trivia.')
    else:
        return render_template('create_trivia/index.html')
