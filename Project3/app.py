import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

from recommendation import(
    recommend_courses,
    dataset_info,
    get_categories,
    preview,
    courses
)

# streamlit page Configuration 
st.set_page_config(
    page_title="SmartCourse Recommender AI",
    page_icon="🎓",
    layout="wide"
)


# sidebar of the page
info = dataset_info()
with st.sidebar:
    st.title("🎓 SmartCourse AI")
    st.markdown("### 📊 Dataset ")
    st.metric("Courses",info["Total Courses"])
    st.metric("Categories",info["Categories"])
    
    st.markdown("---")
    
    st.metric("Beginner",info ["Beginner"])
    st.metric("Intermediate",info["Intermediate"])
    st.metric("Advanced",info["Advanced"])
    
    st.markdown("---")
    
    difficulty = st.selectbox(
        "Difficulty",
        ["All","Beginner","Intermediate","Advanced"]
    )
    
    top_n = st.slider(
        "Recommendations",
        1,10,5
    )
    
    
# header of the page
st.title("🎓 SmartCourse Recommender AI")
st.caption(
    "AI Recommendation System using TF-IDF & Cosine Similarity"
)

st.markdown("---")

# configuring the user intrest
categories = get_categories()
selected = st.multiselect(
    "Select Your Intrests",
    categories
)

st.write("Selected Intrests")

if selected:
    st.success(", ".join(selected))
else:
    st.info("Please select at least one interest.")
    

#  Configuring Recommendation Button 
if st.button("🚀 Recommend Courses", use_container_width=True):
    if len(selected)==0:
        st.warning("Please select at least one interest")
    else:
        result = recommend_courses(selected,difficulty,top_n)
        if result.empty:
            st.error("No recommendation found.")
        else:
            st.success(f"Found {len(result)} recommendations.")
            
            st.markdown("---")
            st.subheader("📚 Recommended Courses")
            for _, row in result.iterrows():
                with st.container():
                    st.markdown(
                        f"## 📘 {row['Title']} "
                    )
                    
                    col1,col2 = st.columns(2)
                    
                    with col1:
                        st.write(
                            f"**Category:** {row['Category']}"
                        )
                        
                        st.write(
                            f"**Difficulty:** {row['Difficulty']}"
                        )
                         
                        st.write(
                            f"**Duration:** {row['Duration']}"
                        )
                        
                    with col2:
                        st.write(
                            f"⭐ Rating: {row['Rating']}"
                        )
                        
                        st.write(
                            f"🎯 Match: {row['Match']:.2f}%"
                        )
                        
                        st.write(row["Description"])
                        st.write("**Skills**")
                        st.info(row["Tags"])
                        
                        st.progress(
                            min(
                                int(row["Match"]),  
                                100
                            )
                        )
                        
                        st.markdown("---")
        
 
# Dataset preview
st.subheader("📄 Dataset Preview")
st.dataframe(
    preview(),
    use_container_width=True,
    hide_index=True
)

# Category Distribution 
st.subheader("📊 Category Distribution")

full_courses = courses

category_count = full_courses["Category"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

category_count.plot(
    kind="bar",
    ax=ax,
    color="skyblue"
)

ax.set_xlabel("Category")
ax.set_ylabel("Number of Courses")
ax.set_title("Courses by Category")

plt.xticks(rotation=45)

st.pyplot(fig)


# configuring the footer
st.markdown("---")
st.caption(
    "Developed by Nawnit kumar chaubey | DecodeLabs AI Intership Project 3"
)
