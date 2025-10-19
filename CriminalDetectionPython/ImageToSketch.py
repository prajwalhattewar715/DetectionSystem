#import the library
import cv2
import json, requests, urllib, io
import os
import os
from sketchify import sketch
import pyttsx3
from PencilSketch import *
user='criminaldetection'
pao='SProject23'

github_session = requests.Session()
github_session.auth = (user, pao)
#get the image location and the image file name

img_location = 'https://raw.githubusercontent.com/criminaldetection/criminalphotos/main/A00147.jpg'
img_location ='https://github.com/criminaldetection/criminalphotos/raw/A00147.jpg'
#img_location = 'A00147.jpg'
#filename = 'A00147.jpg'
from github import Github
g = Github('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')
repository = g.get_user().get_repo('criminal_repo')
i=0
for file in repository.get_contents("photos"):
        print(file.name)
        i=i+1  
        contents = file
        decoded = contents.decoded_content
        with open('1.jpg', 'wb') as f:
            f.write(decoded)
            #read in the image
        img = cv2.imread('1.jpg')
            #convert the image to gray scale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #invert the image
        inverted_gray_image = 255 - gray_image
            #blur the image by gaussian blur
        blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
            #invert the blurred image
        inverted_blurred_image = 255 - blurred_image
            #create the pencil sketch image
        pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)
            #show the image
        img = sketch.normalsketch('1.jpg', os.getcwd(), '221',scale=10)
          
        img = cv2.imread('221.png') 
        cv2.imshow('Original Image', img) 
        cv2.imshow('New Image', pencil_sketch_image)
        
        cv2.waitKey(0)
        if(i==1):
            break



for repo in g.get_user().get_repos():
    print(repo.name)
    