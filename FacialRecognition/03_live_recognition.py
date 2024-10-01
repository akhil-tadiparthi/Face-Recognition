import cv2
import numpy as np
import csv
import os 
from configFile import *

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(modelPath)
cascadePath = cascadePath
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# Create a space in the script earlier to add to this list. Might need to combine steps into one script
# where this array can be accessed 
names = read_list_from_csv(csvPath)

# Start live video capture
cam = cv2.VideoCapture(0)
# Width
cam.set(3, 640)
# Height
cam.set(4, 480)

# Define window size in live stream
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Confidence
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('Facial Recognition',img) 

    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

print("\n Exited Facial Recognition Program")
cam.release()
cv2.destroyAllWindows()
