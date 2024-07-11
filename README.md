# Attendance Tracking System

This is a Python script for a real-time attendance tracking system that uses face recognition to identify and log attendance of known students in a classroom or other environment.

## **Requirements**

The following modules are required to run this script:

- **`face_recognition`**
- **`cv2`**
- **`numpy`**
- **`csv`**
- **`datetime`**

## **How it works**

The script first loads images of known students and encodes their faces. It then creates a list of all known face encodings and corresponding names. A copy of this list is also created for tracking attendance.

Next, the script starts an infinite loop for video streaming and processing. It captures a frame from the video and resizes it for faster processing. It then detects faces in the frame and encodes their faces. For each detected face, it compares the face encoding with the known face encodings and finds the best match. If there is a match with any known face, it assigns the name of the known face to the current face. If the recognized face is a known student, it marks them as present and logs their attendance in a CSV file with the current date as the name. If the recognized face is not a known student, it adds a red text label to the frame.

The script also displays the video stream with text labels for recognized faces. If the 'q' key is pressed, the while loop is broken and the video capture is released.

## **How to use**

1. Clone this repository to your local machine.
2. Install the required modules using **`pip install -r requirements.txt`**.
3. Create a folder called **`Images`** in the same directory as the script and add images of known students to it.
4. Run the script using **`python attendance_system.py`**.
5. Ensure that your webcam is connected and working properly.
6. The script will start detecting faces in the video stream and marking attendance for known students. The attendance log will be saved in a CSV file with the current date as the name.
7. Press the 'q' key to stop the script and release the video capture.

## **Notes**

- This script is designed to work with a single camera input.
- The script can be modified to include more known students by adding their images and encodings to the code.
- The script assumes that all known students are present at the beginning of the session.

## **Contributing**

If you'd like to contribute to this project, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, feature requests, and documentation improvements.
