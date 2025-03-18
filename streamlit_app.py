import streamlit as st
import requests
from functions import *

st.set_page_config(
   page_title="Mental-ly",
   page_icon="💀",
   layout="wide",
   initial_sidebar_state="collapsed",
)

st.title("Welcome to My Streamlit App", anchor=None)

# Sidebar navigation using buttons
st.sidebar.header("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("About"):
    st.session_state.page = "About"
if st.sidebar.button("Contact"):
    st.session_state.page = "Contact"

# Initialize session state for page, show_joke_section, last_processed_name, and last_guessed_age if not already set
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "show_joke_section" not in st.session_state:
    st.session_state.show_joke_section = False
if "last_processed_name" not in st.session_state:
    st.session_state.last_processed_name = ""
if "last_guessed_age" not in st.session_state:
    st.session_state.last_guessed_age = None

# Page content
if st.session_state.page == "Home":
    st.header("Age Detector")
    st.write("Come and find out your true mental age based on your name!")

    user_input = st.text_input("Enter a name to guess the age:")
    if user_input and user_input != st.session_state.last_processed_name:
        guessed_age = get_guessed_age(user_input)
        if guessed_age is not None:
            st.session_state.last_guessed_age = guessed_age
            st.markdown(f"<h1 style='text-align: center; color: Blue;'>{guessed_age}</h1>", unsafe_allow_html=True)
            if guessed_age > 60:
                st.error("You are too old! Go and take a nap. You need it.")
            elif guessed_age < 20:
                st.success("You are too young! Go and play some games.")
                st.balloons()
            else:
                st.balloons()
            st.session_state.show_joke_section = True
        else:
            st.write("Failed to fetch data from the API. Please try again later.")
        st.session_state.last_processed_name = user_input
    elif st.session_state.last_guessed_age is not None:
        st.markdown(f"<h1 style='text-align: center; color: Blue;'>{st.session_state.last_guessed_age}</h1>", unsafe_allow_html=True)

    if st.session_state.show_joke_section:
        st.subheader("Tell us more about yourself:")
        is_single = st.checkbox("Are you single?")
        if is_single:
            st.write("*I'm single too! Let's mingle.*")
        joke_category = st.selectbox(
            "What type of joke would you like?",
            [" ", "Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"],
            format_func=lambda x: "Select a category" if x == " " else x
        )
        st.caption("Additional options coming soon!")

        get_joke(joke_category)

elif st.session_state.page == "About":
    st.header("About")
    st.write("This app uses the Agify API to guess the age based on a name. The app is built using Streamlit and hosted on Streamlit community cloud. You can find the source code on GitHub.\n\nI'll be adding more features to this app soon. Stay tuned!")

elif st.session_state.page == "Contact":
    st.header("Contact")
    st.write("For inquiries, please contact: aadhikassim@gmail.com\n\nPortfolio: https://aadhilkassim.github.io\n\nMore jokes and fun stuff coming soon! Find me at: [GitHub](https://www.github.com/AadhilKassim)")