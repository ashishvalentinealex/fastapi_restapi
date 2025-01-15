# FastAPI File Upload - Image/Video Processor

This project uses **FastAPI** to provide an endpoint for uploading images and videos. Depending on the file type, images will be saved directly into a specified folder, while videos will be processed by extracting each frame and saving the frames as individual images.

## Features
- Upload an **image** or **video** using a POST request.
- If an **image** is uploaded, it is saved in a folder named after the provided **name**.
- If a **video** is uploaded, each frame is extracted and saved as an image in the folder named after the provided **name**.
- Supports multiple video formats like **MP4**, **AVI**, **MOV**, etc.
- The server responds with a message confirming the file processing status.

## Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.7+**: Install Python from [official website](https://www.python.org/downloads/).
- **pip**: Python's package manager (should come with Python).
- **FastAPI** and **Uvicorn**: For serving the application.
- **OpenCV**: For video frame extraction.

### Install dependencies

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/fastapi-file-upload.git
cd fastapi-file-upload
```
## Run the Server
```bash 
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## How It Works
The FastAPI server listens for POST requests on the /upload/ endpoint.
Upon receiving a request, the server checks whether the file is an image or a video.
If the file is an image, it is saved with a unique name in the specified folder.
If the file is a video, the server extracts frames from the video and saves each frame as a separate image in the specified folder.
The server responds with a success message once the file is processed.

## Run Tests
To test the functionality, you can use tools like Postman or Python requests to upload images or videos via POST requests to http://localhost:8000/upload/. Use the provided Python script to send video/image files to the server.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to open issues and pull requests for any bugs or enhancements. Contributions are always welcome!
