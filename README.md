# 🚗 Driver Fatigue Detection System (AI-Based)

This project is an AI-powered real-time system designed to detect driver fatigue using computer vision techniques. It identifies signs of drowsiness and yawning and triggers alerts to improve driving safety.

---

## 🚀 Features

* Real-time face detection using dlib
* Eye Aspect Ratio (EAR) based drowsiness detection
* Mouth Aspect Ratio (MAR) based yawning detection
* Intelligent alert system with sound notification
* Smooth and stable UI (no flickering)
* Threaded webcam stream for better performance
* FPS display for performance monitoring

---

## 🧠 How It Works

1. Webcam captures live video frames
2. Facial landmarks are detected using dlib
3. Eye Aspect Ratio (EAR) is calculated to detect eye closure
4. Mouth Aspect Ratio (MAR) is calculated to detect yawning
5. System applies smoothing and frame-based logic
6. If fatigue is detected → alert is triggered

---

## 🔊 Detection Logic

* **Eyes Closed → Drowsiness**
* **Mouth Open → Yawning**
* **Both Conditions → Strong Alert 🚨**

---

## 🛠️ Technologies Used

* Python
* OpenCV
* dlib
* NumPy
* SciPy

---

## 📦 Project Structure

```
driver-drowsiness-detection/
│
├── main.py
├── alarm.mp3
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/omugale21/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download Model File

Download the facial landmark model:

http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Extract and place the `.dat` file in the project root folder.

---

### 4️⃣ Install Audio Dependency

```bash
sudo apt install mpg123
```

---

### 5️⃣ Run the Project

```bash
python main.py
```

---

## ⚠️ Note

* This project is designed for local systems with webcam support
* Real-time webcam functionality may not work in browser-based deployments

---

## 🔮 Future Improvements

* Head pose estimation
* Driver identity recognition
* Fatigue score calculation
* Mobile / embedded deployment
* Web-based demo interface

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub and share it!

