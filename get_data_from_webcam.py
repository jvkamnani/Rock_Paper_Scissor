import cv2
import numpy as np
import imutils
import os

MAIN_URL = cwd = os.getcwd() + '/pictures from webcam/'
ROCK_URL = MAIN_URL + 'rock/'
SCISSOR_URL = MAIN_URL + 'scissor/'
PAPER_URL = MAIN_URL + 'paper/'

rock_count = 0
scissor_count = 0
paper_count = 0


vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    rec_frame = cv2.rectangle(frame, (99,199), (300, 400), (255, 0, 0), 1 )
    roi = frame[200:400, 100:300]
    roi = cv2.resize(roi, (200, 200))

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottom_left_x = 100
    bottom_left_y = 125 
    fontScale = 0.7
    fontColor = (255,255,255)
    lineType = 2

    rec_frame = cv2.putText(rec_frame,'Press R to save roi into rock', (bottom_left_x, bottom_left_y), font, fontScale, fontColor, lineType)
    rec_frame = cv2.putText(rec_frame, 'Press S to save roi into scissor', (bottom_left_x, bottom_left_y + 25) , font, fontScale, fontColor, lineType)
    rec_frame = cv2.putText(rec_frame,'Press P to save roi into paper', (bottom_left_x, bottom_left_y + 50), font, fontScale, fontColor, lineType)
    
    cv2.imshow('webcam', rec_frame)
    cv2.imshow('roi', roi)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite(SCISSOR_URL + 'scissor_' + str(scissor_count) + '.jpg' , roi)
        scissor_count += 1
    elif key == ord('p'):
        cv2.imwrite(PAPER_URL + 'paper_' + str(paper_count) + '.jpg' , roi)
        paper_count += 1
    elif key == ord('r'):
        cv2.imwrite(ROCK_URL + 'rock_' + str(rock_count) + '.jpg' , roi)
        rock_count += 1
