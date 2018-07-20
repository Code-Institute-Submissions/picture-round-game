import os
import json
from questions_answers import questions

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answer.json"


def get_user(username):
    with open(USER_FILE_NAME, "r").read():
        user_data = json.load(file)

        user_name_user_date = user_data["name"]

        if username != user_name_user_date:
            user_data["name"] = username
            file.write(json.dumps(user_data))
        else:
            pass

def save_user(user_dict):
    with open(USER_FILE_NAME, "r+") as user_data:
        
        all_user_dicts = json.load(user_data)
        
        def search(user_dict, user_data):
            return next((dict for dict in user_data if dict["name"] == user_dict["name"]), False)
        
        # for dict in all_user_dicts:
        if search(user_dict, all_user_dicts):
            print("Found!!!")
        else:
            all_user_dicts.append(user_dict)
            with open(USER_FILE_NAME, "w+") as user_data:
                user_data.write(json.dumps(all_user_dicts, sort_keys=True, indent=4, default=str))


def list_questions():
    with open(questions_answers_file,"r").read():
        return questions_answers_file


def get_questions(question_id):
    with open(questions_answers_file, "r"):
        
        questions_answers = json.load(questions_answers_file)
        
        def search(question_id, questions_answers):
            return next((dict for dict in questions_answers if dict["title"] == question_id["title"]), False)
        
        if search(question_id, questions_answers):
            print("question one!!!")
        else:
            print("no joy")

#def grade_answer(user_obj, question_id, answer):

#def get_leaderboard():

test_dict = {"name": "foo", "points": 999}
save_user(test_dict)

#Run whole project
def main():
    if __name__ == "__main__":
        main()