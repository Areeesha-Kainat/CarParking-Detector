import streamlit as st
import cv2
import pickle
import numpy as np

st.title("Car Parking Space Detector")

# Load saved parking positions
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

# Load Video
video_path = "CarParkingOutput.mkv"  # Replace with your actual video file path
cap = cv2.VideoCapture(video_path)

# Streamlit video display
stframe = st.empty()  # Placeholder for video frames

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Draw Parking Boxes
    for pos in posList:
        cv2.rectangle(frame, pos, (pos[0] + 107, pos[1] + 48), (255, 0, 255), 2)

    stframe.image(frame, channels="RGB")

cap.release()
