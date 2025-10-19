import imageio
import imgaug as ia
import cv2 
import keras
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
def convertImageToSketch(img):
    #convert the image to gray scale
    gray_image = cv2.cvtColor(x[0], cv2.COLOR_BGR2GRAY)
                #invert the image
    inverted_gray_image = 255 - gray_image
                #blur the image by gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
                #invert the blurred image
    inverted_blurred_image = 255 - blurred_image
                #create the pencil sketch image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)
                #show the image
    cv2.imshow('Original Image', img)
    cv2.imshow('New Image', pencil_sketch_image)
    cv2.waitKey(0)
from matplotlib import pyplot as plt
image = imageio.v2.imread("1.jpg")
img=cv2.imread("1.jpg")
from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate=(-25, 25))
image_aug = rotate(image=image)

print("Augmented:")
cv2.imwrite("12.jpg",image_aug)
#ia.imshow(image_aug)
print("Original:")
#ia.imshow(image)
 

image_path = '1.jpg'
directory_path = "images"
plt.imshow(plt.imread(image_path))
plt.show()
generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=40
)
x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
plt.imshow(x[0].astype('uint8'))
generator = tf.keras.preprocessing.image.ImageDataGenerator(
    brightness_range=(0., 2.)
)
plt.show()
x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
plt.imshow(x[0].astype('uint8'))
plt.show()

generator = tf.keras.preprocessing.image.ImageDataGenerator(
    width_shift_range=[-40, -20, 0, 20, 40],
    height_shift_range=[-50,50]
)
x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
plt.imshow(x[0].astype('uint8'))
plt.show()
generator = tf.keras.preprocessing.image.ImageDataGenerator(
    shear_range=45
)

x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
plt.imshow(x[0].astype('uint8'))
plt.show()
convertImageToSketch(x[0])
