from flask import session
from app.controllers.trivia_controller import get_all_trivias
from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    all_trivias = get_all_trivias()
    return render_template('dashboard/index.html', trivias=all_trivias)


@dashboard_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  
    return redirect(url_for('dashboard.index')) 