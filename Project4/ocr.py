# ==========================================
# AI Image Text Recognition
# OCR Engine using EasyOCR
# ==========================================

import easyocr
import cv2
import numpy as np
from PIL import Image

# ==========================================
# EasyOCR Reader
# ==========================================

@st.cache_resource
def get_reader():
    return easyocr.Reader(
        ['en'],
        gpu=False,
        verbose=False
    )

# ==========================================
# Image Preprocessing
# ==========================================

def preprocess_image(image):

    # PIL -> NumPy
    img = np.array(image)

    # RGB -> BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Resize (3x for better OCR)
    img = cv2.resize(
        img,
        None,
        fx=3,
        fy=3,
        interpolation=cv2.INTER_CUBIC
    )

    # Gray
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # Denoise
    gray = cv2.fastNlMeansDenoising(
        gray,
        None,
        12,
        7,
        21
    )

    # Contrast Enhancement
    gray = cv2.equalizeHist(gray)

    # Sharpen
    kernel = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

    gray = cv2.filter2D(
        gray,
        -1,
        kernel
    )

    # Adaptive Threshold
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return thresh


# ==========================================
# OCR
# ==========================================

def extract_text(image):

    text, _ = extract_text_with_confidence(image)

    return text


# ==========================================
# OCR + Confidence
# ==========================================

def extract_text_with_confidence(image):

    processed = preprocess_image(image)
    reader = get_reader()
    result = reader.readtext(
        processed,
        detail=1,
        paragraph=True,
        decoder="beamsearch",
        contrast_ths=0.05,
        adjust_contrast=0.7,
        width_ths=0.7,
        height_ths=0.7
    )

    words = []
    confidence = []

    for detection in result:

        text = detection[1].strip()
        score = detection[2]

        # Ignore low confidence garbage
        if score > 0.45:

            words.append(text)
            confidence.append(score * 100)

    final_text = "\n".join(words)

    avg_confidence = (
        sum(confidence) / len(confidence)
        if confidence
        else 0
    )

    return final_text, round(avg_confidence,2)


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
# Save Text
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
# Languages
# ==========================================

def supported_languages():

    return ["English"]
