import cv2
import numpy as np
from PIL import Image
import os
from configFile import *

# Path for image database
path = imageDatabase

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cascadePath)

def getUser(path):
    folderPaths = []
    for i in os.listdir(path):
        if ".DS_Store" not in i: folderPaths.append(os.path.join(path, i)) 
    return folderPaths


# Get Images and Label the Data
def getImages():
    folderPaths = getUser(path)

    imagePaths = []
    for i in folderPaths:
        for j in os.listdir(i):
            imagePaths.append(os.path.join(i, j))
    
    face_sample=[]
    num = []

    for imagePath in imagePaths:

        if ".DS_Store" in imagePath:
            continue

        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[0])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            face_sample.append(img_numpy[y:y+h,x:x+w])
            num.append(id)

    return face_sample, num


print ("\n Training on faces...")
faces, nums = getImages()
recognizer.train(faces, np.array(nums))

# Save the model
recognizer.save(modelPath)

print("\n {0} faces trained.".format(len(np.unique(nums))))
