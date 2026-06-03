from flask import Blueprint
bp = Blueprint('dashboard', __name__)
@bp.route('/dashboard')
def dashboard(): return 'Dashboard'
