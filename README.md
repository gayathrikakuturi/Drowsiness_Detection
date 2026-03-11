# 🚗 Driver Drowsiness Detection System

A **real-time driver monitoring system** built using **Python, OpenCV, and MediaPipe FaceMesh** that detects driver fatigue by analyzing eye closure, blink patterns, and yawning behavior.
If drowsiness is detected, the system triggers an **audio alert** to warn the driver.

---

# 🧠 Features

* 👁️ **Eye Aspect Ratio (EAR)** based eye closure detection
* 😴 **Driver status detection** (Alert / Drowsy / Sleepy)
* 👁️‍🗨️ **Blink counter**
* 😮 **Yawn detection using mouth landmarks**
* 🔔 **Audio alert when driver becomes sleepy**
* 📷 **Real-time webcam monitoring**

---

# 🛠️ Technologies Used

* 🐍 Python
* 🎥 OpenCV
* 🤖 MediaPipe FaceMesh
* 🔢 NumPy
* 🔊 Winsound (alarm sound)

---

# ⚙️ Pre-Requisites

Make sure Python is installed.

Check version:

```bash
python --version
```

Install required modules:

```bash
pip install mediapipe==0.10.9
pip install opencv-python==4.9.0.80
pip install numpy==1.26.4
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

# 📁 Project Structure

```
Driver-Drowsiness-Detection
│
├── detection.py        # Main program
├── music.wav           # Alarm sound file
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

---

# ▶️ How to Run the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/driver-drowsiness-detection.git
```

Navigate to the project folder:

```bash
cd driver-drowsiness-detection
```

Run the program:

```bash
python detection.py
```

Press **Q** to exit the program.

---

# 🖥️ Output

When the system runs, the webcam opens and displays real-time driver monitoring information.

Example output on screen:

```
EAR: 0.29
Blinks: 12
Yawns: 2
STATUS: ALERT
```

Driver status levels:

| Status    | Condition                                         |
| --------- | ------------------------------------------------- |
| 🟢 ALERT  | Eyes open normally                                |
| 🟡 DROWSY | Eye closure detected                              |
| 🔴 SLEEPY | Eyes closed for multiple frames (alarm triggered) |

If the driver becomes **sleepy**, the system will play **music.wav** as an alert sound.

---

# ⚠️ Privacy Note

Screenshots or demo videos are not included to maintain privacy since the system processes **live webcam input**.

---

# 📌 Future Improvements

Possible extensions for this project:

* 📊 Driver fatigue analytics dashboard
* 📂 Event logging system
* 🌐 Web interface using Flask
* 🚘 Integration with vehicle safety systems

---

# 👨‍💻 Author

**Kakuturi Gayathri**

This project was developed as part of a **Computer Vision and AI portfolio project** using Python, OpenCV, and MediaPipe.

