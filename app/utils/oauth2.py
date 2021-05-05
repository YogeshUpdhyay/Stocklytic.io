from flask import redirect, url_for
from flask_login import login_user
from ..auth.models import User

def handle_authorize(remote, token, user_info):
    if user_info:
        user = User.query.filter_by(email = user_info.get("email")).first()
        login_user(user)
        return redirect(url_for('dashboard.index'))
