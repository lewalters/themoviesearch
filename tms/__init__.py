from flask import Flask

def create_app():

    app = Flask(__name__)
    
    from tms import index
    app.register_blueprint(index.bp)

    from tms import search
    app.register_blueprint(search.bp)

    return app