import pytest
from flask import json
from app import app
from tests.test_user_auth import login_token,mock_reg

mock_ans=[{"description":""},
          {"description":123546},
          {"description":"How do i add api secret key in python?"}]

def test_Answer_empty_description():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[0]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)


def test_Answer_int_description():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[1]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)


def test_Answer_successfull_description_post():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[2]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 201)
