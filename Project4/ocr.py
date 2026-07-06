# ==========================================
# AI Image Text Recognition
# OCR Engine using EasyOCR
# ==========================================

import easyocr
import cv2
import numpy as np
from PIL import Image

# ==========================================
# Initialize EasyOCR Reader
# ==========================================

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

# ==========================================
# Image Preprocessing
# ==========================================

def preprocess_image(image):

    # Convert PIL Image to NumPy
    img = np.array(image)

    # RGB -> BGR
    img = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2BGR
    )

    # Convert to Grayscale
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # Reduce Noise
    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    # Binary Threshold
    threshold = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return threshold


# ==========================================
# Extract Text Only
# ==========================================

def extract_text(image):

    text, _ = extract_text_with_confidence(image)

    return text


# ==========================================
# Extract Text + Confidence
# ==========================================

def extract_text_with_confidence(image):

    processed = preprocess_image(image)

    result = reader.readtext(processed)

    words = []

    confidence = []

    for detection in result:

        text = detection[1]

        score = detection[2]

        words.append(text)

        confidence.append(score * 100)

    final_text = " ".join(words)

    avg_confidence = (
        sum(confidence) / len(confidence)
        if confidence
        else 0
    )

    return final_text, round(avg_confidence, 2)


# ==========================================
# Draw Bounding Boxes
# ==========================================

def draw_boxes(image):

    img = np.array(image)

    img = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2BGR
    )

    result = reader.readtext(img)

    for detection in result:

        box = detection[0]

        top_left = tuple(map(int, box[0]))
        bottom_right = tuple(map(int, box[2]))

        cv2.rectangle(
            img,
            top_left,
            bottom_right,
            (0,255,0),
            2
        )

    img = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    return Image.fromarray(img)


# ==========================================
# Save Extracted Text
# ==========================================

def save_text(
    text,
    filename="output/extracted_text.txt"
):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)


# ==========================================
# Supported Languages
# ==========================================

def supported_languages():

    return [
        "English"
    ]
