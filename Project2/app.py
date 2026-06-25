

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

from model import (
    predict_species,
    accuracy,
    f1,
    cm
)

st.set_page_config(
    page_title="FlowerSense AI",
    page_icon="🌸",
    layout="wide"
)


iris = load_iris()



with st.sidebar:

    st.title("🌸 FlowerSense AI")

    st.markdown("### 📊 Dataset Information")

    st.write("📄 Samples : 150")
    st.write("🌼 Classes : 3")
    st.write("📊 Features : 4")

    st.markdown("---")

    st.success(f"Model Accuracy : {accuracy:.2%}")

    st.info("Algorithm : K-Nearest Neighbors (KNN)")


st.title("🌸 FlowerSense AI")

st.caption(
    "Iris Flower Classification using K-Nearest Neighbors (KNN)"
)

st.markdown("---")



col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        value=5.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        value=3.5
    )

with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        value=1.4
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        value=0.2
    )



if st.button("🔍 Predict Species", use_container_width=True):

    species = predict_species([
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ])

    st.success(
        f"🌸 Predicted Species : **{species.title()}**"
    )

    if species.lower() == "setosa":

        st.info(
            "🌼 Setosa flowers generally have short petals and broad sepals."
        )

    elif species.lower() == "versicolor":

        st.info(
            "🌺 Versicolor flowers have medium-sized petals."
        )

    else:

        st.info(
            "🌸 Virginica flowers usually have the largest petals."
        )

st.markdown("---")



st.subheader("📈 Model Performance")

metric1, metric2 = st.columns(2)

with metric1:

    st.metric(
        "Accuracy",
        f"{accuracy:.2%}"
    )

with metric2:

    st.metric(
        "F1 Score",
        f"{f1:.2%}"
    )

st.markdown("---")


st.subheader("📊 Confusion Matrix")

fig, ax = plt.subplots(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=[
        "Setosa",
        "Versicolor",
        "Virginica"
    ],
    yticklabels=[
        "Setosa",
        "Versicolor",
        "Virginica"
    ],
    linewidths=1,
    linecolor="white",
    cbar=True,
    ax=ax
)

ax.set_xlabel("Predicted Class")
ax.set_ylabel("Actual Class")
ax.set_title("Confusion Matrix")

st.pyplot(fig)

st.markdown("---")



st.subheader("🌿 Iris Dataset Preview")

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["Species"] = iris.target

df["Species"] = df["Species"].map({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")


with st.expander("📖 About This Project"):

    st.write("""
This project demonstrates a basic supervised machine learning
classification model using the famous Iris Dataset.

Workflow:
- Load Dataset
- Train-Test Split
- Feature Scaling
- Train KNN Classifier
- Predict Flower Species
- Evaluate using Accuracy, F1 Score and Confusion Matrix

Developed as part of DecodeLabs Artificial Intelligence Internship.
""")

st.markdown("---")


st.caption(
    "🌸 Developed by Nawnit Kumar Chaubey | DecodeLabs AI Internship Project 2"
)