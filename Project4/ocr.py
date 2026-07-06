# ===========AI image Text Recognition system=======================

# important python library
import pytesseract
from PIL import Image
import cv2
import numpy as np 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image Preprocessing
def preprocess_image(image):
    
    # converting PIL Images to numpy array
    img = np.array(image)
    
    # converting RGB to BGR
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    
    #Grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #Reduce Noise
    blur = cv2.GaussianBlur(gray,(5,5),0)
    
    #binary threshold
    threshold = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    return threshold


# Extracting the text from the image 
def extract_text(image):
    processed = preprocess_image(image)
    text = pytesseract.image_to_string(processed,lang="eng")
    return text.strip()


# Extract text with confidence
def extract_text_with_confidence(image):
    processed = preprocess_image(image)
    data = pytesseract.image_to_data(processed,output_type=pytesseract.Output.DICT)
    words =[]
    confidence =[]
    for word,conf in zip(data["text"],data["conf"]):
        word = word.strip()
        if word !="":
            words.append(word)
            try:
                confidence.append(float(conf))
            except:
                pass
            
    final_text = " ".join(words)
    avg_confidence = (sum(confidence)/len(confidence)
                      if confidence
                      else 0
    )
    
    return final_text,round(avg_confidence,2)


# Now saving the Extracted text 
def save_text(text,filename="output/extracted_text.txt"):
    with open(filename,"w",encoding="utf-8")as file:
        file.write(text)
        

# creating the support for language
def supported_languages():
    return[
        "eng"
    ]