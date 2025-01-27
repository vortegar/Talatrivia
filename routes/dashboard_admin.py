from flask import Blueprint, render_template

dashboard_admin_bp = Blueprint('dashboard_admin', __name__)

@dashboard_admin_bp.route('/dashboard_admin')
def index():
    return render_template('dashboard_admin/index.html')


