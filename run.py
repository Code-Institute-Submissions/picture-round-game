import os 
from flask import Flask, render_template, request, redirect
#import picture_test2

app = Flask (__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    
    if request.method == "POST":
        username = request.form.get('username', None)
        return redirect("/?username=" + username)
    else:
        username = request.args.get('username', None)
        
    return render_template("index.html", username=username)
    
@app.route('/answer-question', methods=["POST"])
def answer_question():
    
    if request.method == "POST":
        username = request.form.get('username', None)
        
        pass
        # add logic to check answer and update score
        
    return render_template("index.html", username=username)   
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)