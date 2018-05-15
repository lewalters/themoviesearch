import requests

from flask import Blueprint, render_template, request
from tms import API_KEY

# Link format: https://api.themoviedb.org/3/search/movie?api_key=<api_key>&query=<query>&page=<page>
API_LINK = 'https://api.themoviedb.org/3/search/movie'

bp = Blueprint('search', __name__)

@bp.route('/search')
def search():
    """
        Blueprint for the search results page
    """

    query = request.args.get('query')
    payload = {'api_key': API_KEY, 'query': query, 'page': request.args.get('page')}
    response = requests.get(API_LINK, params=payload)
    responseJSON = response.json()

    return render_template('search.html', page=responseJSON['page'], total_pages=responseJSON['total_pages'],
                           total_results=responseJSON['total_results'], results=responseJSON['results'],
                           query=query)