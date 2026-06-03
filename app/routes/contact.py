# BUG: no CSRF protection on form submission
@bp.route('/contact', methods=['POST'])
def contact():
    send_email(request.form['email'], request.form['message'])
