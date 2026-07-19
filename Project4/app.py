import streamlit as st
from PIL import Image
import easyocr
from ocr import (
    extract_text_with_confidence,
    extract_text,
    draw_boxes,
    save_text,
    supported_languages
)

from image_utils import (
    grayscale,
    blur,
    threshold,
    resize
)

@st.cache_resource
def get_reader():
    return easyocr.Reader(
        ['en'],
        gpu=False,
        verbose=False
    )

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Image Text Recognition",
    page_icon="📄",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("📄 AI OCR")

    st.markdown("---")

    st.markdown("## Features")

    st.success("✅ Image Upload")
    st.success("✅ OCR")
    st.success("✅ Image Processing")
    st.success("✅ Text Extraction")
    st.success("✅ Download Text")

    st.markdown("---")

    st.info("""
Supported Formats

• JPG
• JPEG
• PNG
• BMP
""")

# ==========================
# Header
# ==========================

st.title("📄 AI Image Text Recognition")

st.caption(
    "Extract text from images using OpenCV + EasyOCR"
)

st.markdown("---")

# ==========================
# Upload Image
# ==========================

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=[
        "png",
        "jpg",
        "jpeg",
        "bmp"
    ]
)

# ==========================
# Image Preview
# ==========================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image = resize(image)

    st.subheader("🖼 Original Image")

    st.image(
        image,
        use_container_width=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("Grayscale")

        gray = grayscale(image)

        st.image(
            gray,
            use_container_width=True,
            clamp=True
        )

    with col2:

        st.subheader("Blur")

        blur_img = blur(image)

        st.image(
            blur_img,
            use_container_width=True,
            clamp=True
        )

    with col3:

        st.subheader("Threshold")

        thres = threshold(image)

        st.image(
            thres,
            use_container_width=True,
            clamp=True
        )

    st.markdown("---")

    st.success("✅ Image Ready for OCR")

    # ==========================
    # OCR Button
    # ==========================

    if st.button(
        "🚀 Extract Text",
        use_container_width=True
    ):

        with st.spinner("Reading Image..."):

            text, confidence = extract_text_with_confidence(image)

        st.markdown("---")

        st.subheader("📄 Extracted Text")

        if text.strip() == "":

            st.warning("No text detected in the image.")

        else:

            st.text_area(
                "OCR Result",
                text,
                height=250
            )

            st.success(
                f"Average Confidence : {confidence:.2f}%"
            )

            words = len(text.split())
            characters = len(text)
            lines = len(text.splitlines())

            c1, c2, c3 = st.columns(3)

            c1.metric("Words", words)
            c2.metric("Characters", characters)
            c3.metric("Lines", lines)

            st.download_button(
                label="📥 Download Text",
                data=text,
                file_name="Extracted_Text.txt",
                mime="text/plain",
                use_container_width=True
            )

else:

    st.info("👆 Please upload an image to start OCR.")

# ==========================
# Footer
# ==========================

st.markdown("---")

st.caption("Developed by Nawnit Kumar Chaubey")

st.caption("DecodeLabs AI Internship Project 4")
