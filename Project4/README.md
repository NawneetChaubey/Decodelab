# 📄 AI Image Text Recognition

An AI-powered Optical Character Recognition (OCR) application built using **Python**, **Streamlit**, **OpenCV**, and **Tesseract OCR**.

This project was developed as **Project 4** of the **DecodeLabs Artificial Intelligence Internship Program**.

---

## 📌 Project Overview

AI Image Text Recognition extracts text from images using Optical Character Recognition (OCR). The application preprocesses uploaded images using OpenCV techniques before extracting text with the Tesseract OCR engine.

---

## 🚀 Features

- 📤 Upload Image
- 🖼 Image Preview
- ⚫ Grayscale Conversion
- 🌫 Noise Reduction
- ⚪ Threshold Processing
- 🤖 OCR Text Extraction
- 📊 OCR Confidence Score
- 📥 Download Extracted Text
- 🎨 Interactive Streamlit UI

---

## 🧠 OCR Workflow

1. Upload an Image
2. Resize Image
3. Convert to Grayscale
4. Apply Gaussian Blur
5. Apply Thresholding
6. Extract Text using Tesseract OCR
7. Display & Download Results

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- Pillow
- NumPy
- Pytesseract
- Tesseract OCR

---

## 📂 Project Structure

```text
AI-Image-Text-Recognition/
│
├── app.py
├── ocr.py
├── image_utils.py
├── requirements.txt
├── README.md
```

---

## ▶️ Installation

Clone Repository

```bash
git clone https://github.com/NawneetChaubey/AI-Image-Text-Recognition.git
```

Move into Project

```bash
cd AI-Image-Text-Recognition
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

## ⚙️ Install Tesseract OCR

Download Tesseract OCR from:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path inside `ocr.py` if required:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```


## 📈 Future Improvements

- Multi-language OCR
- PDF Text Extraction
- Handwritten Text Recognition
- Batch Image Processing
- OCR Confidence Visualization
- Image Rotation Correction

---

## 👨‍💻 Author

**Nawnit Kumar Chaubey**

B.Tech Computer Science Engineering (AI & Data Science)

---

## 📜 License

This project was developed for educational purposes as part of the DecodeLabs Artificial Intelligence Internship Program.
