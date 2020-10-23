import cv2
import numpy as np
import imutils
import tensorflow as tf
import random


vid = cv2.VideoCapture(0)

display_text = 'Press P to Play'

model = tf.keras.models.load_model('mymodel_3.h5')

def predict(roi):
    model_roi = np.reshape(roi, [1, 200, 200, 3])
    prediction = model.predict(model_roi)
    prediction = prediction[0]
    if prediction[0]> prediction[1] and prediction[0] > prediction[2]:
        return 'paper'
    elif prediction[1]>prediction[0] and prediction[1] > prediction[2]:
        return 'rock'
    else:
        return "scissor"

def counting_text(game_mode, display_text, frames):
    if game_mode == 'c':
        if frames <=20:
            display_text = 'ROCK'
        elif frames > 20 and frames <= 40:
            display_text = 'PAPER'
        elif frames > 40 and frames <= 60:
            display_text = "SCISSORS"
        elif frames <110:
            display_text = "SHOOT"
    return display_text

def predict_who_won(ai, user):
    if ai =='rock':
        if user == 'rock':
            return 'TIE'
        elif user == 'scissor':
            return 'AI WINS'
        else:
            return 'USER WINS'
    elif ai =='paper':
        if user == 'paper':
            return 'TIE'
        elif user == 'rock':
            return 'AI WINS'
        else:
            return 'USER WINS'
    elif ai =='scissor':
        if user == 'scissor':
            return 'TIE'
        elif user == 'paper':
            return 'AI WINS'
        else:
            return 'USER WINS'

def ai_move():
    int_move = random.randint(1, 3)
    if int_move == 1:
        return "rock"
    elif int_move == 2:
        return "paper"
    elif int_move == 3:
        return "scissor"

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeft_X           = 225
bottomLeft_Y           = 125
fontScale              = 1
fontColor              = (128,0,0)
lineType               = 2


frames = 0
game_mode = 'p'
result = False
ai_input = ''
victory_status = ''
while(True):
    ret, frame = vid.read()
    rec_frame = cv2.rectangle(frame, (99,199), (300, 400), (255, 0, 0), 1 )
    roi = frame[200:400, 100:300]
    roi = cv2.resize(roi, (200, 200))
    rec_frame = cv2.putText(rec_frame,display_text, (bottomLeft_X, bottomLeft_Y), font, fontScale, fontColor, lineType)
    if result == True:
        rec_frame = cv2.putText(rec_frame,"AI put " + ai_input , (bottomLeft_X, bottomLeft_Y + 25), font, fontScale, fontColor, lineType)
        rec_frame = cv2.putText(rec_frame,victory_status , (bottomLeft_X, bottomLeft_Y + 52), font, fontScale, fontColor, lineType)

    cv2.imshow('webcam', rec_frame)
    cv2.imshow('roi', roi)
    frames += 1
    key = cv2.waitKey(20)
    if key == ord('q'):
        break
    if key == ord('p'):
        game_mode = 'c'
        frames = 0
    display_text = counting_text(game_mode, display_text, frames)
    if game_mode == 'c':
        if frames == 110:
            user_input = predict(roi)
            ai_input = ai_move()
            result = True
            victory_status = predict_who_won(ai_input, user_input)
        elif frames >111 and frames <=220:
            display_text = 'You Put: ' + user_input 

        elif frames > 220:
            display_text = "Press P to Play Again"
            frames = 0
            result = False
            game_mode = 'p'
        