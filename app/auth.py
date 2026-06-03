from flask_login import login_user
def login(user, remember=False): login_user(user, remember=remember)
