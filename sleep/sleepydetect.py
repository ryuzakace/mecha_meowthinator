from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2



def eyear(eye):
    a=dist.euclidean(eye[1],eye[5])
    b=dist.euclidean(eye[2],eye[4])
    c=dist.euclidean(eye[0],eye[3])
    e=(a+b)/(2.0*c)
    return e

def alarm():
    playsound.playsound("/home/anindya/TEST/sleep/alarm.wav")


EYE_AR_THRESH=0.3
EYE_AR_CONSEC_FRAMES=48
COUNTER=0
ALARM_ON=False
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("/home/anindya/TEST/sleep/face.dat")
(lStart,lEnd)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart,rEnd)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vs=VideoStream(0).start()
time.sleep(1)

while 1:
    frame=vs.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects=detector(gray,0)
    for rect in rects:
        shape=predictor(gray,rect)
        shape=face_utils.shape_to_np(shape)
        leftEye=shape[lStart:lEnd]
        rightEye=shape[rStart:rEnd]
        leftEAR=eyear(leftEye)
        rightEAR=eyear(rightEye)
        ear=(leftEAR+rightEAR)/2.0

        leftEyeHull=cv2.convexHull(leftEye)
        rightEyeHull=cv2.convexHull(rightEye)
        cv2.drawContours(frame,[leftEyeHull],-1,(0,255,0),1)
        cv2.drawContours(frame,[rightEyeHull],-1,(0,255,0),1)
        if ear < EYE_AR_THRESH:
            COUNTER+=1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True
                    t = Thread(target=alarm)
                    t.deamon = True
                    t.start()
                cv2.putText(frame,"ALERT!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        else:
            COUNTER = 0
            ALARM_ON = False
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
vs.stop()
