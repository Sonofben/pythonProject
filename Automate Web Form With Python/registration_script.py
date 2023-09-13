import logging
import requests
from bs4 import BeautifulSoup
import json

# Load data from JSON file
with open("data.json", 'r') as json_file:
    data = json.load(json_file)

registration_url = 'https://reachoutworld.org/'

for person in data:
    session = requests.Session()
    try:
        response = session.get(registration_url)
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")
        session.close()
        continue
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
        logging.info(f"Registered {person['fullnames']} successfully!")
    else:
        logging.error(f"Registration failed for {person['fullnames']}")

    session.close()
