import requests

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