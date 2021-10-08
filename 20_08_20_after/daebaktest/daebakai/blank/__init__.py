# blank
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash


blank = Blueprint('blank', __name__,url_prefix='/blank')
 

@blank.route("/")

def Main():
    
   
    return render_template('blank-main.html')
    
    
 
