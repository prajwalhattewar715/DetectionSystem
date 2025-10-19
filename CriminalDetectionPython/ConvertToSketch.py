import cv2 
import numpy as np
import os
import glob
from sketchify import sketch
def convert(imgpath="NA",sketchpath="NA",sketchpath2="NA"): 
     
    img = cv2.imread(imgpath)
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
    width =200
    height = 200
    dim = (width, height)
    
    # resize image
    #resized = cv2.resize(thresh2, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.resize(pencil_sketch_image, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(sketchpath,resized)
    #cv2.imwrite(sketchpath2,resized)
def convert_sketch(img):    
     
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
    iimg=255 -pencil_sketch_image
    pencil_sketch_image=sharpenImg( iimg)
    width =200
    height = 200
    dim = (width, height)
    
    # resize image
    #resized = cv2.resize(thresh2, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.resize(pencil_sketch_image, dim, interpolation = cv2.INTER_AREA)
    return resized
def dodge(front: np.ndarray, back: np.ndarray) -> np.ndarray:
    """The formula comes from https://en.wikipedia.org/wiki/Blend_modes
    Args:
        front: (np.ndarray) - front image to be applied to dodge algorithm
        back: (np.ndarray) - back image to be applied to dodge algorithm

    Returns:
        image: (np.ndarray) - dodged image
    """
    result = back*255.0 / (255.0-front) 
    result[result>255] = 255
    result[back==255] = 255
    return result.astype('uint8')
def sharpenImg(inverted):    
    sharpen_value=6
    kernel=np.array([[0, -1, 0], [-1, sharpen_value,-1], [0, -1, 0]])
    finalimg=255 - cv2.filter2D(src=inverted, ddepth=-1, kernel=kernel)
    return finalimg
def sharpenImg1(inverted,sharpen_value=6):     
    kernel=np.array([[0, -1, 0], [-1, sharpen_value,-1], [0, -1, 0]])
    finalimg=255 - cv2.filter2D(src=inverted, ddepth=-1, kernel=kernel)
    return finalimg
def convert_to_sketch2(imgpath1="NA",imgpath="NA",ext=".jpg",imgpath2="NA"):
    frame = cv2.imread(imgpath1)
    #cv2.imshow('image', frame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    grayscale = np.array(np.dot(frame[..., :3], [0.299, 0.587, 0.114]), dtype=np.uint8)
    grayscale = np.stack((grayscale,) * 3, axis=-1)
    inverted_img = 255 - grayscale
    blur_img = cv2.GaussianBlur(inverted_img, ksize=(0, 0), sigmaX=5)
    final_img = dodge(blur_img, grayscale)
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(final_img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(imgpath+"_1"+ext,resized)
    #cv2.imwrite(imgpath2+"_1"+ext,resized)
    inverted = 255 - final_img
    finalimg=sharpenImg(inverted)
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(finalimg, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(imgpath+"_2"+ext,resized)
    #cv2.imwrite(imgpath2+"_2"+ext,resized)
    finalimg=sharpenImg1(inverted,7)
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(finalimg, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(imgpath+"_3"+ext,resized)
    #cv2.imwrite(imgpath2+"_3"+ext,resized)
    finalimg=sharpenImg1(inverted,10)
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(finalimg, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(imgpath+"_10"+ext,resized)
    cv2.imwrite(imgpath2+"_10"+ext,resized)

def convert_to_sketch2_for_aug(imgpath1="NA"):
    frame = cv2.imread(imgpath1)
    #cv2.imshow('image', frame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    grayscale = np.array(np.dot(frame[..., :3], [0.299, 0.587, 0.114]), dtype=np.uint8)
    grayscale = np.stack((grayscale,) * 3, axis=-1)
    inverted_img = 255 - grayscale
    blur_img = cv2.GaussianBlur(inverted_img, ksize=(0, 0), sigmaX=5)
    final_img = dodge(blur_img, grayscale)
    return final_img
def convert_to_sketch2_sharp_for_aug(imgpath1="NA",level=6):
    frame = cv2.imread(imgpath1)
    #cv2.imshow('image', frame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    grayscale = np.array(np.dot(frame[..., :3], [0.299, 0.587, 0.114]), dtype=np.uint8)
    grayscale = np.stack((grayscale,) * 3, axis=-1)
    inverted_img = 255 - grayscale
    blur_img = cv2.GaussianBlur(inverted_img, ksize=(0, 0), sigmaX=5)
    final_img = dodge(blur_img, grayscale)
    inverted = 255 - final_img
    finalimg=sharpenImg1(inverted,level)
    return finalimg
def convert_to_sketchify(imgpath1,imgpath2,imgname):
    img = sketch.normalsketch(imgpath1, imgpath2, imgname,scale=10)
    img=cv2.imread(imgpath2+imgname+".png")
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(imgpath2+imgname+".jpg",resized)
    os.remove(imgpath2+imgname+".png")