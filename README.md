# 🚗 AI Driver Monitoring System (Real-Time)

An advanced **AI-powered Driver Monitoring System** that detects **drowsiness, yawning, and driver distraction** in real-time using computer vision and intelligent alert mechanisms.

This system enhances driving safety by providing **multi-level alerts, voice feedback, and attention tracking**.

---

## 🚀 Key Features

* 👁️ **Drowsiness Detection** using Eye Aspect Ratio (EAR)
* 😮 **Yawning Detection** using Mouth Aspect Ratio (MAR)
* 🧠 **Attention Monitoring** (Head Pose + Face Position)
* 🔊 **Smart Voice Alerts** (Text-to-Speech)
* 🚨 **Multi-Level Alert System** (Warning → Critical)
* ⏱️ **Cooldown Mechanism** (Prevents alert spam)
* 🎥 **Real-Time Video Streaming Dashboard (Flask)**
* ⚡ **Threaded Camera for High Performance**
* 📊 **Fatigue Score Visualization (Backend Ready)**

---

## 🧠 System Architecture

```text
Webcam → Face Mesh → Landmark Detection → 
EAR / MAR / Attention → Decision Engine → 
Voice Alert + Alarm → Dashboard
```

---

## 🔍 Detection Logic

### 👁️ Drowsiness

* Eyes closed for consecutive frames → **DROWSY**

### 😮 Yawning

* Mouth open beyond threshold → **YAWNING**

### 👀 Attention Tracking

* Face center (nose position) detects:

  * Looking Left / Right
  * Looking Up / Down
  * Focused state

---

## 🔔 Smart Alert System

| Condition         | Alert                         |
| ----------------- | ----------------------------- |
| Slight fatigue    | 🔊 "Stay alert"               |
| Drowsy            | 🔊 Voice + 🚨 Alarm           |
| Not focused       | 🔊 "Please focus on the road" |
| Continuous drowsy | 🚨 Strong alert               |

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* SciPy
* Flask (Dashboard)
* pyttsx3 (Voice Alerts)

---

## 📂 Project Structure

```
ai-driver-monitoring-system/
│
├── app/
│   ├── detection/
│   ├── services/
│   ├── api/
│   └── frontend/
│
├── main.py
├── alarm.mp3
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/omugale21/ai-driver-monitoring-system.git
cd ai-driver-monitoring-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Audio Dependency

```bash
sudo apt install mpg123
```

---

### 4️⃣ Run Backend Server

```bash
python -m app.api.app
```

---

### 5️⃣ Run Main Application

```bash
python -m app.main
```

---

## 🎯 Use Cases

* 🚗 Driver safety systems
* 🏭 Fleet monitoring
* 🚕 Taxi driver monitoring
* 🧪 AI/ML research projects

---

## 🔮 Future Enhancements

* 📊 Fatigue Score System (0–100)
* 🎥 Event-based video recording
* ☁️ Cloud logging & analytics
* 📱 Mobile deployment
* 🤖 Deep learning-based fatigue prediction

---

🔥 This project demonstrates a **real-world AI safety system** combining computer vision, real-time processing, and intelligent alert mechanisms.
