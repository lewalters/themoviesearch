from flask import Flask

API_KEY = '694931b7ea0714661d853f5b46ea1d7a'

def create_app():

    app = Flask(__name__)
    
    from tms import index
    app.register_blueprint(index.bp)

    from tms import search
    app.register_blueprint(search.bp)

    from tms import details
    app.register_blueprint(details.bp)

    return app