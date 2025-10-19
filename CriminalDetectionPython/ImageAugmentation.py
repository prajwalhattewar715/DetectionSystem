import imageio
import imgaug as ia
import cv2
import os
import keras

from ConvertToSketch import *
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
  
def augmentation(imgpath1="NA",imgpath2="NA",ext=".jpg"):
    image1 = imageio.v2.imread(imgpath1)
    image=convert_sketch(image1)
    img1=cv2.imread(imgpath1)
    image=convert_sketch(img1)
    UPLOAD_DIR1=os.getcwd()+"\\images\\"
    try:  
        for file in os.listdir(UPLOAD_DIR1):
            try:
                os.remove(UPLOAD_DIR1+file)
            except Exception as e1:
                print("err in delete imgdir")
                print(e1) 
        for file in os.listdir(UPLOAD_DIR1+"/0/"):
            os.remove(UPLOAD_DIR1+"/0/"+file)  
        os.mkdir(UPLOAD_DIR1+"/0/") 
    except Exception as e:
        print("error")
        print(e) 
    cv2.imwrite(UPLOAD_DIR1+"/0/1.jpg",resizeImg(image))
    from imgaug import augmenters as iaa
    ia.seed(4)

    rotate = iaa.Affine(rotate=(-25, 25))
    image_aug = rotate(image=image)

    print("Augmented:")
    cv2.imwrite(imgpath2+"_0"+ext,resizeImg(image_aug))
    #ia.imshow(image_aug)
    print("Original:")
    #ia.imshow(image)
    

    image_path = imgpath1
     
    directory_path = UPLOAD_DIR1
      
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"_1"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        brightness_range=(0., 2.)
    ) 
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"_2"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        width_shift_range=[-40, -20, 0, 20, 40],
        height_shift_range=[-50,50]
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"_3"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=45
    )

    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"_4"+ext,resizeImg(x[0].astype('uint8')))
 
def augmentation1(imgpath1="NA",imgpath2="NA",ext=".jpg"):
    image1 = imageio.v2.imread(imgpath1)
    image=convert_to_sketch2_for_aug(imgpath1)
    img1=cv2.imread(imgpath1)
    UPLOAD_DIR1=os.getcwd()+"\\images\\"
    try:  
        for file in os.listdir(UPLOAD_DIR1):
            try:
                os.remove(UPLOAD_DIR1+file)
            except Exception as e1:
                print(e1) 
                print("err in delete imgdir")
        for file in os.listdir(UPLOAD_DIR1+"/0/"):
            os.remove(UPLOAD_DIR1+"/0/"+file)  
        os.mkdir(UPLOAD_DIR1+"/0/") 
    except Exception as e:
        print("error in aug1")
        print(e) 
    cv2.imwrite(UPLOAD_DIR1+"/0/1"+ext,resizeImg(image))
    image=convert_to_sketch2_for_aug(imgpath1)
    from imgaug import augmenters as iaa
    ia.seed(4)

    rotate = iaa.Affine(rotate=(-25, 25))
    image_aug = rotate(image=image)

    print("Augmented:")
    cv2.imwrite(imgpath2+"sk1_0"+ext,resizeImg(image_aug))
    #ia.imshow(image_aug)
    print("Original:")
    #ia.imshow(image)
    

    image_path = imgpath1
    UPLOAD_DIR1=os.getcwd()+"\\images\\" 
    directory_path = UPLOAD_DIR1
      
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sk1_1"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        brightness_range=(0., 2.)
    ) 
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sk1_2"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        width_shift_range=[-40, -20, 0, 20, 40],
        height_shift_range=[-50,50]
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sk1_3"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=45
    )

    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sk1_4"+ext,resizeImg(x[0].astype('uint8')))
def augmentation2(imgpath1="NA",imgpath2="NA",ext=".jpg"):
    image1 = imageio.v2.imread(imgpath1)
    image=convert_to_sketch2_sharp_for_aug(imgpath1)
    img1=cv2.imread(imgpath1)
    UPLOAD_DIR1=os.getcwd()+"\\images\\"
    try:  
        for file in os.listdir(UPLOAD_DIR1):
            try:
                print("ffffffffffffffff")
                print(file)
                os.remove(UPLOAD_DIR1+file)
            except Exception as e1:
                print(e1) 
        for file in os.listdir(UPLOAD_DIR1+"0/"):
            os.remove(UPLOAD_DIR1+"/0/"+file)   
        #os.mkdir(UPLOAD_DIR1+"0/") 
    except Exception as e:
        print("error in aug2")
        print(e) 
    cv2.imwrite(UPLOAD_DIR1+"/0/1"+ext,resizeImg(image))
    from imgaug import augmenters as iaa
    ia.seed(4)

    rotate = iaa.Affine(rotate=(-25, 25))
    image_aug = rotate(image=image)

    print("Augmented:")
    cv2.imwrite(imgpath2+"sksharp_0"+ext,resizeImg(image_aug))
    #ia.imshow(image_aug)
    print("Original:")
    #ia.imshow(image)
    

    image_path = imgpath1
    UPLOAD_DIR1=os.getcwd()+"\\images\\" 
    directory_path = UPLOAD_DIR1
      
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp_1"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        brightness_range=(0., 2.)
    ) 
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp_2"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        width_shift_range=[-40, -20, 0, 20, 40],
        height_shift_range=[-50,50]
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp_3"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=45
    )

    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp_4"+ext,resizeImg(x[0].astype('uint8')))
