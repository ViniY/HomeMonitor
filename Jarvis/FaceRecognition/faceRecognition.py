import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

"""This file is only for testing, 
In this program we are building  face detection 
and recognition using opencv
"""

"""
Locally testing the acc
"""


def read_images(path):
    imgs = []
    for f in os.listdir(path):
        if "DS_Store" in f:
            continue
        imgs.append(cv2.imread(os.path.join(path, f)))
    return imgs


def color_grey(imgs):
    imgs_grey = []
    for img in imgs:
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgs_grey.append(grayscale)
    return imgs_grey


def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def detect_faces(f_cascade, colored_img, scaleFactor=1.1):
    img_copy = np.copy(colored_img)
    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);

    # go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img_copy


if __name__ == '__main__':
    path = "faceDetectionDataset"
    # load cascade classifier training file for haarcascade

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    imgs = read_images(path)
    imgs_grey = color_grey(imgs)
    """simply plot the gray scale image"""
    # cv2.imshow("000", imgs_grey[0])
    # cv2.waitKey(0)
    # call our function to detect faces
    test2 = cv2.imread('../../Jarvis/FaceRecognition/faceDetectionDataset/img_500.jpg')
    faces_detected_img = detect_faces(face_cascade, test2)

    # convert image to RGB and show image
    plt.imshow(convertToRGB(faces_detected_img))
    plt.show()



