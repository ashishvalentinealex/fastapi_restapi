import os
import cv2
import uuid
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil

app = FastAPI()

# Directory where files will be stored
BASE_UPLOAD_DIR = "/home/ashish/final_demo/face_recognition/face_recognition_by_pi/uploads"
os.makedirs(BASE_UPLOAD_DIR, exist_ok=True)

class SendData:
    @staticmethod
    def generate_unique_filename(prefix='', suffix=''):
        unique_id = str(uuid.uuid4())
        return f"{prefix}{unique_id}{suffix}"

    @staticmethod
    def extract_frames_from_video(video_path, output_folder, prefix="frame_", image_format="jpg"):
        """
        Extract frames from a video and save them as images.
        """
        try:
            cap = cv2.VideoCapture(video_path)
            frame_count = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_filename = f"{prefix}{frame_count}.{image_format}"
                frame_path = os.path.join(output_folder, frame_filename)
                cv2.imwrite(frame_path, frame)
                print(f"Saved frame: {frame_path}")
                frame_count += 1

            cap.release()
            return frame_count
        except Exception as e:
            print(f"Error while extracting frames: {e}")
            return 0

    def __init__(self, file_path, output_base_folder, name):
        # Create a folder based on the provided name
        output_folder = os.path.join(output_base_folder, name)
        os.makedirs(output_folder, exist_ok=True)

        # Check if the file is an image or video
        file_ext = os.path.splitext(file_path)[-1].lower()
        if file_ext in [".jpg", ".jpeg", ".png", ".bmp"]:
            # Handle image
            unique_file_name = self.generate_unique_filename(prefix="uploaded_", suffix=file_ext)
            output_path = os.path.join(output_folder, unique_file_name)
            shutil.move(file_path, output_path)
            print(f"Image moved to {output_path}")
        elif file_ext in [".mp4", ".avi", ".mov", ".mkv"]:
            # Handle video: extract frames
            frame_count = self.extract_frames_from_video(video_path=file_path, output_folder=output_folder)
            print(f"Extracted {frame_count} frames from video.")
            os.remove(file_path)  # Clean up the original video file after processing
        else:
            print(f"Unsupported file type: {file_ext}")


@app.post("/upload/")
async def upload_file(name: str = Form(...), file: UploadFile = None):
    if not file:
        return JSONResponse(content={"error": "No file provided"}, status_code=400)

    # Save the uploaded file temporarily
    temp_file_path = os.path.join(BASE_UPLOAD_DIR, file.filename)
    with open(temp_file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Process the file and organize it
    SendData(file_path=temp_file_path, output_base_folder=BASE_UPLOAD_DIR, name=name)

    return JSONResponse(content={"message": f"File uploaded and processed under folder '{name}'"})


@app.get("/")
async def root():
    return {"message": "Welcome to the file upload API!"}
