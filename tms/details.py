import json
import requests

from flask import Blueprint, render_template
from tms import API_KEY

API_LINK = 'https://api.themoviedb.org/3/movie/'

bp = Blueprint('details', __name__, url_prefix='/movie')

@bp.route('/<id>')
def details(id):
    response = requests.get(API_LINK + id, params={'api_key': API_KEY})
    responseJSON = json.loads(response.text)

    return render_template('details.html', details=responseJSON)