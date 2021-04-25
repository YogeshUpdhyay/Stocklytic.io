from flask import Blueprint, render_template

bp = Blueprint("user", __name__)

@bp.route("/login")
def login():
    return render_template("index.html")