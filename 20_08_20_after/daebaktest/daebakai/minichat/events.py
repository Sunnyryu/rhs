from flask import session
from flask_socketio import emit, join_room, leave_room,send
from .. import socketio
from datetime import datetime
from daebakai.chat.database import chat_Database, bot_Database
import re
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords


@socketio.on('minijoined', namespace='/')
def joined(json):
    print('테스트테스트')
    c_number = session['id']
    c_name = session['name']
    room = c_name+'_'+str(c_number)
    join_room(room)
    a = bot_Database.select_basic_bot()
    r_message = a[0]['content']

    robot_dict ={}
    robot_dict['name']= 'daebakbot'
    robot_dict['message'] = r_message
    robot_dict['a_number'] = 'answer1'
    robot_dict['korean_message'] = a[0]['korean_content']
    robot_dict['korean_diction'] = a[0]['korean_diction']
    k = 'history'
    emit('mini hello daebakbot', robot_dict, room = room)

#@socketio.on('recommend', namespace='/chat')
#def recommend(message, methods=['GET', 'POST']):
#    c_number = session['id']
#    c_name = session['name']
#    room = c_name+'_'+str(c_number)
#    join_room(room)
#    r_message = 'my recommend is bts`s photobook. so i offer link. plz click to link'
#    robot_dict ={}
#    robot_dict['name']= 'daebakbot'
#    robot_dict['message'] = r_message
#    robot_dict['link'] = 'https://daebak.co/collections/bts/products/bts-the-fact-photobook-special-edition-we-remember'
#    emit('recommend2', robot_dict, room=room)


@socketio.on('minicustomer', namespace='/')
def customer_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json) + "시작")
    if json['message']!='':
        c_number = session['id']
        c_name = json['user_name']
        c_message = json['message']
        if "'" in c_message:
            c_message = c_message.replace("'", "''")
        print(c_message,"call")
        c_time = datetime.now().strftime('%-I:%M %p')
        c_YMH = datetime.now().strftime('%A %B %-d %Y %-I%p ')
        room = c_name+'_'+str(c_number)
        table_name = 'daebak_chat'
        c_table_check = chat_Database.show_table(table_name)
        if c_table_check == 1:
            c_table_insert = chat_Database.insert_message(c_number, c_name, c_message, c_time, c_YMH, table_name)
        elif c_table_check == 0:
            c_table_create = chat_Database.create_table(table_name)
            c_table_insert = chat_Database.insert_message(c_number, c_name, c_message, c_time, c_YMH, table_name)
        print(json,"akak")
        emit('mini customer send', json, room=room)
    else:
        print('messeage is bin')



@socketio.on('mini robot event', namespace='/')
def robot_event(json, methods=['GET', 'POST']):
    c_number = session['id']
    c_name = json['user_name']
    c_message = json['message']
    a_number = json['a_number']
    r_name = 'daebakbot'
    test_list = []
    print(a_number)
    room = c_name+'_'+str(c_number)
    test_db = bot_Database.test()
    for i in test_db:
        for k in i['base_keyword'].split(','):
            test_list.append(k.lower().strip())
    test_list2 = sorted(test_list)

    #print(test_list)
    table_name = 'daebak_bot'
    test_tokenize= TreebankWordTokenizer()
    test_message = test_tokenize.tokenize(c_message)
    print(test_message,"테스트")
    stop_word = stopwords.words('english')
    print(stop_word)
    stop_word.extend(['\'ve','\'re','\'m','\'s','n\'t'])
    stop_word_list = []
    for s_word in test_message:
        if s_word not in stop_word and re.sub(r"[^a-zA-Z0-9]","",s_word):
            s_word = re.sub(r"[^a-zA-Z0-9]","",s_word)
            if s_word in stop_word_list:
                pass
            else:
                stop_word_list.append(s_word)
    stop_word_list = sorted(stop_word_list)

    test_1 = [x for x in stop_word_list if x in test_list2]
    print(test_1,"0000")
    print(stop_word_list,"9292")
    print(len(stop_word_list),"길이")
    if len(test_1) > 1:
        stop_word_str = ", ".join(test_1)
        bot_content = bot_Database.select_content(stop_word_str)
    elif len(test_1) == 1:
        stop_word_str = "".join(test_1)
        bot_content = bot_Database.select_content(stop_word_str)
    else:
        robot_dict = {}
        robot_dict['name']= r_name
        r_message = "i don't know"
        robot_dict['message'] = r_message
        robot_dict['korean_message'] = "나는 잘몰라요."
        robot_dict['korean_diction'] = "naneun jalmollayo."
        print("ex1")
        emit('mini robot resend', robot_dict, room=room)
    try:
        if bot_content:
            robot_dict = {}
            robot_dict['name']= r_name
            robot_dict['message'] = bot_content[0]['content']
            robot_dict['link'] = bot_content[0]['link']
            robot_dict['image'] = bot_content[0]['img']
            robot_dict['korean_message'] = bot_content[0]['korean_content']
            robot_dict['korean_diction'] = bot_content[0]['korean_diction']
            emit('mini robot resend', robot_dict, room=room)
        else:
            print("길이가 1보다 작음")
            robot_dict = {}
            robot_dict['name']= r_name
            r_message = "i don't know"
            robot_dict['message'] = r_message
            robot_dict['korean_message'] = "나는 잘몰라요."
            robot_dict['korean_diction'] = "naneun jalmollayo."
            print("ex2")
            emit('mini robot resend', robot_dict, room=room)
    except:
        print("not word")


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
