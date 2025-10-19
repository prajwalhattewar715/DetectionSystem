import cv2
import numpy as np

frame = cv2.imread("images/22.jpg")
cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
grayscale = np.array(np.dot(frame[..., :3], [0.299, 0.587, 0.114]), dtype=np.uint8)
grayscale = np.stack((grayscale,) * 3, axis=-1)
inverted_img = 255 - grayscale
blur_img = cv2.GaussianBlur(inverted_img, ksize=(0, 0), sigmaX=5)

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

final_img = dodge(blur_img, grayscale)
inverted = 255 - final_img
cv2.imshow('image', final_img)
cv2.waitKey(0)

sharpen_value=6
kernel=np.array([[0, -1, 0], [-1, sharpen_value,-1], [0, -1, 0]])
finalimg=255 - cv2.filter2D(src=inverted, ddepth=-1, kernel=kernel)
cv2.imshow('image', finalimg)
cv2.waitKey(0)