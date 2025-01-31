import cv2
from ultralytics import YOLO

model = YOLO('custom_best.pt')

def detect_objects(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)
    
    # Accessing the first result from the results list
    boxes = results[0].boxes.xyxy.cpu().numpy()  # Bounding boxes
    confidences = results[0].boxes.conf.cpu().numpy()  # Confidences
    class_ids = results[0].boxes.cls.cpu().numpy()  # Class IDs

    labels = model.names  # Get the names from the model

    # Draw the bounding boxes
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        x1, y1, x2, y2 = box
        label = f"{labels[int(class_id)]} {confidence:.2f}"
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame


def process_image(image_path, output_path):
    frame = cv2.imread(image_path)
    result_frame = detect_objects(frame)
    cv2.imwrite(output_path, result_frame)
    print(f"Processed image saved at {output_path}")

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    # Use 'mp4v' codec for mp4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also try 'avc1' for H.264
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result_frame = detect_objects(frame)
        out.write(result_frame)
        cv2.imshow('Video', result_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Processed video saved at {output_path}")

if __name__ == "__main__":
    # For image
    # process_image('path_to_your_image.jpg', 'output_image.jpg')

    # For video
    process_video('vid1.mp4', 'output_video.mp4')  # Changed to .mp4
