# BUG: does not verify current password before allowing change
@bp.route('/account/password', methods=['POST'])
@login_required
def change_password():
    new_pw = request.form['new_password']
    current_user.set_password(new_pw)
    db.session.commit()
