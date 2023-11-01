import requests
import json
import os
import random
import lorem

# Create a list of user data with unique first and last names
user_data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "username": "john.doe",
        "password": "demopassword"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "username": "jane.smith",
        "password": "demopassword"
    },
    {
        "first_name": "Michael",
        "last_name": "Johnson",
        "username": "michael.johnson",
        "password": "demopassword"
    },
    {
        "first_name": "Emily",
        "last_name": "Brown",
        "username": "emily.brown",
        "password": "demopassword"
    },
    {
        "first_name": "William",
        "last_name": "Jones",
        "username": "william.jones",
        "password": "demopassword"
    },
    {
        "first_name": "Olivia",
        "last_name": "Miller",
        "username": "olivia.miller",
        "password": "demopassword"
    },
    {
        "first_name": "David",
        "last_name": "Wilson",
        "username": "david.wilson",
        "password": "demopassword"
    },
    {
        "first_name": "Ava",
        "last_name": "Davis",
        "username": "ava.davis",
        "password": "demopassword"
    },
    {
        "first_name": "James",
        "last_name": "Martinez",
        "username": "james.martinez",
        "password": "demopassword"
    },
    {
        "first_name": "Sophia",
        "last_name": "Lee",
        "username": "sophia.lee",
        "password": "demopassword"
    }
]

def register_demo_users(api_endpoint):
    # Loop through the user data and send POST requests
    for user in user_data:
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(user)

        # Send the POST request
        response = requests.post(api_endpoint, data=data, headers=headers)

        # Check the response status
        if response.status_code == 201:
            print(f"User '{user['username']}' registered successfully.")
        else:
            print(f"Failed to register user '{user['username']}' with status code: {response.status_code}")


def upload_post(api_endpoint, user_id):
    # Define the API endpoint URL
    url = api_endpoint + f'{user_id}/'

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the relative path to the image directory
    image_directory = os.path.join(script_directory, 'images')

    # List all image files in the directory
    image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Select a random image file
    random_image = random.choice(image_files)

    # Generate a random description
    description = lorem.paragraph()

    # Prepare the form data
    data = {
        'description': description,
    }

    # Read the selected image file
    with open(os.path.join(image_directory, random_image), 'rb') as image_file:
        files = {'image': (random_image, image_file, 'image/jpeg')}

        # Send the POST request with the form data and image
        response = requests.post(url, data=data, files=files)

    # Check the response status
    if response.status_code == 201:
        print(f"POST request successful. Description: {description}")
    else:
        print(f"Failed to send POST request. Status code: {response.status_code}")

def upload_posts(api_endpoint, startinguserid, numofusers=10, numofposts=[3, 7]):
    for user_id in range(startinguserid, startinguserid+numofusers):
        posts_to_upload = random.randint(numofposts[0], numofposts[1])
        for i in range(0, posts_to_upload):
            upload_post(api_endpoint, user_id)

### ----------------- Execution ------------------- ###


#register_demo_users('http://localhost:8000/demo_register/')
upload_posts('http://localhost:8000/demo_post/', 11)