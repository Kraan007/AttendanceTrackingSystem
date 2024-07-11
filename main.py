# Importing required modules
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Creating a video capture object
video_capture = cv2.VideoCapture(0)

# Loading images of known people and encoding their faces
kiran_image = face_recognition.load_image_file("Images/2021PE0505.png")
kiran_encoding = face_recognition.face_encodings(kiran_image)[0]

arsh_image = face_recognition.load_image_file("Images/2021PE0174.png")
arsh_encoding = face_recognition.face_encodings(arsh_image)[0]

karan_image = face_recognition.load_image_file("Images/2021PE0621.png")
karan_encoding = face_recognition.face_encodings(karan_image)[0]

abhijeet_image = face_recognition.load_image_file("Images/2021PE0609.jpg")
abhijeet_encoding = face_recognition.face_encodings(abhijeet_image)[0]

haris_image = face_recognition.load_image_file("Images/2021PE0668.jpg")
haris_encoding = face_recognition.face_encodings(haris_image)[0]

# Creating a list of all known face encodings and corresponding names
known_face_encoding = [
    kiran_encoding,
    arsh_encoding,
    karan_encoding,
    abhijeet_encoding,
    haris_encoding
]

known_faces_names = [
    "Kiran",
    "Arsh",
    "Karan",
    "Abhijeet",
    "Haris"
]

# Creating a copy of the list of known face names
students = known_faces_names.copy()

# Initializing variables for face detection and recognition
face_locations = []
face_encodings = []
face_names = []
s = True
unknown_label = "Unknown"

# Getting current date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Creating a CSV file with current date as the name and opening it for writing
f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)

# Starting an infinite loop for video streaming and processing
while True:
    _, frame = video_capture.read()
    # Resizing the frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Detecting faces in the frame and encoding their faces
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        # Looping through all detected face encodings and finding the best match
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            # If there is a match with any known face, assign the name of the known face to the current face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_faces_names[first_match_index]
            else:
                name = unknown_label

            face_names.append(name)

            # If the recognized face is a known face, mark it as present and log attendance
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name + ' Present',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

                # If the recognized face is a student, remove their name from the students list and log attendance
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

            # If the name of the recognized face is unknown, add a red text label to the frame
            elif name == unknown_label:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (0, 0, 255)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name,
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

    cv2.imshow("SmartCheckIn", frame)

    # If the 'q' key is pressed, the while loop is broken and the video capture is released
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()