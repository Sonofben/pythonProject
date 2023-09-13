import requests
import json
from bs4 import BeautifulSoup

with open("data.json", 'r') as json_file:
    data = json.load(json_file)
def register_on_website(email, fullnames, zone, group):
    base_url = "http:reachoutworld.org/group/udugroup"
    registration_url = "http:reachoutworld.org/register"

    responses = requests.get(registration_url)
    if responses.status_code != 200:
        print("Failed to access the registration page")
        return

    soup = BeautifulSoup(responses.text, "html.parser")

    registration_data = {
        "email": email,
        "fullnames": fullnames,
        "zone": zone,
        "group": group,
    }

    response = requests.post(registration_url, data=registration_data)
    if response.status_code == 200:
        print("Registration successful")
    else:
        print("Registration failed")
