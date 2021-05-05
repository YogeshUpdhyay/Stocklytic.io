from flask import redirect, url_for, render_template
from flask_login import login_user
from werkzeug.exceptions import ServiceUnavailable

from ..auth.models import User

def handle_authorize(remote, token, user_info):
    if user_info:
        print(user_info)
        user = User.query.filter_by(email = user_info.get("email")).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard.index'))
        else:
            user = User(username = user_info.get('name'), email = user_info.get('email'))
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('dashboard.index'))
    raise ServiceUnavailable
