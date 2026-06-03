from flask import session
# BUG: session secret key hardcoded
SECRET_KEY = 'dev-secret-123'
def login_user(user_id): session['user_id'] = user_id
