from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import current_user, AnonymousUserMixin, login_required

from .models import Stock

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@login_required
def index():
    # index page 
    return render_template("index.html", current_user=current_user)


@bp.route("/stocks/<id>")
def stock(id):
    stock = Stock.query.filter_by(id=id).first()
    return render_template("stockdetail.html",
                            current_user=current_user,
                            stock=stock)


@bp.route("/stocks")
def stocks():
    stocks = Stock.query.filter_by(userid = current_user.id)

    return render_template("stocks.html", 
                            current_user=current_user,
                            stocks=stocks)
