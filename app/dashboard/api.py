from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__, url_prefix="/api/v1")

@bp.route("/stockdetail")
def stock_detail():
    pass

