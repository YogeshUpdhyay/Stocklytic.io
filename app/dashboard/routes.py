import os
import json
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .models import Stock

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@login_required
def index():
    # index page 

    # reading indicators
    indicators = json.load(open(os.path.join(os.getcwd(), 'app/utils/static/indicators.json')))

    return render_template(
        "index.html", 
        current_user=current_user, 
        indicators=indicators
    )
