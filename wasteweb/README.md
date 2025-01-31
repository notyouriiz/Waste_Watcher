## Overview
The Waste_Watcher project is a web application designed to monitor and detect waste in water bodies using advanced object detection techniques. Built with Django and powered by the YOLO (You Only Look Once) model, this application provides real-time video feeds and notifications regarding waste accumulation, aiming to assist in environmental conservation efforts.

## Features
- **Real-Time Object Detection**: Utilizes YOLOv8 to identify various types of waste in video streams.
- **Django Web Framework**: A robust framework for building web applications, ensuring scalability and maintainability.
- **User-Friendly Interface**: Provides an intuitive interface to view live video feeds and receive alerts about waste levels.
- **Threshold Notifications**: Alerts users when the amount of detected waste exceeds a predefined limit.
- **Video Processing**: Processes video files to highlight detected objects and save annotated outputs.

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **OpenCV**: A library for computer vision tasks, used for video processing.
- **YOLO (Ultralytics)**: A state-of-the-art object detection model that identifies objects in images and videos.

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/notyouriiz/Waste_Watcher.git
   cd Waste_Watcher/WasteWeb
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install django opencv-python ultralytics
   ```

3. **Download YOLO Weights**:
   Ensure you have the YOLO weights file (`final.pt`) in the appropriate directory as specified in your code.

4. **Run Database Migrations**:
   Set up the database by running migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Application**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   Access the application by navigating to `http://localhost:8000` in your web browser.

## File Structure
```plaintext
WasteWeb/
│
├── assets/                # Directory for storing logo and other image assets
│   
├── detect/                # Directory for storing machine learning models
│   
├── static/                # Directory for static files (CSS, JS)
│   
├── template/              # Directory for HTML templates and styling of the web application
│   
├── app.py                 # Main application file for running the Flask server (if applicable)
├── tempCodeRunnerFile.py  # Temporary code runner file (can be ignored)
├── test.mp4               # Sample video file for testing purposes
└── README.md              # Project documentation
```

## Usage
- Navigate to the home page to view the live video feed of monitored water bodies.
- Access the `/deteksi_sampah` endpoint to check the current trash count and receive notifications based on the threshold.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Thanks to Ultralytics for their YOLO implementation.
- OpenCV for providing essential tools for image and video processing.
- Django community for their robust framework that supports rapid development.

---

This README now includes detailed explanations of each folder within your `WasteWeb` project. Feel free to modify any sections or add more information as needed!
