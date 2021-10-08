# ai_predict 
# -*- coding: utf-8 -*-
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash,json
from flask import send_file

from werkzeug.utils import secure_filename
from daebakai import bcrypt
from daebakai import db 
import cv2
import os
import numpy as np


  
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
ai_predict = Blueprint('ai_predict', __name__,url_prefix='/ai_predict')
 
@ai_predict.route("/", methods=["GET","POST"])
def Main():

    maxclassname = request.args.get('maxclassname')
    maxprobability = request.args.get('maxprobability')
    # print(maxclassname, maxprobability)
# data = request.form['senddata']
    

    return render_template('ai-predict.html' )

@ai_predict.route("/image", methods=["POST"])
def Image():
    if request.method == 'POST':
        file = request.files['file']
        npimg = np.fromfile(file, np.uint8)
        file = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        filename = os.getcwd()+'\\test.jpg'
        file = cv2.imwrite(filename, file)

        face_cascade = cv2.CascadeClassifier('face_detector.xml')
        # Read the input image
        img = cv2.imread(filename)
        
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        
        # # Draw rectangle around the faces

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # # # Display the output
        
        cv2.imwrite("daebakai//face_detected.png", img) 

        image = send_file('face_detected.png', mimetype='image/png')
        


    return image


@ai_predict.route("/facedetection")
def face():
    return render_template("ai-face.html")

