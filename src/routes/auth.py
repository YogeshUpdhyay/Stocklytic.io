from flask import Blueprint, render_template, request
from ..models.auth import User

bp = Blueprint("user", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        return(request.form.get("password"))


@bp.route("/register")
def register():
    return render_template("register.html")