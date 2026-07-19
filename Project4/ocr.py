from paddleocr import PaddleOCR
import cv2
import numpy as np
from PIL import Image
import streamlit as st

# ---------------------------
# Load PaddleOCR only once
# ---------------------------
@st.cache_resource
def get_ocr():
    return PaddleOCR(
        use_angle_cls=True,
        lang="en",
        show_log=False
    )

# ---------------------------
# Image Preprocessing
# ---------------------------
def preprocess_image(image):

    img = np.array(image)

    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img

    # Resize for better OCR
    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Denoise
    gray = cv2.fastNlMeansDenoising(gray)

    # Adaptive Threshold
    gray = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return gray


# ---------------------------
# Extract Text
# ---------------------------
def extract_text(image):

    processed = preprocess_image(image)

    ocr = get_ocr()

    result = ocr.ocr(processed)

    text = []

    if result and result[0]:
        for line in result[0]:
            text.append(line[1][0])

    return "\n".join(text)


# ---------------------------
# Extract Text + Confidence
# ---------------------------
def extract_text_with_confidence(image):

    processed = preprocess_image(image)

    ocr = get_ocr()

    result = ocr.ocr(processed)

    words = []
    scores = []

    if result and result[0]:

        for line in result[0]:

            txt = line[1][0]
            score = line[1][1]

            words.append(txt)
            scores.append(score * 100)

    final_text = "\n".join(words)

    confidence = (
        sum(scores) / len(scores)
        if scores else 0
    )

    return final_text, round(confidence, 2)


# ---------------------------
# Draw OCR Boxes
# ---------------------------
def draw_boxes(image):

    img = np.array(image)

    img_bgr = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2BGR
    )

    ocr = get_ocr()

    result = ocr.ocr(img_bgr)

    if result and result[0]:

        for line in result[0]:

            box = np.array(line[0]).astype(int)

            cv2.polylines(
                img_bgr,
                [box],
                True,
                (0, 255, 0),
                2
            )

    rgb = cv2.cvtColor(
        img_bgr,
        cv2.COLOR_BGR2RGB
    )

    return Image.fromarray(rgb)


# ---------------------------
# Save Text
# ---------------------------
def save_text(text, filename="output.txt"):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(text)

    return filename


# ---------------------------
# Supported Languages
# ---------------------------
def supported_languages():

    return [
        "English"
    ]
