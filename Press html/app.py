import os

from flask import Flask, render_template, redirect, request, url_for


#connect to IMAGE_UPLOADS
app = Flask(__name__)


#set app variables





#home page


@app.route('/')
def home():
    return render_template("index.html")
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            port=int(os.environ.get('3000')),
            debug=False)