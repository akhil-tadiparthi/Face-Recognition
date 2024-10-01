import cv2
import csv
import os
from configFile import *
from PIL import Image
from gaussian_transformation import *
from random_erasing import *
from rotate import *
from adjust_contrast import *

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

cascade_classifier = cv2.CascadeClassifier(cascadePath)

face_num = input('\n Enter a User ID (1-100) then press return:   ')
number_int = int(face_num)
face_name = input('\n Enter the User\'s name then press return:   ')
print("\n 1 - Rotate")
print("\n 2 - Adjust Contrast")
print("\n 3 - Random Erasing")
print("\n 4 - Gaussian Transformation")
augmentation_technique = input('\n Enter the augmentation techniqe to use :   ')

name_list = read_list_from_csv(csvPath)
name_list.insert(number_int, face_name)
write_list_to_csv(csvPath, name_list)

print("\n Taking Pictures of you...")

count = 0

while(True):

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    images = cascade_classifier.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in images:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        mypath = imageDatabase + "/" + face_name
        if not os.path.isdir(mypath):
            os.makedirs(mypath)

        cv2.imwrite(mypath + '/' + str(face_num) + "." + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('Image Capture', img)

        pil_image = Image.fromarray(gray[y:y+h,x:x+w])
        
        augmentation_count = 30

        if augmentation_technique == '1': # Rotate
            for i in range(augmentation_count):
                # Apply image augmentation
                augmented_image = rotate_face_image(pil_image, 10)

                # Convert the augmented image back to numpy array
                augmented_image_array = np.array(augmented_image)

                # Save the augmented image
                cv2.imwrite(mypath + '/' + str(face_num) + "." + str(count) + "_rotated.jpg", augmented_image_array)

        if augmentation_technique == '2': # Adjust Contrast
            for i in range(augmentation_count):
                # Apply image augmentation
                augmented_image = adjust_brightness_contrast(pil_image, 3, 2)

                # Convert the augmented image back to numpy array
                augmented_image_array = np.array(augmented_image)

                # Save the augmented image
                cv2.imwrite(mypath + '/' + str(face_num) + "." + str(count) + "_contrasted.jpg", augmented_image_array)

        if augmentation_technique == '3': # Random Erasing
            for i in range(augmentation_count):
                # Apply image augmentation
                augmented_image = apply_random_erasing(pil_image)

                # Convert the augmented image back to numpy array
                augmented_image_array = np.array(augmented_image)

                # Save the augmented image
                cv2.imwrite(mypath + '/' + str(face_num) + "." + str(count) + "_erased.jpg", augmented_image_array)

        if augmentation_technique == '4': #Gaussian
            for i in range(augmentation_count):
                # Apply image augmentation
                augmented_image = gaussian_transformation(pil_image, alpha=50, sigma=5)

                # Convert the augmented image back to numpy array
                augmented_image_array = np.array(augmented_image)

                # Save the augmented image
                cv2.imwrite(mypath + '/' + str(face_num) + "." + str(count) + "_gaussian.jpg", augmented_image_array)

    k = cv2.waitKey(100) & 0xff
    if k == 27: # ASCII for escape
        break
    elif count >= 30: # Take 30 face images
         break

print("\n Images taken")
cam.release()
cv2.destroyAllWindows()


