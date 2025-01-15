import requests

# Replace these with your actual details
url = "http://localhost:8000/upload/"
name = "ashish"  # The name you want to give to the folder
image_path = "/home/ashish/Downloads/messi_test.jpeg"  # Path to the image on your system

# Open the image file in binary mode
with open(image_path, "rb") as image_file:
    # Create the multipart/form-data payload
    files = {'file': (image_path, image_file, 'image/jpeg')}  # Adjust MIME type if needed (e.g., 'image/png')
    data = {'name': name}

    # Send the POST request to the FastAPI server
    response = requests.post(url, data=data, files=files)

# Print the response from the server
print(response.status_code)
print(response.json())
