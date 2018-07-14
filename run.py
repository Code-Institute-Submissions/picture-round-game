import os 
from flask import Flask, render_template 
#import picture_test2

app = Flask (__name__)

@app.route('/')
def hello():
    #question = picture_test2.get_question(0)
    
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)