import streamlit as st
from functions import get_guessed_age

st.title("Welcome to My Streamlit App")

st.sidebar.header("Navigation")
st.sidebar.text("Use the sidebar to navigate")


st.header("Age Detector")
st.write("Come and find out your true mental age based on your name!")


user_input = st.text_input("Enter a name to guess the age:")
if user_input:
    guessed_age = get_guessed_age(user_input)
    if guessed_age is not None:
        st.write(f"The guessed age for the name '{user_input}' is: {guessed_age}")
    else:
        st.write("Failed to fetch data from the API. Please try again later.")