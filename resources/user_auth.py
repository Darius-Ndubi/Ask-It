from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from app import api
from app.model.manUser import ManageUsersDAO

ns = api.namespace('auth', description='User authentication operations')

user_signup = api.model('Sign Up', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='Your Email'),
    'username': fields.String(required=True, description='Your username'),
    'password': fields.String(required=True, description='Your password'),
    'confirm_password':fields.String(required=True, description='Confirm your password'),
})


UAO=ManageUsersDAO()


@ns.route('/signup')
@ns.response(409, 'Email Conflict')
@ns.response(400, 'Incorrect Input')
class SignUp(Resource):
    '''Allows a user to sign up'''
    @ns.doc('New user signup')
    @ns.expect(user_signup)
    @ns.response(201, 'Account created')
    def post(self):
        return UAO.add_user_details(api.payload)