# Ai recommendation system for different programming courses

# importing the python libraries 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# loading the datasets
courses = pd.read_csv("data/courses.csv")

# creating the search text 
courses["content"]=(
    courses["Category"].fillna("") + " " + courses["Description"].fillna("") + " " + courses["Tags"].fillna("")
)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(courses["content"])

# creating the recommendation system
def recommend_courses(interests,difficulty="ALL",top_n=5):
    """
    Recommend courses based on user interests
    
    Parameters
    ----------
    interests: list
         user selected interests
         
    difficulty : str
         Beginner/Intermediate/Advance/All
         
    top_n : int 
         Number of recommendations
         
    Returns
    -------
    DataFrame 
    
    """
    
    if not interests:
        return pd.DataFrame()
    
    # user query
    query = " ".join(interests)
    query_vector = vectorizer.transform([query])
    
    similarity = cosine_similarity(query_vector,tfidf_matrix).flatten()
    recommendations = courses.copy()
    recommendations["Match"] = similarity * 100
    
    if difficulty != "ALL":
        recommendations = recommendations[recommendations["Difficulty"]==difficulty]
    
    recommendations = recommendations.sort_values(by="Match",ascending=False)
    return recommendations.head(top_n)


# getting the dataset information 
def dataset_info():
    return{
        "Total Courses": len(courses),
        "Categories": courses["Category"].nunique(),
        "Beginner": len(courses[courses["Difficulty"]== "Beginner"]),
        "Intermediate": len(courses[courses["Difficulty"]=="Intermediate"]),
        "Advanced": len(courses[courses["Difficulty"]=="Advanced"]),
    }
    
    
# Available Categories 
def get_categories():
    return sorted(
        courses["Category"].unique()
    )
    
    
# previewing the dataset 
def preview():
    return courses.head(10)
    