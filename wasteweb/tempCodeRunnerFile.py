from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import time

app = Flask(__name__)

# Load the YOLO model
model = YOLO("C:\\Samsung SFT 2024\\wasteweb_2\\detect\\train2\\weights\\final.pt")

# Variable to store the amount of detected trash
sampah = {"sampah_botol": 0, "sampah_plastik": 0, "sampah_kecil": 0}

# Threshold for the amount of trash
threshold = 10

# Detection interval timeout
detect_timeout = 10
last_detect_time = {}  # Detection per label


def gen_frames():
    cap = cv2.VideoCapture("C:\\Samsung SFT 2024\\wasteweb\\test.mp4")
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        else:
            # Detect objects using YOLOv8
            results = model(frame)
            current_time = time.time()

            # Loop through each result
            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    label = model.names[class_id]

                    # Process detection of trash categories
                    if "botol" in label.lower():
                        if (
                            label not in last_detect_time
                            or (current_time - last_detect_time[label]) > detect_timeout
                        ):
                            sampah["sampah_botol"] += 1
                            last_detect_time[label] = current_time
                    elif "plastik" in label.lower():
                        if (
                            label not in last_detect_time
                            or (current_time - last_detect_time[label]) > detect_timeout
                        ):
                            sampah["sampah_plastik"] += 1
                            last_detect_time[label] = current_time
                    elif "kecil" in label.lower():
                        if (
                            label not in last_detect_time
                            or (current_time - last_detect_time[label]) > detect_timeout
                        ):
                            sampah["sampah_kecil"] += 1
                            last_detect_time[label] = current_time

            # Annotate frame with detection results
            annotated_frame = result.plot()

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode(".jpg", annotated_frame)
            frame = buffer.tobytes()

            # Yield the frame as part of the video feed
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/deteksi_sampah")
def deteksi_sampah():
    total_sampah = sum(sampah.values())

    # Check if the total trash count exceeds the threshold
    if total_sampah > threshold:
        return jsonify(
            {
                "sampah_botol": sampah["sampah_botol"],
                "sampah_plastik": sampah["sampah_plastik"],
                "sampah_kecil": sampah["sampah_kecil"],
                "notifikasi": "Total sampah sudah melebihi batas, Segera lakukan pengambilan!",
            }
        )
    else:
        return jsonify(
            {
                "sampah_botol": sampah["sampah_botol"],
                "sampah_plastik": sampah["sampah_plastik"],
                "sampah_kecil": sampah["sampah_kecil"],
                "notifikasi": "Belum ada notifikasi.",
            }
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
