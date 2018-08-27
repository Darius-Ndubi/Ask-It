from app import api
from app.utility.validUser import UserAuthValidator
from werkzeug.security import generate_password_hash


class ManageUsersDAO(object):
    def __init__(self):
        self.users=[]
        
    
    def check_user_email(self,email):
        for user in self.users:
            if user.get('email') == email:
                
                return email

    def add_user_details(self,data):
        #user input validation checks
        uservalidatorO=UserAuthValidator(data['email'],data['username'],data['password'],data['confirm_password'])
        data_check = uservalidatorO.signupValidator()

        if data_check == True:

            if self.check_user_email(data['email']) != None:
                api.abort(409, "Sign up request for {} could not be completed due to existance of same email".format(data['email']))
            
            data['id'] = len(self.users)+1
            password_hash = generate_password_hash(data['password'])

            data['password'] = password_hash
            data['confirm_password']='#'

            self.users.append(data)

            #print (self.users)
        
            return "Sign Up was successful proceed to Sign In",201