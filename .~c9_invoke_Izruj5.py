import os 
import json
from flask import Flask, render_template, request, redirect

from picture import get_questions, save_user
#import picture_test2

USER_FILE_NAME = "user_data.json"

app = Flask (__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    # Handle the POST request
    if request.method == "POST":
        username = request.form.get("username").lower()
        
        """
        get("username") is an expression, getting the VALUE, of the KEY "username"
        form.get is an expression, grabbing a value from the object "form"
        request.form is an expression, grabbing the object "form" from the object "request"
        username = is an expression, assigning a value to the variable "username"
        
        All in all that line is read by python as: "get whatever the value of the key username is, on the object form, on the object request and put it in "username"
        
        Your "form" is an object created by the browser when it sees the HTML tag <form>, and it contains:
            "checkpoint":
        
        That goes into a request object, that is created by the browser when you perform a request, be it GET or POST
        
        That request object comes to the back end via Flask and routes and webservers, but that's a whole other beast
        
        That said, that entire line all boils down to "a string goes here that was input by the user"
        
        And since it evaluates to a string, after all the evaluations are done and checked, you can perform operations on to a string
        
        So either on line 17, or on line 43 (now, after all this text pushed it down), you can perform a .lower(), on to a string
        
        """
                
        user_dict = {   # <------- this is user_dict
            "name": username, # Assigning the value username that comes from line 17 to the key "name"
            "score": 0,
            "checkpoint": 1
        }
            
        save_user(user_dict)
            
        return redirect("/?username=" + username)
    
    # Handle the GET request
    else:   # <---------------------------------------------- This is your request.method = "GET" case, which is initial load of index.html, before anyone inputs anything
        return render_template("index.html", username=username)


@app.route('/answer-question', methods=["GET","POST"])
def answer_question():
    
    if request.method == "POST":
        answer = request.form.get("answers") # Correct answer
        return redirect("/answer-question=" + answer) # Next answer
    else:
        answer = request.args.get("answers")
        return render_template("Question-heading")
    print(request.form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
