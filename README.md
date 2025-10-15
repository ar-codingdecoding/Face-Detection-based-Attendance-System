# Face-Detection-based-Attendance-System

A simple, real-time attendance system built with Python that utilizes a webcam to detect and recognize faces. This project automates the attendance-taking process by comparing faces against a database of known individuals and logging attendance to a CSV file.

## Features

- **Real-time Face Detection:** Captures and processes live video from a webcam to detect faces.
- **Efficient Face Recognition:** Compares detected faces against a set of known individuals to confirm identity.
- **Automated Attendance Logging:** Records the name, date, and time of each recognized person to a structured CSV file.
- **Scalable:** Easily add new individuals to the system by simply placing their images in a dedicated folder.
- **User-friendly:** The system provides real-time feedback in the terminal and a clean visual output.

## Prerequisites

Before you run this project, ensure you have the following installed on your system:

- **Python 3.x:** This project is built and tested with Python 3.
- **Visual Studio Build Tools with C++ workload (for Windows users):** The `dlib` library, a core dependency, requires a C++ compiler to be built on Windows.
- **CMake:** A build tool required by `dlib` for compilation.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone [https://github.com/ar-codingdecoding/Face-Detection-based-Attendance-System.git](https://github.com/ar-codingdecoding/Face-Detection-based-Attendance-System.git)
cd Face-Detection-based-Attendance-System

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.\.venv\Scripts\activate
# On macOS / Linux:
source ./.venv/bin/activate

# Install Required Libraries
pip install opencv-python face_recognition numpy pandas
