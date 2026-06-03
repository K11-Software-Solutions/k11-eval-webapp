# BUG: no admin role check — any logged-in user can access
@bp.route('/admin/users')
@login_required
def admin_users():
    return User.query.all()
