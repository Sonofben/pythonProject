import logging
import requests
from bs4 import BeautifulSoup
import json

# Load data from JSON file
with open("Emeis2Learndata.json", 'r') as json_file:
    data = json.load(json_file)



registration_url: str = 'https://emeis2learn.newzenler.com/'

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

    firstname_input = soup.find('input', {'name': 'firstname'})
    lastname_input = soup.find('input', {'name': 'lastname'})
    emailaddress_input = soup.find('input', {'name': 'emailaddress'})
    password_input = soup.find('input', {'name': '[password'})

    firstname_input['value'] = person['fullnames']
    lastname_input['value'] = person['email']
    emailaddress_input['value'] = person['zone']
    password_input['value'] = person['group']

    form_data = {
        'csrf_token': csrf_token,
        'firstname': person['firstname'],
        'lastname': person['lastname'],
        'emailaddress': person['emailaddress'],
        'password': person['password']
    }

    response = session.post(registration_url, data=form_data)

    if response.status_code == 200:
        logging.info(f"Registered {person['firstname']} successfully!")
    else:
        logging.error(f"Registration failed for {person['firstname']}")

    session.close()
