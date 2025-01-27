from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.login_controller import login_controller
from flask import session
from app.models.user import User

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if login_controller(email, password):
            user = User.query.filter_by(email=email).first()
            if user.role == 'admin':
                return redirect(url_for('dashboard_admin.index'))
            else:
                return redirect(url_for('trivia.index'))
        else:
            return render_template('login/index.html', error="Credenciales inválidas")
    return render_template('login/index.html')
