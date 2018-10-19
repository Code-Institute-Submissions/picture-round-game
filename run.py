import os 
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session
from picture import save_user, get_user, list_of_all_questions, get_question_by_id

app = Flask (__name__, static_url_path='/static')
app.secret_key = "my_super_secret_key"

USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"

user_dict = {
            "name": "person",
            "score": 0,
        }


@app.route('/', methods=["GET", "POST"])
def user():
    """Main page with instructions"""
    if request.method == "POST":

        username = request.form.get("username").lower()
        session["username"] = username
        save_user(user_dict)
        flash("Hello, %s press start to play the game." % (session["username"]))
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
    if "username" not in session:
        return redirect("index.html")
    
    session["score"] = 0
    session["get_question_by_id"] = 0
    
    for key, value in request.form.items():
            question_id = key
            print(question_id)
            answer = value
            if question_id:
                question = get_question_by_id(int(question_id))
            if question['answer'] == answer.lower():
                session["get_question_by_id"] +=1
                session["score"] += 10
            
                if session["get_question_by_id"] < len(questions_answers_file):
                    flash("Correct answer, %s! Your score is %s." % (
                        session["username"], session["score"]))
                    print(get_question_by_id)
                else:
                    flash("Correct answer, %s!" % session["score"])
            else:
                flash("Wrong answer or mispelling, %s. Try again " % (session["username"]))
        
        
    if session["get_question_by_id"] >= len(questions_answers_file):
        if session["score"] >= user_dict["score"]:
            user_dict["score"] = session["score"]
            user_dict["name"] = session["username"]
        return render_template("results.html", username=session["username"],
                                score=session["score"],
                                highscore=user_dict["score"],
                                higherscore=user_dict["name"])
    
    return render_template("results.html")    

  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
