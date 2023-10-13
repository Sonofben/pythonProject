import logging
import requests
from bs4 import BeautifulSoup
import json

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load registration data from a JSON file
with open("details.json", 'r') as json_file:
    data = json.load(json_file)

# Define the registration URL
registration_url = "https://healingstreams.tv/LHS/online_reg.php?r=GYLFWARRI"  # Update to the correct URL

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

    # Find the input fields for registration data
    my_details_input = soup.find('input', {'name': 'my_details'})  # Update with the correct field name
    submit_button = soup.find('input', {'name': 'email_check'})
    
    # Check if the input field was found
if my_details_input is not None:
    my_details_input['value'] = person['email']
else:
    logging.error(f"Input field 'my_details' not found for {person['email']}")
    # Fill in the input fields with person's data
    my_details_input['value'] = person['email']
    
    # Prepare the form data for registration
    form_data = {
        'my_details': person['email']
    }

    # Send a POST request with the registration data to the correct form action URL
    action_url = soup.find('form')['action']  # Get the form's action URL
    registration_url = f"https://healingstreams.tv/LHS/new_email_action.php?r=Online" # Use the action URL as the registration URL
    response = session.post(registration_url, data=form_data)

    if response.status_code == 200:
        # Log a success message if registration is successful
        logging.info(f"Registered {person['email']} successfully!")
    else:
        # Log an error if registration fails
        logging.error(f"Registration failed for {person['email']}")

# Close the session to release resources
session.close()
