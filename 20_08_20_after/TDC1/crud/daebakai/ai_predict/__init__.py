# ai_predict 
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from daebakai import bcrypt
from daebakai import db 




ai_predict = Blueprint('ai_predict', __name__,url_prefix='/ai_predict')
 
@ai_predict.route("/")
def Main():
    
    return render_template('ai-predict.html' )

