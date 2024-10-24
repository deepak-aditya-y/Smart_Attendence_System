# **Smart Attendance System using Face Recognition**

A real-time **face recognition-based attendance system** that identifies students using their facial features and automatically updates their attendance in a **Firebase database**. The system leverages **OpenCV, Face Recognition library, Firebase Realtime Database, and Cloud Storage** for seamless operations.

---

## **Features**
- **Face Recognition**: Detects and identifies registered students in real-time.
- **Attendance Management**: Updates attendance records in **Firebase** with timestamped entries.
- **Cloud Integration**: Stores student data and images on **Firebase Realtime Database** and **Cloud Storage**.
- **Dynamic UI**: Displays student information along with attendance status on a custom GUI interface.
- **Encoding Support**: Generates and saves facial encodings for fast and efficient recognition.

---

## **Prerequisites**

1. **Python 3.x** installed  
2. Create a Firebase project:
   - Enable **Realtime Database** and **Storage**.
   - Download the **`serviceAccountKey.json`** file for authentication.
3. **Dependencies**: Install the required Python libraries using:
   ```bash
   pip install opencv-python face-recognition firebase-admin numpy cvzone
