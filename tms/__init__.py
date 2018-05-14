from flask import Flask

def create_app():

    app = Flask(__name__)
    
    @app.route('/')
    def movies():
        return 'The Movie Search'

    return app