import requests
from bs4 import BeautifulSoup
import json

# Load data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

registration_url = 'https://reachoutworld.org/group/udugroup'

for person in data:
    session = requests.Session()

    try:
        response = session.get(registration_url)
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the website: {e}")
        continue  # Skip this person's registration and move on to the next

    soup = BeautifulSoup(response.text, 'html.parser')

    csrf_token_input = soup.find("input", {"name": "csrf_token"})
    if csrf_token_input:
        csrf_token = csrf_token_input.get("value")
    else:
        session.close()
        continue

    # The rest of your registration code...

    session.close()
