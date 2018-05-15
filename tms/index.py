from flask import Blueprint, render_template

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    """
        Simple blueprint for the main/index page with a search box
    """
    
    return render_template('index.html')