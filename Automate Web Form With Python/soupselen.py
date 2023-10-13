import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import json

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load registration data from a JSON file
with open("details.json", 'r') as json_file:
    data = json.load(json_file)

# Define the registration URL
registration_url = "https://healingstreams.tv/LHS/online_reg.php?r=GYLFWARRI"  # Update to the correct URL

# Create a Selenium WebDriver for your preferred browser
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to your Chrome driver

# Navigate to the registration URL
driver.get(registration_url)

# Iterate through the registration data for each person
for person in data:
    try:
        # Find the input field and submit button using Selenium
        my_details_input = driver.find_element_by_name("my_details")  # Update with the correct field name
        submit_button = driver.find_element_by_name("email_check")

        # Check if the input field was found
        if my_details_input:
            my_details_input.send_keys(person['email'])
            submit_button.send_keys(Keys.RETURN)
        else:
            logging.error(f"Input field 'my_details' not found for {person['email']}")
            continue

        # Log a success message if registration is successful
        logging.info(f"Registered {person['email']} successfully!")

    except NoSuchElementException as e:
        # Log an error if there's an issue and continue to the next person
        logging.error(f"Error during registration for {person['email']}: {e}")
        continue

# Close the Selenium WebDriver
driver.quit()
