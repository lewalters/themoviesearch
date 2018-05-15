import requests

from flask import Blueprint, render_template
from tms import API_KEY

# Link format: https://api.themoviedb.org/3/movie/<id>?api_key=<api_key>
API_LINK = 'https://api.themoviedb.org/3/movie/'

bp = Blueprint('details', __name__, url_prefix='/movie')

@bp.route('/<id>')
def details(id):
    """
        Blueprint for the movie details page
    """

    response = requests.get(API_LINK + id, params={'api_key': API_KEY})

    return render_template('details.html', details=response.json())