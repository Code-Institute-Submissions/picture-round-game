import os 
import json
from flask import Flask, render_template, request, redirect

from picture import save_user, list_questions, get_questions,  grade_answer
#import picture_test2

USER_FILE_NAME = "user_data.json"

app = Flask (__name__)

@app.route('/', methods=["GET", "POST"])
def index():
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


@app.route('/answer-question', methods=["GET","POST"])
def answer_question():
    
    if request.method == "POST":
        answer = request.form.get("answers" + grade_answer) # Correct answer
        return redirect("/?answer-question=") # Next answer
    else:
        answer = request.args.get("get_questions")
        return render_template("/question-heading-one")
    print(request.form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
