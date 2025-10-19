#!C:\Users\Megha Home\AppData\Local\Programs\Python\Python310\python
# Import modules for CGI handling
import cgi, cgitb, jinja2 
import numpy as np
import cv2
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from FunFactory import *
from trainCNN1 import *
import os 

def criminal_Prediction(filenm="NA"):
    UPLOAD_DIR_Model=os.getcwd()+"\\model\\best_model_dataflair3.h5"
    model = keras.models.load_model(UPLOAD_DIR_Model)
    word_dict=getDictionary11()
    background = None
    accumulated_weight = 0.5

    ROI_top = 100
    ROI_bottom = 300
    ROI_right = 150
    ROI_left = 350
 
     

    UPLOAD_DIR=os.getcwd()+"\\InputImg\\temp\\"  
    test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=UPLOAD_DIR, target_size=(200,200), class_mode='categorical', batch_size=1, shuffle=True)
    imgs, labels = next(test_batches)
    predictions = model.predict(imgs, verbose=0)
    print(predictions)
    #print(word_dict[np.argmax(predictions)])
    print(predictions[0][np.argmax(predictions)])
    print("prediction === "+word_dict[np.argmax(predictions)])
    cv2.destroyAllWindows()
    
    if predictions[0][np.argmax(predictions)]<1.0:
        return "-1"
    else:
        #return word_dict[np.argmax(predictions)]
        return word_dict[np.argmax(predictions)]

     
