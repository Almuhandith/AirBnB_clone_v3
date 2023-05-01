#!/usr/bin/python3
""" Script that imports a Blueprint and runs Flask """
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_storage(exception):
    """Closes the database connection"""
    storage.close()

if __name__ == "__main__":

     host = getenv('HBNB_API_HOST', default='0.0.0.0')
     port = getenv('HBNB_API_PORT', defaut=5000)

     app.run(host, int(port), threaded=True)
