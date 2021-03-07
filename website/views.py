from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
    
@views.route('/about.txt')
def about():
    return render_template("about.html")
    
@views.route('/write')
def write():
    return render_template("write.html")
    
@views.route('/updates')
def blog():
    return render_template("updates.html")
