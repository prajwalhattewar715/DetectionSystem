#!C:\Users\Megha Home\AppData\Local\Programs\Python\Python310\python
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
#from keras.optimizers import Adam, SGD
#from keras.optimizers import SGD
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
import itertools
import random
import warnings
import numpy as np
import cv2
import os
import cgi
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint, EarlyStopping
from FunFactory import *
#from matplotlib import pyplot as plt
def getDictionary11():
    print("Content-type: text/html")
    print()
    form=cgi.FieldStorage()
    warnings.simplefilter(action='ignore', category=FutureWarning)

    UPLOAD_DIR=os.getcwd()+"\\DataSet\\"
    UPLOAD_DIR_Model=os.getcwd()+"\\model\\"
    train_path=os.getcwd()+"\\DataSet\\"
    test_path=os.getcwd()+"\\test\\"
    #train_path = r'\\train\\'
    #test_path = r'E:\\gesture\\test\\'
    lblcnt=8
    try:
        lblcnt=int(getLabelCount())
    except Exception as e:
        print("error lbl")
        print(e)
    print("lblcnt")
    print(str(lblcnt))
    train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=train_path, target_size=(200,200), class_mode='categorical', batch_size=lblcnt,shuffle=True)
     
    label_map = (train_batches.class_indices)
    c=0
    mydict={}
    for label in label_map:
        mydict[c]=label
        print(label)
        c=c+1
    print(label_map)
    print("dict")
    print(mydict)
    return(mydict)
#getDictionary11()