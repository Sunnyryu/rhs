from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from flask import session
minichat = Blueprint('minichat', __name__)

@minichat.route('/', methods=['GET','POST'])
def Main():
    return render_template('minichat.html')

from . import events
