from flask import Blueprint, render_template, request
from jinja2 import TemplateNotFound

bp = Blueprint("dashboard", __name__)


@bp.route("/")
def index():
    current_user = {
        "username": "Yogesh Upadhyay"
    }
    return render_template("index.html", current_user=current_user)

@bp.route('/<template>')
def route_template(template):

    try:

        current_user = {
            "username": "Yogesh Upadhyay"
        }

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment, current_user=current_user )

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