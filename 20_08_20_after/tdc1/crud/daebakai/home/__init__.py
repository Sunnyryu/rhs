# home 
from flask import Flask , render_template, url_for, request, redirect, Blueprint,session, g

home = Blueprint('home', __name__)

@home.route("/")
def Home():
    
    return render_template('home.html')
