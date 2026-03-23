# 🚗 AI Driver Monitoring System

This project is a real-time driver monitoring system built using computer vision.
It detects driver fatigue, drowsiness, yawning, and distraction, and provides live feedback through a dashboard along with alerts.

The system is designed to simulate a real-world driver safety solution and has been containerized using Docker for easy deployment.

---

## 🚀 What This Project Does

* Monitors driver behavior in real-time using webcam input
* Detects eye closure (drowsiness) and yawning
* Tracks head movement to identify distraction
* Calculates a fatigue score based on multiple factors
* Sends live updates to a web dashboard
* Triggers alerts when unsafe conditions are detected
* Captures screenshots and records video during critical situations

---

## 🧠 Core Logic (Simple Explanation)

* If eyes remain closed for a certain duration → system marks as **drowsy**
* If mouth is open frequently → system detects **yawning**
* If head is not facing forward → system detects **distraction**
* Based on all signals → a **fatigue score** is calculated
* If score crosses threshold → alert is triggered

---

## 🖥️ Dashboard

The system includes a web-based dashboard that shows:

* Live video feed
* Current driver status (Awake / Drowsy / Distracted)
* Fatigue score
* Event logs

---

## 🛠️ Tech Used

* Python
* OpenCV
* MediaPipe
* NumPy, SciPy
* Flask (for dashboard & APIs)
* Docker & Docker Compose

---

## 📦 Project Structure

```id="proj_struct"
driver-monitoring-system/
│
├── app/
│   ├── api/            # Flask backend
│   ├── detection/      # Drowsiness & head pose logic
│   ├── services/       # Alerts, recording, behavior tracking
│   └── config.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run (Docker)

```bash id="clone_cmd"
git clone https://github.com/omugale21/ai-driver-monitoring-system.git
cd ai-driver-monitoring-system
```

```bash id="run_cmd"
docker compose up --build
```

Then open:

```text id="open_link"
http://localhost:5000
```

---

## ⚠️ Notes

* The system uses your local webcam
* Works best on Linux environments
* When running in Docker, video is shown via dashboard (not popup window)
* Voice alerts may be limited in container environments

---

## 🎥 Demo

I will be adding a demo video and screenshots soon.

---

## 🔮 Future Improvements

* Cloud-compatible version (upload-based demo)
* Better fatigue scoring model
* Mobile/edge deployment
* API-based integration

---

## 📌 Final Thoughts

This project helped me understand:

* Real-time computer vision pipelines
* System design for AI applications
* Docker-based deployment
* Building a complete end-to-end application (not just a model)
