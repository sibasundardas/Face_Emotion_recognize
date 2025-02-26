# Face_Emotion_recognize
## Overview
This project is a Face Emotion Recognition system that uses a pre-trained model to detect and classify emotions from facial expressions.

## How to Run
To run the application, simply execute the `app.py` file. The pre-trained model will be loaded automatically, and the system will start recognizing emotions from the input images or video feed.

```bash
python app.py
```

## Requirements
Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- TensorFlow/Keras
- NumPy

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Pre-trained Model
The pre-trained model is included in the repository. It has been trained on a dataset of facial expressions and is capable of recognizing the following emotions:
- Happy
- Sad
- Angry
- Surprised
- Neutral
- Disguisted
- Fear

## Usage
Once the application is running, it will start capturing video from your webcam. The system will detect faces in the video feed and classify the emotions in real-time.

## License
This project is licensed under the MIT License.

## Acknowledgements
- The pre-trained model is based on the [FER2013 dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data).
- Special thanks to the contributors of the open-source libraries used in this project.
