import streamlit as st
from PIL import Image
from ocr import(
    extract_text,
    extract_text_with_confidence,
    save_text
)
from image_utils import(
    grayscale,
    blur,
    threshold,
    resize
)

# page configuration
st.set_page_config(
    page_title="AI Image Text Recognition",
    page_icon= "📄",
    layout="wide"
)

# configure the sidebar
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
    st.info(
        """
        Supported Formats
        .JPG
        .PNG
        .JPEG
        .BMP
 
        """
        
    )
    
    
    
#configuring the header
st.title("📄 AI Image Text Recognition")
st.caption(
    "Extract text from images using OpenCV + Tesseract OCR"
)
st.markdown("---")

# configure uploading the image
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=[
        "png",
        "jpg",
        "jpeg",
        "bmp"
    ]
)

#previewing the image
if uploaded_file:
    image = Image.open(uploaded_file)
    image = resize(image)
    st.subheader("🖼 Original Image")
    st.image(
        image,
        use_column_width=True
    )
    st.markdown("---")
    col1,col2,col3 = st.columns(3)
    
    with col1:
        st.subheader("Grayscale")
        gray = grayscale(image)
        st.image(
            gray,
            use_column_width=True,
            clamp=True
        )
        
    with col2:
        st.subheader("Blur")
        blur_img = blur(image)
        st.image(
            blur_img,
            use_column_width=True,
            clamp=True
        )
        
        
    with col3:
        st.subheader("Threshold")
        thres = threshold(image)
        st.image(
            thres,
            use_column_width=True,
            clamp=True
        )
        
    st.markdown("---")
    st.success("✅ Image Ready for OCR")
    
    
# setting the OCR
if st.button(
    "🚀 Extract Text",
    use_container_width=True
):
    with st.spinner(
        "Reading Image..."
    ):
        text ,confidence = extract_text_with_confidence(
            image
        )
        st.markdown("---")
        st.subheader("📄 Extracted Text")
        if text.strip()=="":
            st.warning(
                "NO text detected in the image."
            )
        else:
            st.text_area(
                "OCR Result",
                text,
                height=250
            )
            st.success(f"Average Confidence : {confidence:.2f}%")
            
            # statistics 
            words = len(text.split())
            characters = len(text)
            lines = len(text.splitlines())
            col1,col2,col3 = st.columns(3)
            
            with col1:
                st.metric("words",words)
                
            with col2:
                st.metric("Characters",characters)
                
            with col3:
                st.metric("Lines",lines)
                
            # config Download
            
            st.download_button(
                label="📥 Download Text",
                data=text,
                file_name="Extracted_Test.txt",
                mime="text/plain",
                use_container_width=True
            )
            
            
# config footer
st.markdown("---")
st.caption(
    "Developed by Nawnit Kumar Chaubey"
)
st.caption(
    "DecodeLabs AI Internship Project4"
)