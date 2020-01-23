import os

from flask import Flask, render_template, redirect, request, url_for


#connect to IMAGE_UPLOADS
app = Flask(__name__)


#set app variables





#home page


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")
    
    
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(8000),
            debug=True)