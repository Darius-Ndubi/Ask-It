from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='Ask It API',
    description='A simple Question & Answer API',)

from resources.user_auth import ns as auth
api.add_namespace(auth)