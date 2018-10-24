import os
import json
#from questions_answers import questions

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"


def get_user(username):# ----------------------------------------- Adding username into user_data
    with open(USER_FILE_NAME, "r+") as user_data:
        all_user_dicts = json.load(user_data)
        print("all_user_dicts", all_user_dicts, )
        print("username", username)
        for dict in all_user_dicts:
            if dict["name"] == username:
                return dict
        
        return ""

def save_user(user_dict):# --------------------------------------- Saving username
    with open(USER_FILE_NAME, "r+") as user_data:
        
        all_user_dicts = json.load(user_data)
        
        def search(user_dict, user_data):
            return next((dict for dict in user_data if dict["name"] == user_dict["name"]), False)

        found = search(user_dict, all_user_dicts)
        if found:
            found['name'] = user_dict['name']
            found['score'] = user_dict['score']
            #found['checkpoint'] = user_dict['checkpoint']
            with open(USER_FILE_NAME, "w+") as user_data:
                user_data.write(json.dumps(all_user_dicts, sort_keys=True, indent=4, default=str))
        else:
            all_user_dicts.append(user_dict)
            with open(USER_FILE_NAME, "w+") as user_data:
                user_data.write(json.dumps(all_user_dicts, sort_keys=True, indent=4, default=str))


def list_of_all_questions():#----------------------- List of all questions 
    with open(questions_answers_file,"r") as all_questions:
        quest = json.dumps(all_questions.read())
        return quest
        

def get_question_by_id(question_id):#------------------------------ Getting question ID 
    with open(questions_answers_file, "r") as question_file:
        questions = json.loads(question_file.read())
        for q in questions:
            if q["id"] == question_id:
                return q
        return None
        
def users_answers(username_answer):# ---------------------------- Checking users answer 
    with open(questions_answers_file,"r") as question:
        all_users_answers = json.dumps(question)
        
        for dict in all_users_answers:
            if dict["answer"] == username_answer:
                pass
            else:
                return "Try again"

def main():
    if __name__ == "__main__":
        main()
        


