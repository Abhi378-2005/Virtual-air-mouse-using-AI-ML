# 🖱️ AI Virtual Mouse using Hand Gestures

A computer vision project that allows you to control your mouse cursor using hand gestures. Built with Python, OpenCV, and MediaPipe.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-green)
![MediaPipe](https://img.shields.io/badge/Library-MediaPipe-orange)

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)

## 🧐 About the Project
This project eliminates the need for a physical mouse by tracking hand landmarks via a webcam. It detects the hand, tracks the index finger to move the cursor, and recognizes specific gestures (like pinching) to perform clicks. It is designed as an intermediate-level Machine Learning application.

## 🚀 Features
- **Real-time Hand Tracking:** Uses MediaPipe to detect hands with low latency.
- **Cursor Control:** Maps the index finger's position to the computer screen.
- **Clicking Mechanism:** Simulates a mouse click when the Index Finger and Thumb touch.
- **Smoothened Movement:** (Optional) Reduces cursor jitter for better usability.

## 🛠️ Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV (`cv2`)
- **Hand Tracking:** Google MediaPipe
- **Automation:** PyAutoGUI

---

## 💻 Installation & Setup

This project uses batch scripts to make setup incredibly easy.

### Prerequisites
- Python installed on your system.
- A webcam.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Virtual-AI-Mouse.git](https://github.com/YOUR_USERNAME/Virtual-AI-Mouse.git)
cd Virtual-AI-Mouse