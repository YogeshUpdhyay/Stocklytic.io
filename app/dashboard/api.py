from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__, url_prefix="/api/v1")

@bp.route("/stockdetail", methods=["GET"])
def stock_detail():
    return jsonify(msg="Success")

