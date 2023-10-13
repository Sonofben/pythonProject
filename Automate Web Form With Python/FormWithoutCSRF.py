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
registration_url = "https://healingstreams.tv/LHS/online_reg.php"  # Update to the correct URL

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

    # Find the input fields for registration data (inspect the HTML to get the correct field names)
    email_input = soup.find('input', {'name': 'email'})  # Update with the correct field names
    fullname_input = soup.find('input', {'name': 'full_name'})
    country_input = soup.find('input', {'name': 'country'})
    state_input = soup.find('input', {'name': 'state'})

    # Fill in the input fields with person's data
    email_input['value'] = person['email']
    fullname_input['value'] = person['full_name']
    country_input['value'] = person['country']
    state_input['value'] = person['state']

    # Prepare the form data for registration
    form_data = {
        'email': person['email'],
        'full_name': person['full_name'],
        'country': person['country'],
        'state': person['state']
    }

    # Send a POST request with the registration data to the correct form action URL
    action_url = soup.find('form')['action']  # Get the form's action URL
    registration_url = f"https://healingstreams.tv/submit_registration"  # Build the complete URL
    response = session.post(registration_url, data=form_data)

    if response.status_code == 200:
        # Log a success message if registration is successful
        logging.info(f"Registered {person['email']} successfully!")
    else:
        # Log an error if registration fails
        logging.error(f"Registration failed for {person['email']}")

# Close the session to release resources
session.close()
