# home 
from flask import Flask , render_template, url_for, request, redirect, Blueprint,session, g
hm = Blueprint('hm', __name__, url_prefix='/')


@hm.route('/')
@hm.route('/index')
def index():
    return render_template('home.html')

