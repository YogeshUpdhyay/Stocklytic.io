import json
from flask import Blueprint, request
import talib as ta

from app.utils.stock import Stock

bp = Blueprint("api", __name__, url_prefix="/api/v1")

stock = Stock()

@bp.route("/stockdetail", methods=["GET", "POST"])
def stock_detail():
    # reading args
    ticker = request.form["ticker"]
    indicator = request.form["indicator"] if request.form["indicator"] != "" else None
    # intraday_mode = request.form["intraday-mode"]

    data = stock.get_data(ticker)
    try:
        if indicator:
            indicator_function = getattr(ta, indicator)
            result = indicator_function(data["Close"], timeperiod=2)
            data["Indicator"] = result
    except Exception as e:
        pass

    # graph data
    graph_data = stock.parse_data(data)
    return json.dumps(graph_data)

