from flask import Flask, render_template, Response, request
import os
import signal
import cv2
from keras.models import model_from_json
import numpy as np

app = Flask(__name__)

# Load the model
json_file = open("emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("emotiondetector.h5")

# Load Haar Cascade for face detection
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Emotion labels
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

def generate_frames():
    webcam = cv2.VideoCapture(0)
    while True:
        # Read the frame from webcam
        success, im = webcam.read()
        if not success:
            break

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (p, q, r, s) in faces:
            face = gray[q:q + s, p:p + r]
            face_resized = cv2.resize(face, (48, 48))
            img = extract_features(face_resized)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]

            # Draw rectangle and put emotion label
            cv2.rectangle(im, (p, q), (p + r, q + s), (255, 0, 0), 2)
            cv2.putText(im, prediction_label, (p - 10, q - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    webcam.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/camera')
def camera():
    return render_template('camera.html')


@app.route('/shutdown', methods=['POST'])
def shutdown():
    if request.method == 'POST':
        os.kill(os.getpid(), signal.SIGINT)  # Gracefully stop the Flask server
    return "Server shutting down..."

if __name__ == "__main__":
    app.run(debug=True)
