from flask import session
from collections import defaultdict

from app import db
from flask import session
from app.models.user import User
from app.models.trivia import Trivia
from app.models.question import Question
from app.models.associative_tables import permisse_to_play

from app.models.trivia import Trivia
from sqlalchemy.exc import OperationalError

from flask import jsonify

def get_all_trivias():
    user_id = session.get('user_id')
    trivias = Trivia.query.join(permisse_to_play).join(User).filter(User.id == user_id).all()

    return trivias

def get_questions_by_trivia():
    user_id = session.get('user_id')

    trivias = Trivia.query.filter(Trivia.users.any(id=user_id)).all()

    questions_by_trivia = defaultdict(list)

    for trivia in trivias:
        trivia_data = {
            'title': trivia.title,
            'questions': []
        }

        for question in trivia.question:
            trivia_data['questions'].append(question)

        questions_by_trivia[trivia.id] = trivia_data

    return questions_by_trivia

def create_trivia_title(request):
    title = request.form.get('title')

    if not title:
        return False

    new_trivia = Trivia(title=title)

    try:
        db.session.add(new_trivia)
        db.session.commit()
    except OperationalError as e:
        db.session.rollback() 
        print(f"Error al guardar la trivia: {e}")
        return False

    return True

def create_question(request):
    title = request.form.get('title')

    if not title:
        return False

    new_trivia = Trivia(title=title)

    try:
        db.session.add(new_trivia)
        db.session.commit()
    except OperationalError as e:
        db.session.rollback() 
        print(f"Error al guardar la trivia: {e}")
        return False

    return True

def create_question(request):
    question = request.form.get('question')
    answer = request.form.get('answer')
    level = request.form.get('level')
    option1 = request.form.get('option1')
    option2 = request.form.get('option2')
    option3 = request.form.get('option3') 
    option4 = request.form.get('option4')  

    if not question or not answer or not level or not option1 or not option2:
        return False

    new_question = Question(
        question=question,
        answer=answer,
        level=level,
        option1=option1,
        option2=option2,
        option3=option3,
        option4=option4
    )

    db.session.add(new_question)
    db.session.commit()
    return True
def create_trivia_by_question():
    try:
        users = User.query.all()
        questions = Question.query.all()
        trivias = Trivia.query.all()

        users_data = [{"id": user.id, "name": user.username, "email": user.email} for user in users]
        questions_data = [
        {
            "id": question.id,
            "question": question.question,
            "answer": question.answer,
            "level": question.level,
            "option1": question.option1,
            "option2": question.option2,
            "option3": question.option3,
            "option4": question.option4,
            "trivias": [{"id": trivia.id, "title": trivia.title} for trivia in question.trivias]
        } for question in questions]

        trivias_data = [{"id": trivia.id, "title": trivia.title} for trivia in trivias]

        return {
            "users": users_data,
            "questions": questions_data,
            "trivias": trivias_data
        }
    except OperationalError as e:
        print(f"Error al recuperar los datos: {e}")
        return jsonify({"error": "Error al recuperar los datos"})
    
def get_data_trivia(request):
    user_id = request.form.get('user_id')
    trivia_id = request.form.get('trivia_id')
    selected_questions = request.form.getlist('questions')
    print('aca va el id',user_id)
    user = User.query.get(user_id)
    trivia = Trivia.query.get(trivia_id)
    print(user, trivia)
    if not user or not trivia:
        return False
    
    if trivia not in user.trivias:
        user.trivias.append(trivia)

    for question_id in selected_questions:
        question = Question.query.get(question_id)
        if question:
            trivia.question.append(question)

    db.session.commit()
    return True


