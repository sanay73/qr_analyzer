QR Security Analyzer 🛡️

A Python-based cybersecurity tool that scans QR codes and checks URLs for suspicious signs before opening them.

Features

- Scan QR codes using a webcam.
- Scan QR codes from images.
- Extract QR code content.
- Check HTTPS usage.
- Detect IP-based URLs.
- Identify URL shorteners.
- Detect suspicious URL patterns.
- Calculate a basic risk score.

Requirements

- Kali Linux or another supported Linux system.
- Python 3.
- Git.
- pip.
- Webcam (optional).
- QR code image (optional).

Installation Steps

Step 1: Update Kali Linux

sudo apt update

Step 2: Install required packages

sudo apt install git python3 python3-pip python3-venv -y

Step 3: Clone the GitHub repository


git clone https://github.com/sanay73/qr_analyzer.git

Step 4: Enter the project folder

cd qr-Analyzer

Step 5: Create a virtual environment

python3 -m venv venv

Step 6: Activate the virtual environment

source venv/bin/activate

Step 7: Upgrade pip

python -m pip install --upgrade pip

Step 8: Install OpenCV

python -m pip install opencv-python

Step 9: Check OpenCV installation

python -c "import cv2; print(cv2.__version__)"

Step 10: Run the project

Use the filename that exists in your project folder.

python3 qr_analyzer.py

If your main Python file has a different name, replace "qr_analyzer.py" with that filename.

How to Use

1. Start the program.
2. Select webcam scanning or image scanning.
3. Allow camera access if prompted.
4. Scan a QR code or enter an image path.
5. View the decoded content.
6. Review the security findings and risk score.

Example Image Path

/home/kali/Downloads/test.png

Security Checks

Check| Purpose
HTTPS| Checks whether the URL uses HTTPS.
IP-based URL| Detects URLs using an IP address.
URL shortener| Identifies selected shortening services.
Suspicious patterns| Flags selected suspicious characters.
Keywords| Checks for words such as login or password.
Risk score| Estimates risk using basic rules.

Important Security Notes

- Do not open suspicious links.
- HTTPS does not guarantee that a website is safe.
- A low risk score does not guarantee safety.
- This tool uses basic checks and may produce false positives.
- The tool should inspect QR content without automatically opening URLs.

Technologies Used

- Python 3
- OpenCV
- Regular expressions
- IP address validation
- URL parsing

Project Structure

QR-Security-Analyzer/
├── qr_analyzer.py
├── requirements.txt
├── README.md
└── venv/

Your actual files may differ. Do not upload the "venv/" folder to GitHub.

Disclaimer

This project is for educational and defensive cybersecurity purposes only. Use it responsibly.
