import os
import json
from questions_answers import questions

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answer.json" 

user_data = []
dict_data = []


def get_user(username):
    with open("user_data.json", "r").read():
        user_data = json.load(file)
        
        user_name_user_date = user_data["name"]
        
        if username != user_name_user_date:
            user_data["name"] = username
            file.write(json.dumps(user_data))
        else:
            pass
    
def save_user(user_dict):
    with open("user_data.json","r") as user_data:
        print(user_data)
    
#        if next((dict for dict in user_data if dict["name"] == user_dict["name"]),False):
#        pass
#        else:
#            pass

#def list_questions():
#    with open(questions_answers_file,"r").read():
#        return questions_answers_file


#def get_questions(question_id, n):
#    with open(questions_answers_file, "r").read():
#        question_id = sorted(questions.values(), key = lambda t:t[1]) #Trying to order the dictionary 
    


def main(): #Run whole project
    if __name__=="__main__":
        main()