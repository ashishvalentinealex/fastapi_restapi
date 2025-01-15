FastAPI File Upload - Image/Video Processor
This project uses FastAPI to provide an endpoint for uploading images and videos. Depending on the file type, images will be saved directly into a specified folder, while videos will be processed by extracting each frame and saving the frames as individual images.

Features
Upload an image or video using a POST request.
If an image is uploaded, it is saved in a folder named after the provided name.
If a video is uploaded, each frame is extracted and saved as an image in the folder named after the provided name.
Supports multiple video formats like MP4, AVI, MOV, etc.
The server responds with a message confirming the file processing status.
Prerequisites
Before running this project, make sure you have the following installed:

Python 3.7+: Install Python from official website.
pip: Python's package manager (should come with Python).
FastAPI and Uvicorn: For serving the application.
OpenCV: For video frame extraction.
Install dependencies
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/fastapi-file-upload.git
cd fastapi-file-upload
Create a virtual environment (if not already done):

bash
Copy code
python3 -m venv fastapi_env
source fastapi_env/bin/activate  # On Windows, use `fastapi_env\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install fastapi uvicorn opencv-python requests
Run the Server
Once the dependencies are installed, you can start the FastAPI server using the following command:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
This will start the server on http://localhost:8000.

API Endpoint
POST /upload/
This endpoint allows you to upload a file (image or video) along with a name for the folder where the file will be saved.

Request:
name (form data): The name for the folder where the file will be stored (e.g., "ashish").
file (form data): The file to upload (image or video).
Response:
The server responds with a JSON message indicating whether the file was processed successfully.

json
Copy code
{
  "message": "File uploaded and processed under folder 'name'"
}
Example Request (using Python):
To upload a file using Python with the requests library, use the following script:

python
Copy code
import requests

# Replace these with your actual details
url = "http://localhost:8000/upload/"
name = "ashish"  # The name you want to give to the folder
file_path = "/path/to/your/file.mp4"  # Path to the video or image on your system

# Open the file in binary mode
with open(file_path, "rb") as file:
    # Create the multipart/form-data payload
    files = {'file': (file_path, file, 'video/mp4')}  # Adjust MIME type if needed (e.g., 'image/jpeg')
    data = {'name': name}

    # Send the POST request to the FastAPI server
    response = requests.post(url, data=data, files=files)

# Print the response from the server
print(response.status_code)
print(response.json())
Example Response:
json
Copy code
{
  "message": "File uploaded and processed under folder 'ashish'"
}
Folder Structure
The uploaded files will be saved in the uploads/ folder. The folder structure will look like this:

markdown
Copy code
uploads/
└── ashish/
    ├── frame_0.jpg
    ├── frame_1.jpg
    ├── uploaded_image.jpg
For videos, each frame will be saved as an image (frame_0.jpg, frame_1.jpg, etc.), while for images, they will be directly saved in the folder as-is.

How It Works
The FastAPI server listens for POST requests on the /upload/ endpoint.
Upon receiving a request, the server checks whether the file is an image or a video.
If the file is an image, it is saved with a unique name in the specified folder.
If the file is a video, the server extracts frames from the video and saves each frame as a separate image in the specified folder.
The server responds with a success message once the file is processed.
Run Tests
To test the functionality, you can use tools like Postman or Python requests to upload images or videos via POST requests to http://localhost:8000/upload/. Use the provided Python script to send video/image files to the server.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to open issues and pull requests for any bugs or enhancements. Contributions are always welcome!
