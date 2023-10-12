import logging
import requests
from bs4 import BeautifulSoup
import json

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load registration data from a JSON file
with open("data2.json", 'r') as json_file:
    data = json.load(json_file)

# Define the registration URL
registration_url = "https://healingstreams.tv/LHS/online_reg.php#registernow"

# Create a session to persist cookies and headers
session = requests.Session()

# Iterate through the registration data for each person
for person in data:
    try:
        # Send a GET request to the registration URL
        response = session.get(registration_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Log an error if there's an issue with the GET request and continue to the next person
        logging.error(f"Error during GET request for {person['email']}: {e}")
        continue

    # Parse the HTML response with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the CSRF token from the page
    csrf_token_input = soup.find("input", {"name": "csrf_token"})
    if csrf_token_input:
        csrf_token = csrf_token_input.get("value")
        print(f"CSRF Token for {person['email']}: {csrf_token}")
    else:
        # Log an error if CSRF token is not found and continue to the next person
        logging.error(f"CSRF token not found for {person['email']}")
        continue

    # Find the input fields for registration data
    email_input = soup.find('input', {'name': 'email'})
    fullname_input = soup.find('input', {'name': 'fullname'})
    username_input = soup.find('input', {'name': 'username'})
    password_input = soup.find('input', {'name': 'password'})

    # Fill in the input fields with person's data
    email_input['value'] = person['email']
    fullname_input['value'] = person['fullname']
    username_input['value'] = person['username']
    password_input['value'] = person['password']

    # Prepare the form data for registration
    form_data = {
        'csrf_token': csrf_token,
        'email': person['email'],
        'fullname': person['fullname'],
        'username': person['username'],
        'password': person['password']
    }

    # Send a POST request with the registration data
    response = session.post(registration_url, data=form_data)

    if response.status_code == 200:
        # Log a success message if registration is successful
        logging.info(f"Registered {person['email']} successfully!")
    else:
        # Log an error if registration fails
        logging.error(f"Registration failed for {person['email']}")

# Close the session to release resources
session.close()