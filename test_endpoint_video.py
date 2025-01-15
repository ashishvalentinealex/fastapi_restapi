import requests

# Replace these with your actual details
url = "http://localhost:8000/upload/"
name = "ashish"  # The name you want to give to the folder
video_path = "/home/ashish/Downloads/WhatsApp Video 2025-01-15 at 11.51.21 AM.mp4"  # Path to the video on your system

# Open the video file in binary mode
with open(video_path, "rb") as video_file:
    # Create the multipart/form-data payload
    files = {'file': (video_path, video_file, 'video/mp4')}  # Adjust MIME type if needed (e.g., 'video/mkv')
    data = {'name': name}

    # Send the POST request to the FastAPI server
    response = requests.post(url, data=data, files=files)

# Print the response from the server
print(response.status_code)
print(response.json())
