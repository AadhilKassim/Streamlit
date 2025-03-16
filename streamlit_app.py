import streamlit as st
import requests
from functions import get_guessed_age

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
            if guessed_age > 60:
                st.error("You are too old! Go and take a nap. You need it.")
            elif guessed_age < 20:
                st.success("You are too young! Go and play some games.")
                st.balloons()
            else:
                st.balloons()

            # Additional section to know more about the person
            st.subheader("Tell us more about yourself:")
            is_single = st.checkbox("Are you single?")
            joke_category = st.selectbox(
                "What type of joke would you like?",
                ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]
            )
            st.caption("Additional options coming soon!")

            if is_single:
                st.write("*I'm single too! Let's mingle.*")


            # Fetch and display a joke based on the selected category
            st.subheader("Here's a joke to brighten your day:")
            try:
                response = requests.get(f"https://sv443.net/jokeapi/v2/joke/{joke_category}")
                if response.status_code == 200:
                    joke_data = response.json()
                    if joke_data["type"] == joke_category:
                        st.write(joke_data["joke"])
                    elif joke_data["type"] == "twopart":
                        st.write(f"{joke_data['setup']} ... {joke_data['delivery']}")
                else:
                    st.warning("Couldn't fetch a joke at the moment. Please try again later.")
            except Exception as e:
                st.error(f"An error occurred while fetching a joke: {e}")
        else:
            st.write("Failed to fetch data from the API. Please try again later.")

elif st.session_state.page == "About":
    st.header("About")
    st.write("This app uses the Agify API to guess the age based on a name. The app is built using Streamlit and hosted on Streamlit community cloud. You can find the source code on GitHub.\n\nI'll be adding more features to this app soon. Stay tuned!")

elif st.session_state.page == "Contact":
    st.header("Contact")
    st.write("For inquiries, please contact: aadhikassim@gmail.com\n\nPortfolio: https://aadhilkassim.github.io\n\nMore jokes and fun stuff coming soon! Find me at: [GitHub](https://www.github.com/AadhilKassim)")