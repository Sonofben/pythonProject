import requests
from bs4 import BeautifulSoup
import json

# Load data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# URL of the registration form
registration_url = 'https://reachoutworld.org/group/udugroup'  # Replace with the actual URL

# Iterate through each person's data and register them
for person in data:
    session = requests.Session()
    response = session.get(registration_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract form fields (you'll need to inspect the page to find the actual field names)
    csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")
    fullnames_input = soup.find('input', {'name': 'fullnames'})
    email_input = soup.find('input', {'name': 'email'})
    zone_input = soup.find('input', {'name': 'zone'})
    group_input = soup.find('input', {'name': 'group'})

    fullnames_input['value'] = person['name']
    email_input['value'] = person['email']
    zone_input['value'] = person['zone']
    group_input['value'] = person['group']

    form_data = {
        'csrf_token': csrf_token,
        'fullnames': person['name'],
        'email': person['email'],
        'zone': person['zone'],
        'group': person['group']
    }

    response = session.post(registration_url, data=form_data)

    if response.status_code == 200:
        print(f"Registered {person['fullnames']} successfully!")
    else:
        print(f"Registration failed for {person['fullnames']}")

    session.close()
