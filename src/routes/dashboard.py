from flask import Blueprint, render_template

bp = Blueprint("dashboard", __name__)

@bp.route("/")
def login():
    return render_template("index.html")
