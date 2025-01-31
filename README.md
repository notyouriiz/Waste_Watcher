# Waste Watcher: Intelligence Waste Control System

## Overview
The Waste Detection System is a web application built with Flask that utilizes the YOLO (You Only Look Once) model for real-time object detection. The primary objective of this project is to monitor water bodies, such as rivers, for trash accumulation. By detecting various types of waste, the application provides notifications when the amount of trash exceeds a predetermined threshold, thereby aiding in environmental conservation efforts.

## Features
- **Real-time Video Processing**: Streams video from a specified source and processes frames to detect trash.
- **Object Detection**: Utilizes the YOLOv8 model to identify specific trash categories (bottles, plastics, small waste).
- **Threshold Notifications**: Sends alerts when detected trash exceeds a set limit.
- **Web Interface**: Provides a user-friendly interface to view video feeds and notifications.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **OpenCV**: A library for computer vision tasks, used here for video processing.
- **YOLO (Ultralytics)**: A state-of-the-art object detection model that identifies objects in images and videos.
- **HTML/CSS**: For creating the web interface.

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/notyouriiz/Waste_Watcher.git
   cd Waste_Watcher
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install Flask opencv-python ultralytics
   ```

3. **Download YOLO Weights**:
   Make sure to download the YOLO weights file (`final.pt`) and place it in the appropriate directory as specified in the code.

4. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   Access the application by navigating to `http://localhost:5000` in your web browser.

## Usage
- Navigate to the home page to view the live video feed.
- Access the `/deteksi_sampah` endpoint to check the current trash count and receive notifications based on the threshold.

## Code Structure
```plaintext
waste-detection-system/
│
├── app.py                  # Main application file
├── templates/              # Directory for HTML templates
│   └── index.html          # Main HTML page
└── static/                 # Directory for static files (CSS, JS)
```

## Acknowledgements
- Thanks to Ultralytics for their YOLO model.
- OpenCV for providing powerful tools for image processing.
