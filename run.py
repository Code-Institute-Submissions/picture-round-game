import os 
import json
from flask import Flask, render_template, request, redirect, flash

from picture import save_user, list_questions, get_questions
#import picture_test2

app = Flask (__name__)

USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=["GET", "POST"])
def user():
    """Main page with instructions"""
    # Handle the POST request
    if request.method == "POST":
        username = request.form.get("username").lower()
                
        user_dict = {   
            "name": username, 
            "score": 0,
            "checkpoint": 1
        }
            
        save_user(user_dict)
            
        return redirect("/?username=" + username)
    
    # Handle the GET request
    else:   
        username = request.args.get("username")
        return render_template("index.html", username=username)

#with open(questions_answers_file) as user_obj:
#    USER_OBJ = json.load(user_obj)

@app.route("/question")
def question():
    data = []
    with open("questions_answers.json", "r") as quest_anws_data:
        data = json.load(quest_anws_data)
    return render_template("question.html", quest=data)

@app.route('/answer-question', methods=["GET","POST"])
def answer_question():
    score = 0
    

    
    #if request.method == "POST":
        
        # question_id = request.form.to_dict()
        
        # print(question_id)
        
        # if request.form["answer"].lower() == question_id["answer"]:
        #     score += 1
        #     question_id += 1
        #     flash("Correct answer")
        #return render_template("index.html", username="andy")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
