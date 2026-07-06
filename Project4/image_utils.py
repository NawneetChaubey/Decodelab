#=======Image Utillities===============
import cv2
import numpy as np
from PIL import Image


#Convert PIL Images to Open CV 
def pil_to_cv(image):
    image = np.array(image)
    image = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )
    return image


# convert OpenCV to PIL
def cv_to_pil(image):
    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )
    return Image.fromarray(image)

# configuring the gray scale
def grayscale(image):
    img = pil_to_cv(image)
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )
    return gray

# configuring the Gaussian Blur
def blur(image):
    gray = grayscale(image)
    return cv2.GaussianBlur(
        gray,(5,5),0
    )
    
# configuring the threshold
def threshold(image):
    blur_img = blur(image)
    thresh = cv2.threshold(
        blur_img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    return thresh

# Resize the Image
def resize(image,width=800):
    img = pil_to_cv(image)
    h,w = img.shape[:2]
    ratio = width/w
    new_height = int(h*ratio)
    resized = cv2.resize(img,(width,new_height))
    return cv_to_pil(resized)