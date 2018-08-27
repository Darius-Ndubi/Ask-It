from app import api
from resources.user_auth import UAO
from app.utility.validQues_Ans import UserQuestionValidator

class QuestionDAO(object):
    

    def __init__(self):
        self.counter = 0
        self.questions = []
    

    def get_username(self,user_id):
        for user in UAO.users:
            if user.get('id') == user_id:
                return user['username']
                
    def create(self, data,user_id):
        #validate user data
        questionValidatorO = UserQuestionValidator(data['title'],data['description'])
        data_check = questionValidatorO.questionValidator()

        if data_check == True:

            uname=self.get_username(user_id)
            question = data
            question['id'] = self.counter = self.counter + 1    
            question['username']=uname
            self.questions.append(question)
            return question