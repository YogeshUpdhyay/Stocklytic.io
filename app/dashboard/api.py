from flask import Blueprint, jsonify, request

from app.utils.stock import Stock

bp = Blueprint("api", __name__, url_prefix="/api/v1")

stock = Stock()

@bp.route("/stockdetail", methods=["GET", "POST"])
def stock_detail():
    ticker = request.form["ticker"]
    print(ticker)
    data = stock.get_data("NSE:{}".format(ticker))
    print(data)
    return jsonify(msg="Success")

