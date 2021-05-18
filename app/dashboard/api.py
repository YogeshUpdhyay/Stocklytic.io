import os
import json
from flask import Blueprint, request
import talib as ta

from app.utils.stock import Stock

bp = Blueprint("api", __name__, url_prefix="/api/v1")

stock = Stock()

def get_indicator_desc(indicator) -> str:
    indicators = json.load(open(os.path.join(os.getcwd(), "app/utils/static/indicators.json"), 'r'))
    try:
        return indicators[indicator]
    except Exception as e:
        return None

@bp.route("/stockdetail", methods=["GET", "POST"])
def stock_detail():
    # reading args
    ticker = request.form["ticker"]
    indicator = request.form["indicator"] if request.form["indicator"] != "" else None
    # intraday_mode = request.form["intraday-mode"]

    # defining response
    response = {}

    response["name"] = stock.get_info(ticker)

    data = stock.get_data(ticker)
    try:
        if indicator:
            indicator_function = getattr(ta, indicator)
            result = indicator_function(data["Close"], timeperiod=2)
            data["Indicator"] = result

            response["indicator"] = get_indicator_desc(indicator)

    except Exception as e:
        pass

    # graph data
    graph_data = stock.parse_data(data)

    response['graph_data'] = graph_data

    return json.dumps(response)

