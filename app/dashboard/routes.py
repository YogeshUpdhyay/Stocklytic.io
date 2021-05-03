from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import current_user, AnonymousUserMixin, login_required

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@login_required
def index():
    return render_template("index.html", current_user=current_user)


@bp.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(template, segment=segment, current_user=current_user)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except Exception as e:
        print(e)
        return render_template('page-500.html'), 500


# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  