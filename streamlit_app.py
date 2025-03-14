import streamlit as st

# Title of the app
st.title("Welcome to My Streamlit App")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.text("Use the sidebar to navigate")

# Main content
st.header("Main Content")
st.write("This is a basic Streamlit app setup. Add your content here!")

# Input example
user_input = st.text_input("Enter some text:")
if user_input:
    st.write(f"You entered: {user_input}")