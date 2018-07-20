import os
import json
from questions_answers import questions
SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))
USER_FILE_NAME = "user_data.json"
QUESTIONS_FILE_NAME = "questions_answer.json"

 

#global user_data 
user_data = []
dict_data = []

def questions_answers(file_name):
    
    if not file_name.startswith('/'):
        file_name = os.path.join(SCRIPT_PATH, file_name)
        
    with open("questions_answers.py") as json_file:
        dict_data = json.load(json_file.read())
        print("title" + "photos" + "answer")
    
    return dict_data
    

def load_user_data(file_name):
    
    if not file_name.startswith('/'):
        # if not absolute, then make path relative to our location:
        file_name = os.path.join(SCRIPT_PATH, file_name)

    with open(file_name, "r") as f:
        user_data = f.read()
        user_data = json.loads(user_data)

    return user_data


    
def write_user_data(file_name, user_data):
    
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

user_data = load_user_data(USER_FILE_NAME)

score = 0

user = {}
user['score'] = 1
user['name'] = input ("What is your name? ")
user_data.append(user)

write_user_data(USER_FILE_NAME, user_data)

print("Hello", user_data)


data_answers = { 
    "round_one": "treasure island",
    "round_two": "batman",
    "round_three": "charlotte's web",
    "round_four": "jungle book",
    "round_five": "the arabian nights",
    "round_six": "king solomon's mines",
}

def get_question(question_number):
    
    question = questions[question_number]
    
    return question['title']

def check_answer(question_number, user_answer):
    
    user_answer = user_answer.lower().strip()
    
    dict_data = open("questions_answers.py", "r")
    question = questions[question_number]
    
    result = question["answer"] == user_answer
    
    return result
    

print("Your current score is", score)

print("get_question:", get_question(0))#question one in array
print("get_question:", get_question(1))#question two
print("get_question:", get_question(2))#question three
print("get_question:", get_question(3))#question four
print("get_question:", get_question(4))#question five
print("get_question:", get_question(5))#question six

print("check_answer:", check_answer(0, "test")) #checking function works
print("check_answer:", check_answer(0, "Treasure Island")) #checking answer should return True  
print("check_answer:", check_answer(0, " TReAsuRe Island  "))#checking answer should return True  
print("check_answer:", check_answer(0, " 123456  "))#checking answer should return False  
print("check_answer:", check_answer(0, " £$%^&*()  "))#checking answer should return False
print("check_answer:", check_answer(2, "charlotte's web"))#Answer should returen true 
print("check_answer:", check_answer(3, "jungle book"))#Answer should returen true 
print("check_answer:", check_answer(4, "the arabian nights"))#Answer should returen true 
print("check_answer:", check_answer(5, "king solomon's mines"))#Answer should returen true 

print("all tests passed")