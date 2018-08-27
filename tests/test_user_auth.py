import pytest
from flask import json
from app import app

mock_reg=[{"email":"","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelightgmail.com","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":123454,"username":"delight","password":"delight","confirm_password":"delight"},

          {"email":"yagamidelight@gmail.com","username":"delight","password":"string@12","confirm_password":"string@12"},

          {"email":"yagamidelight@gmail.com","username":"delight","password":123,"confirm_password":123},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight@11","confirm_password":"delight@1"},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight","confirm_password":"delight"},

          {"email":"yagamidelight@gmail.com","username":12334,"password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"      ","password":"delight","confirm_password":"delight"}
]


#email checks
def test_signup_empty_email():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[0]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    #assert response == {"Email: {} is not well formatted (Must have @ and .com".format(mock_reg[0].get('email'))}
    assert(response.status_code == 400)

def test_signup_wrong_email1():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[1]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_wrong_email2():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[2]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_int_email():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[3]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#password checks
def test_signup_int_password():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[5]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    #assert response == {"Email: {} is not well formatted (Must have @ and .com".format(mock_reg[0].get('email'))}
    assert(response.status_code == 400)

def test_signup_passwords_unmatching():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[6]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_poor_passwords():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[7]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#username checks
def test_signup_int_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[8]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_empty_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[9]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_spaces_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[10]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#test correct data
def test_signup_correct_data():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[4]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert (response.status_code == 201)

