import os

from flask import Flask, render_template, redirect, request, url_for
#connect to IMAGE_UPLOADS
app = Flask(__name__)


#set app variables

PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')

#home page

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/designs')
def designs():
    return render_template("designs.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/contact')
def contact():
    
       return render_template("contact.html")


@app.route('/inclusions')
def inclusions():
    return render_template("inclusions.html")
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
