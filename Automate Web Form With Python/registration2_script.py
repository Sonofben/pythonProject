import requests
from bs4 import BeautifulSoup

def register_on_website(email, fullname, zone, group):
    base_url = "http://reachoutworld.org/group/udugroup"
    registration_url = f"{ http://reachoutworld.org}http://reachoutworld.org/register"

    responses = requests.get(registration_url)
    if responses.status_code != 200:
        print("Failed to access the registration page")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")
    print(csrf_token)

    registration_data = {
        "email": email,
        'fullname': fullname,
        "zone": zone,
        "group": group,
        "csrf_token": csrf_token,

    }

    response = requests.post(registration_url, data=registration_data)
    if response.status_code == 200:
        print("Registration successful")
    else:
        print("registration fail")


agrs = [
    {"email": "thomas@gmail.com",
     "fullname": "thomas",
     "zone":"zone",
     "group":"group"},
{"email": "tho@gmail.com",
 "fullname": "tho",
 "zone": "zone",
"group": "group"},
]
