import cv2
import face_recognition
import numpy as np
import pandas as pd
import os
from datetime import datetime

known_face_encodings = []
known_face_names = []
for filename in os.listdir('images'):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join('images', filename)
        person_image = face_recognition.load_image_file(image_path)
        person_face_encoding = face_recognition.face_encodings(person_image)[0]
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])

print("Known faces loaded successfully!")
print(f"Number of known faces: {len(known_face_names)}")
present_students = set()
video_capture = cv2.VideoCapture(0)

print("Starting video capture... Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break
    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) 
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        if name != "Unknown" and name not in present_students:
            present_students.add(name)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Attendance recorded for: {name} at {current_time}")
    frame = cv2.cvtColor(rgb_small_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('Face Detection Attendance System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
attendance_list = []
for name in present_students:
    attendance_list.append({
        'Name': name,
        'Date': datetime.now().strftime("%Y-%m-%d"),
        'Time': datetime.now().strftime("%H:%M:%S")
    })
if attendance_list:
    df = pd.DataFrame(attendance_list)
    filename = datetime.now().strftime("attendance_%Y-%m-%d.csv")
    df.to_csv(filename, index=False)
    print(f"\nAttendance data saved to {filename}")
else:
    print("\nNo attendance recorded. CSV file not created.")
video_capture.release()
cv2.destroyAllWindows()