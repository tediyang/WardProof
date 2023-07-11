#!/usr/bin/python3
"""
  Setup a flask-restful API
"""

from flask import Flask, make_response, jsonify
from flask_bcrypt import Bcrypt
from models import storage
from flasgger import Swagger
from os import environ
from flask_cors import CORS
from api.v1.auth import auth_parent
from api.v1.auth import auth_school
from flask_jwt_extended import JWTManager


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = environ.get("WARDPROOF_KEY")
app.register_blueprint(auth_school)
app.register_blueprint(auth_parent)
CORS(app)
jwt = JWTManager(app)

@app.teardown_appcontext
def close_dbsession(error):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    404 Error response:
        resource not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'WardProof RESTFUL API'
    }

Swagger(app)


if __name__ == "__main__":
    host = environ.get('WARDPROOF_HOST', '0.0.0.0')
    port = environ.get('WARDPROOF_PORT', '5000')
    app.run(host=host, port=port, debug=True)
