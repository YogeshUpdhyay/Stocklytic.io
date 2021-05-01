from flask import Blueprint, render_template, request
from ..models.auth import User
from ..forms.auth import LoginForm, CreateAccountForm

bp = Blueprint("user", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form)
    elif request.method == "POST":
        return(request.form.get("password"))


@bp.route("/register")
def register():
    form = CreateAccountForm()
    return render_template("register.html", form=form)

@bp.route("/logout")
def logout():
    pass