import requests
from bs4 import BeautifulSoup
import json

# Load data from JSON file
with open("registration_data.json", 'r') as json_file:
    data = json.load(json_file)

registration_url = 'https://reachoutworld.org/group/udugroup'

for person in data:
    session = requests.Session()
    response = session.get(registration_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    csrf_token_input = soup.find("input", {"name": "csrf_token"})
    if csrf_token_input:
        csrf_token = csrf_token_input.get("value")
        print(csrf_token)
    else:
        session.close()
        continue
    fullnames_input = soup.find('input', {'name': 'fullnames'})
    email_input = soup.find('input', {'name': 'email'})
    zone_input = soup.find('input', {'name': 'zone'})
    group_input = soup.find('input', {'name': 'group'})

    fullnames_input['value'] = person['fullnames']
    email_input['value'] = person['email']
    zone_input['value'] = person['zone']
    group_input['value'] = person['group']

    form_data = {
        'csrf_token': csrf_token,
        'fullnames': person['fullnames'],
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
