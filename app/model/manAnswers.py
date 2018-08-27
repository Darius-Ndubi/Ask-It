from app.model.manQuestions import QuestionDAO
from app.utility.validQues_Ans import UserQuestionValidator
from app import api
from resources.questions import DAO

class AnswerDAO(QuestionDAO):

    def __init__(self):
        self.answer_id_counter=0
        QuestionDAO.__init__(self)

    def create_answer(self, question_id, data,user_id):
        #check user answer data input
        data_check = UserQuestionValidator.answerValidator(data['description'])

        if data_check == True:
            
            uname=DAO.get_username(user_id)

            if question_id < 0:
                api.abort(400, "Request {} could not be fulfilled due to bad request".format(id)) 
            elif question_id > 0:
                answer = data
                answer['username']=uname
                questions = DAO.questions
                for question in questions:
                    if question.get('id') == question_id:
                        num_ans = len(question['answers'])
                        answer['id'] = num_ans+1
                        question['answers'].append(answer)
                        return answer
            api.abort(404, "question {} dont exist".format(question_id))   

