## Overview
This project implements a YOLO (You Only Look Once) object detection system to identify and annotate waste in images and videos. It is designed to help monitor and manage waste in environments such as rivers and other water bodies, providing a visual representation of detected trash.

## Features
- **Object Detection**: Uses the YOLO model to detect and classify waste items in images and videos.
- **Image Processing**: Processes static images to highlight detected objects.
- **Video Processing**: Analyzes video files, annotating frames with bounding boxes around detected objects.
- **Output Generation**: Saves processed images and videos with annotated detections.

## Technologies Used
- **OpenCV**: A powerful library for computer vision tasks, used for image and video processing.
- **YOLO (Ultralytics)**: A state-of-the-art object detection model that identifies objects in images and videos.

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/notyouriiz/yolo-waste-monitoring.git
   cd yolo-waste-monitoring
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install opencv-python ultralytics
   ```

3. **Download YOLO Weights**:
   Make sure to have the `custom_best.pt` weights file in the `inference` folder.

4. **Run the Application**:
   Execute the `main.py` script to process your images or videos:
   ```bash
   python inference/main.py
   ```

## File Structure
```plaintext
waste_watcher/
│
├── inference/              # Directory containing inference files
│   ├── custom_best.pt      # YOLO model weights file
│   ├── main.ipynb          # Jupyter Notebook for interactive use (optional)
│   ├── main.py             # Main script for processing images/videos
│   ├── output_video.mp4    # Example output video (after processing)
│   └── vid1.mp4            # Input video for testing
└── README.md               # Project documentation
```

## Usage

### Processing Images
To process an image, uncomment the following line in `main.py` and specify your image path:
```python
# process_image('path_to_your_image.jpg', 'output_image.jpg')
```

### Processing Videos
The script is set up to process a video file named `vid1.mp4` located in the `inference` folder. The output will be saved as `output_video.mp4`. You can modify this section of the code if you want to process different videos:
```python
process_video('vid1.mp4', 'output_video.mp4')
```

### Viewing Results
After processing, check the specified output paths for annotated images or videos.

## Acknowledgements
- Thanks to Ultralytics for their YOLO implementation.
- OpenCV for providing essential tools for image and video processing.

---
