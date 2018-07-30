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
    # Handle the POST request
    if request.method == "POST":

        username = request.form.get("username").lower()
        session["username"] = username
        
        user_dict = {
            "name": username,
            "score": 0
        }

        save_user(user_dict)

        return redirect("/answer-question")
    
    # Handle the GET request
    else:
        return render_template("index.html")


@app.route("/question")
def question():
    data = []
    with open("questions_answers.json", "r") as quest_anws_data: # You are telling json that you are planning to read the file
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
        return redirect("/results")
        

        # question ID received from user. pull question and compare both answers .lower() to get the correct for which ever question/checkpoint the user is on.
        # --------------------------------------------FIRST METHOD
        
       
        #[i for i, j in (get_questions_id, list_of_all_questions) if i == j]
        
        # --------------------------------------------SECOND METHOD 
        # def search(list_of_all_questions, get_questions_id):
        #     return next((dict for dict in get_questions_id if dict["id"].lower() == list_of_all_questions["id"].lower()), False)
            
        # if search(list_of_all_questions, get_questions_id):
        #     pass
        # else:
        #     print("wrong question")
            
        
        #Comparing dicts 
        
        
        return render_template("question.html")#This needs to be changed to next question
    else:
        username = session["username"]
        
        user_dict = get_user(username)
        print("user_dict", user_dict)
        checkpoint = user_dict["checkpoint"]
        
        # Get the first question here (or the question on the user's checkpoint)
        # You have to get a user's JSON dictionary, there is already a function that does it
        # Then get the "checkpoint" for that user
        # Then go over a list of all questions, and get the correct question using the checkpoint
        # Then pass that question as a dictionary to question.html
        
        return render_template("question.html", username=username)

@app.route('/results', methods=["GET"])
def resulsts():
    
    #user_data = get_user_data()
    
    return render_template("results.html", leaderboard=[1,2,3])
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
