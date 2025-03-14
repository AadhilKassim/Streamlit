import streamlit as st
from functions import get_guessed_age

st.set_page_config(
   page_title="Mental-ly",
   page_icon="💀",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Welcome to My Streamlit App")

# Sidebar navigation using buttons
st.sidebar.header("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("About"):
    st.session_state.page = "About"
if st.sidebar.button("Contact"):
    st.session_state.page = "Contact"

# Initialize session state for page if not already set
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page content
if st.session_state.page == "Home":
    st.header("Age Detector")
    st.write("Come and find out your true mental age based on your name!")

    user_input = st.text_input("Enter a name to guess the age:")
    if user_input:
        guessed_age = get_guessed_age(user_input)
        if guessed_age is not None:
                        st.markdown(f"<h1 style='text-align: center; color: Blue;'>{guessed_age}</h1>", unsafe_allow_html=True)
                        st.balloons()
        else:
            st.write("Failed to fetch data from the API. Please try again later.")

elif st.session_state.page == "About":
    st.header("About")
    st.write("This app uses the Agify API to guess the age based on a name.")

elif st.session_state.page == "Contact":
    st.header("Contact")
    st.write("For inquiries, please contact us at: example@example.com")