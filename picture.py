import os
import json
#from questions_answers import questions

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"


def get_user(username):# -------------------------Adding username into user_data
    with open(USER_FILE_NAME, "r+") as user_data:
        all_user_dicts = json.load(user_data)
        
        for dict in all_user_dicts:
            if dict["name"] == username:
                return dict
            else:
                return ""

def save_user(user_dict):# ----------------------- Saving username
    with open(USER_FILE_NAME, "r+") as user_data:
        
        all_user_dicts = json.load(user_data)
        
        def search(user_dict, user_data):
            return next((dict for dict in user_data if dict["name"] == user_dict["name"]), False)

        if search(user_dict, all_user_dicts):
            pass
        else:
            all_user_dicts.append(user_dict)
            with open(USER_FILE_NAME, "w+") as user_data:
                user_data.write(json.dumps(all_user_dicts, sort_keys=True, indent=4, default=str))


def list_of_all_questions(question_list):#--------------------List of all questions 
    with open(questions_answers_file,"r") as all_questions:
        quest = json.dumps(all_questions)
        return quest
        

def get_questions(question_id):#------------------------------Getting question ID 
    with open(questions_answers_file, "r") as quest_id:
        quest_id = json.dumps('{"id":""}')
        quest_id['id']
        return get_questions



# def dict_answer_comp():
#     dict_comp = []
#     for key, value in zip (USER_FILE_NAME, questions_answers_file):
#         dict_comp[key, value] = questions_answers_file


def users_answers(username_answer):# ------------------ Checking users answer 
    with open(questions_answers_file,"r") as question:
        all_users_answers = json.load(question)
        
        for dict in all_users_answers:
            if dict["answer"] == username_answer:
                pass
            else:
                return "Try again"

# print dict_answer_comp
#def get_leaderboard():
    
test_dict = {"name": "foo", "points": 999}
save_user(test_dict)

# Run whole project
def main():
    if __name__ == "__main__":
        main()