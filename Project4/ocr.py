import streamlit as st
import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

API_KEY = st.secrets["OCR_API_KEY"]


def preprocess_image(image):
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    gray = cv2.fastNlMeansDenoising(gray)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return Image.fromarray(thresh)


def extract_text(image):

    image = preprocess_image(image)

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    buffer.seek(0)

    response = requests.post(

        "https://api.ocr.space/parse/image",

        files={
            "image": ("image.png", buffer, "image/png")
        },

        data={
            "apikey": API_KEY,
            "language": "eng",
            "OCREngine": "2"
        }
    )

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        return ""

    return result["ParsedResults"][0]["ParsedText"]


def extract_text_with_confidence(image):

    text = extract_text(image)

    confidence = 100 if text.strip() else 0

    return text, confidence


def draw_boxes(image):

    return image


def save_text(text, filename="output.txt"):

    with open(filename, "w", encoding="utf-8") as f:

        f.write(text)


def supported_languages():

    return ["English"]
