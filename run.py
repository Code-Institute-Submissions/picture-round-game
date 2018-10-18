import os 
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session
from picture import save_user, get_user, list_of_all_questions, get_question_by_id

app = Flask (__name__, static_url_path='/static')
app.secret_key = "my_super_secret_key"

USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"


@app.route('/', methods=["GET", "POST"])
def user():
    """Main page with instructions"""
    if request.method == "POST":

        username = request.form.get("username").lower()
        session["username"] = username
        
        user_dict = {
            "name": username,
            "score": 0,
        }

        save_user(user_dict)

        return redirect("/answer-question")
    
    else:
        return render_template("index.html")


@app.route("/question")
def question():
    data = []
    with open("questions_answers.json", "r") as quest_anws_data: # telling json we are planning to read file
        data = json.loads(quest_anws_data.read())
    return render_template("question.html", quest=data)


@app.route('/answer-question', methods=["GET","POST"])
def answer_question():
    score = 0
    
    if request.method == "POST":
        
        score = 0
        for key, value in request.form.items():
            question_id = key
            answer = value
            
            question = get_question_by_id(int(question_id))
            if question['answer'] == answer.lower():
                score += 10
                
        print("score", score)
        print("username", session["username"])
        
        
        user_dict = {
            "name": session["username"],
            "score": score
        }
        save_user(user_dict)
        print(user_dict)
        return render_template("results.html", user_dict=user_dict["name"])

        #return render_template("question.html")#This needs to be changed to next question
    else:
        username = session["username"]
        
        user_dict = get_user(username)
        print("user_dict", user_dict)
        #checkpoint = user_dict["checkpoint"]
        

        return render_template("question.html", username=username)

# @app.route('/results', methods=["GET"])
# def results():
    
    
#     score = 0
#     user_dict = {
#             "name": session["username"],
#             "score": score
#         }
#     save_user(user_dict)
#     username = session["username"]
#     user_dict = get_user(username)
#     print(user_dict)
#     return render_template("results.html", user_dict=user_dict["name"])
    #This is linking to the results html
    
    
    # with open(USER_FILE_NAME, "r") as leaderboard:
    #     user_leaderboard = json.loads(leaderboard.read())
    #     print(user_leaderboard)
        
        
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