def augmentation3(imgpath1="NA",imgpath2="NA",ext=".jpg"):
    image1 = imageio.v2.imread(imgpath1)
    image=convert_to_sketch2_sharp_for_aug(imgpath1,7)
    img1=cv2.imread(imgpath1)
    UPLOAD_DIR1=os.getcwd()+"\\images\\"
    try:  
        for file in os.listdir(UPLOAD_DIR1):
            try:
                os.remove(UPLOAD_DIR1 +file)
            except Exception as e1:
                print(e1) 
        for file in os.listdir(UPLOAD_DIR1+"/0/"):
            os.remove(UPLOAD_DIR1+"/0/"+file)   
        os.mkdir(UPLOAD_DIR1+"/0/") 
    except Exception as e:
        print("error in aug3")
        print(e) 
    cv2.imwrite(UPLOAD_DIR1+"/0/1"+ext,(image))
    from imgaug import augmenters as iaa
    ia.seed(4)

    rotate = iaa.Affine(rotate=(-25, 25))
    image_aug = rotate(image=image)

    print("Augmented:")
    cv2.imwrite(imgpath2+"sksharp7_0"+ext,resizeImg(image_aug))
    #ia.imshow(image_aug)
    print("Original:")
    #ia.imshow(image)
    

    image_path = imgpath1
    UPLOAD_DIR1=os.getcwd()+"\\images\\" 
    directory_path = UPLOAD_DIR1
      
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp7_1"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        brightness_range=(0., 2.)
    ) 
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp7_2"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        width_shift_range=[-40, -20, 0, 20, 40],
        height_shift_range=[-50,50]
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp7_3"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=45
    )

    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp_4"+ext,resizeImg(x[0].astype('uint8')))
def augmentation4(imgpath1="NA",imgpath2="NA",ext=".jpg"):
    image1 = imageio.v2.imread(imgpath1)
    image=convert_to_sketch2_sharp_for_aug(imgpath1,8)
    img1=cv2.imread(imgpath1)
    UPLOAD_DIR1=os.getcwd()+"\\images\\"
    try:  
        for file in os.listdir(UPLOAD_DIR1):
            try:
                os.remove(UPLOAD_DIR1+file)
            except Exception as e1:
                print(e1) 
        for file in os.listdir(UPLOAD_DIR1+"0/"):
            os.remove(UPLOAD_DIR1+"/0/"+file)   
        os.mkdir(UPLOAD_DIR1+"/0/") 
    except Exception as e:
        print("error in aug2")
        print(e) 
    cv2.imwrite(UPLOAD_DIR1+"/0/1"+ext,(image))
    from imgaug import augmenters as iaa
    ia.seed(4)

    rotate = iaa.Affine(rotate=(-25, 25))
    image_aug = rotate(image=image)

    print("Augmented:")
    cv2.imwrite(imgpath2+"sksharp8_0"+ext,resizeImg(image_aug))
    #ia.imshow(image_aug)
    print("Original:")
    #ia.imshow(image)
    

    image_path = imgpath1
    UPLOAD_DIR1=os.getcwd()+"\\images\\" 
    directory_path = UPLOAD_DIR1
      
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp8_1"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        brightness_range=(0., 2.)
    ) 
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
     
    cv2.imwrite(imgpath2+"sksharp8_2"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        width_shift_range=[-40, -20, 0, 20, 40],
        height_shift_range=[-50,50]
    )
    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp8_3"+ext,resizeImg(x[0].astype('uint8')))
    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=45
    )

    x, y = next(generator.flow_from_directory(directory_path, batch_size=1))
    
    cv2.imwrite(imgpath2+"sksharp8_4"+ext,resizeImg(x[0].astype('uint8')))
def resizeImg(img):
    width = 200
    height = 200
    dim = (width, height) 
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized