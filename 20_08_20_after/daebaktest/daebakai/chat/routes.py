from flask import render_template, request,session
from . import chat
from daebakai.chat.database import Database
@chat.route('/', methods=['GET','POST'])
def Main():
    my_name = session['name']
    a = request.path
    print(a[:-1], type(a[:-1]))
    return render_template('chat-main.html', my_name=my_name)
