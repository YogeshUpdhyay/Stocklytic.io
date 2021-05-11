from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, request, redirect, url_for

from .models import User
from .. import login_manager, db
from .forms import LoginForm, CreateAccountForm, ForgotPasswordForm

bp = Blueprint("user", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form)
    else:

        # read form data
        email = request.form['email']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(email=email).first()

        # Check the password
        if user and user.check_password(password):

            login_user(user)
            return redirect(url_for('dashboard.index'))

        # Something (user or pass) is not ok
        login_form = LoginForm()
        return render_template( 'login.html', msg='Wrong user or password', form=login_form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":

        # registeration page 
        form = CreateAccountForm()
        return render_template("register.html", form=form)
    else:
        
        username  = request.form['username']
        email     = request.form['email']

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            form = CreateAccountForm()
            return render_template( 'register.html', 
                                    msg='Username already registered',
                                    form=form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            form = CreateAccountForm()
            return render_template( 'register.html', 
                                    msg='Email already registered', 
                                    form=form)

        # else we can create the user
        user = User(**request.form)
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return render_template('index.html', current_user=user)


@bp.route("/logout")
@login_required
def logout():
    # logout a user
    logout_user()
    form = LoginForm()
    return redirect(url_for('user.login'))

@bp.route("/forgotpassword", methods=["GET", "POST"])
def forgot_password():
    if request.method == "GET":
        form = ForgotPasswordForm()
        return render_template("forgotpassword.html", form=form)
    else:
        email = request.form['email']

        form=ForgotPasswordForm()

        user = User.query.filter_by(email = email).first()
        print(user)
        if not user:
            return render_template("forgotpassword.html", form=form, msg="Email not found")

        # Send reset email to the user

        return render_template("forgotpassword.html", msg="Reset link has been sent to your email id", form=form)



## Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('user.login'))

@bp.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500