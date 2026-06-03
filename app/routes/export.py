# BUG: exports all users including password hashes
@bp.route('/export/users')
def export_users():
    users = User.query.all()
    return csv_response([(u.email, u.password_hash) for u in users])
