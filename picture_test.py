import os
import json

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
QUESTIONS_FILE_NAME = "questions_answer.json" #Trying to add question json file

user_data = []



def load_user_data(file_name):
    """
    Load Dictionary file
    """
    if not file_name.startswith('/'):
        # if not absolute, then make path relative to our location:
        file_name = os.path.join(SCRIPT_PATH, file_name)

    with open(file_name, "r") as f:
        user_data = f.read()
        user_data = json.loads(user_data)

    return user_data


    
def write_user_data(file_name, user_data):
    """
    Load Dictionary file
    """
    if not file_name.startswith('/'):
        # if not absolute, then make path relative to our location:
        file_name = os.path.join(SCRIPT_PATH, file_name)

    
    with open(file_name, "w") as f:
        f.write(json.dumps(user_data))
        #f.read()
        #user_data = json.loads(user_data)
        #print("user_data", user_data)
    
    
def add_user_data(user, user_data):
    load_user_data(USER_FILE_NAME)
    user_data.append(user)
    write_user_data(USER_FILE_NAME, user_data)

#user_data = load_user_data('user_data.json')
#write_user_data('user_data.json', user_data)

print(user_data)

user_name = input('Pick your user name ')
print('Hello', user_name)

user = user_name


add_user_data(user, user_data)

print(user_data)

questions = [
    {
        "title": "Question One",
        "photos": [
            "photo1.jpg",
            "photo2.jpg"
        ],
        "answer": "treasure island",
    },
    {
        "title": "Question Two",
        "photos": [
            "photo3.jpg",
            "photo4.jpg"
        ],
        "answer": "treasure island",
    },
]


data_answers = { 
    "round_one": "treasure island",
    "round_two": "batman",
}

def get_question(question_number):
    
    question = questions[question_number]
    
    return question['title']

def check_answer(question_number, user_answer):
    
    user_answer = user_answer.lower().strip()
    
    question = questions[question_number]
    
    result = question["answer"] == user_answer
    
    return result

    

print("get_question:", get_question(0))#question one in array
print("get_question:", get_question(1))#question two

print("check_answer:", check_answer(0, "test")) #checking function works
print("check_answer:", check_answer(0, "Treasure Island")) #checking answer should return True  
print("check_answer:", check_answer(0, " TReAsuRe Island  "))#checking answer should return True  
print("check_answer:", check_answer(0, " 123456  "))#checking answer should return False  
print("check_answer:", check_answer(0, " £$%^&*()  "))#checking answer should return False 

print("all tests passed")