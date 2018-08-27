from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from flask_jwt_extended import jwt_required,get_jwt_identity
from app import api
from resources.questions import answer,question
from app.model.manAnswers import AnswerDAO


ns = api.namespace('questions', description='Answers to Questions and Operations')

AAO=AnswerDAO()

@ns.route('/<int:question_id>/answers')
@ns.response(404, 'question not found')
class Answer(Resource):

    @jwt_required
    @ns.doc('List answers to question')
    @ns.marshal_list_with(answer,code=200) 
    def get(self,question_id):
        '''Geting all answers to a question'''

        user_id = get_jwt_identity()
        return AAO.find_all_answers_to_question (question_id,user_id),200


    @jwt_required
    @ns.doc('create_answer')
    @ns.expect(answer)
    @ns.marshal_with(answer, code=201)
    def post(self,question_id):
        '''Answering a single question'''

        user_id = get_jwt_identity()
        return AAO.create_answer (question_id, api.payload,user_id), 201