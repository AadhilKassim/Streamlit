import requests
import streamlit as st

def get_guessed_age(name):
    """
    Calls the Agify API to guess the age based on the given name.
    """
    try:
        response = requests.get(f"https://api.agify.io/?name={name}")
        if response.status_code == 200:
            data = response.json()
            return data.get("age", "Unknown")
        else:
            return None
    except Exception as e:
        return None
    
def get_joke(joke_category):
    """
    Calls the JokeAPI to get a joke based on the given category.
    """
    # Fetch and display a joke based on the selected category
    if joke_category != " ":
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