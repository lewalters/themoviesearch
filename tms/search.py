import json
import requests

from flask import Blueprint, render_template, request

API_LINK = 'https://api.themoviedb.org/3/search/movie'
API_KEY = '694931b7ea0714661d853f5b46ea1d7a'

bp = Blueprint('search', __name__)

@bp.route('/search')
def search():
    payload = {'api_key': API_KEY, 'query': request.args.get('query')}
    response = requests.get(API_LINK, params=payload)
    return render_template('search.html', response=json.loads(response.text))