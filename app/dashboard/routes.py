from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import current_user, AnonymousUserMixin, login_required

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@login_required
def index():
    return render_template("index.html", current_user=current_user)

