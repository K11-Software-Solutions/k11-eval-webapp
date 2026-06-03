from flask import Blueprint
bp = Blueprint('profile', __name__)
@bp.route('/profile')
def profile(): return 'Profile'
