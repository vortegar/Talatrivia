from flask import Blueprint, render_template

rank_bp = Blueprint('rank', __name__)

@rank_bp.route('/rank')
def index():
    return render_template('rank/index.html')


