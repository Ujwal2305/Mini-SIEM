# Mini SIEM: Log-Based Threat Detection

A lightweight SIEM (Security Information and Event Management) system built using Flask that detects and visualizes cyber threats from log data. It simulates real-world SOC workflows including threat detection, alerting, and MITRE ATT&CK mapping.

---

## Features

* Real-time dashboard with alerts and attack visualization
* Detection of brute force, SQL injection, XSS, and scanning attacks
* MITRE ATT&CK mapping of detected threats
* Log parsing and monitoring
* Alerts filtering by severity

---

## Tech Stack

* Python (Flask)
* HTML, CSS, JavaScript
* Chart.js

---

## Setup

```bash
git clone https://github.com/yourusername/mini-siem.git
cd mini-siem
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

---

## Run Simulator

```bash
python simulator/attack_simulator.py
```

---

## Keywords

SIEM, SOC, Threat Detection, Log Analysis, Intrusion Detection, MITRE ATT&CK, Brute Force, SQL Injection, XSS, Reconnaissance, Cybersecurity
