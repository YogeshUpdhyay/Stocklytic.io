from flask import Blueprint, render_template

bp = Blueprint("stock", __name__)

@bp.route("/stock/{id}")
def login():
    return render_template("stock.html")