<p align="center">
  <img src="banner.png" alt="Keylogger CSV Banner" width="800"/>
</p>

<h1 align="center">🔐 Keylogger CSV — Ethical Key Capture & Analysis Tool</h1>

<p align="center">
  <i>Developed by <b>Darshan Gholap</b> — B.Sc. Cyber & Digital Science</i><br>
  <i>MIT ACSC Alandi | Ethical Hacking • Cyber Defense • Python Security Tools</i>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green"></a>
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-lightgrey">
  <img src="https://img.shields.io/badge/Status-Stable-success">
</p>

---

## 🧠 About the Project

**Keylogger CSV** is a Python-based cybersecurity tool that records, analyzes, and visualizes keystroke activity for ethical research and security auditing.  
It’s designed for cybersecurity learners and professionals to study input patterns, session behavior, and event logging — **strictly for educational use only**.

---

## 🚀 Features

- 🎹 **Real-Time Key Logging** — Captures every keystroke with accurate timestamps.  
- 🧾 **CSV Export** — Automatically stores logs in structured CSV format.  
- 🕒 **Session Tracking** — Separates user activity by session/timeframe.  
- 📊 **Analysis Script** — `analyze_keylogs.py` provides summaries and insights.  
- 🧩 **Safe Exit Command** — Stop logging anytime with `Ctrl + Shift + S`.  
- 💻 **Cross-Platform** — Works on Windows, Linux, and macOS.  
- 🔒 **Ethical Design** — Built for research and educational environments.

---

## 🧰 Tech Stack

| Component | Description |
|------------|--------------|
| 🐍 Python 3.8+ | Core language for scripting |
| 🎹 pynput | Keyboard input listener |
| 📊 pandas | CSV parsing and data aggregation |
| 📈 matplotlib | Optional visualization support |

---

## ⚙️ Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Darshan-builds/keylogger_csv.git
cd keylogger_csv

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the keylogger
python keylogger_csv.py

# 5. Stop the keylogger safely
# Use Ctrl + Shift + S to stop logging and save CSV output

# 6. Analyze logged data
python analyze_keylogs.py keylogs/keylog.csv
📂 Folder Structure
bash
Copy code
keylogger-csv/
│
├── keylogger_csv.py          # Main keylogging script
├── analyze_keylogs.py        # Analysis and visualization script
├── keylogs/                  # Folder for stored CSV log files
│   └── keylog.csv
├── banner.png                # GitHub project banner
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
⚠️ Ethical Disclaimer
This project is developed solely for educational and research purposes.
Unauthorized use of keylogging software to monitor others without explicit consent is illegal and unethical.
Always use this tool responsibly in a controlled or consent-based environment only.

🔮 Future Enhancements
📊 Add live dashboard visualization.

🧠 Integrate AI-based keystroke pattern analysis.

☁️ Secure remote log transmission.

🔐 Encrypted local log storage.

🧩 Author
Darshan Gholap
🎓 B.Sc. Cyber & Digital Science | MIT ACSC Alandi
💼 Ethical Hacking • Digital Forensics • Cybersecurity Research

