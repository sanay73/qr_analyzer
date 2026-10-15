QR Security Analyzer 🔐

A Python-based cybersecurity tool that scans QR codes and analyzes embedded URLs for potentially suspicious or unsafe characteristics.

🚀 Features

- QR Code Scanning: Scan QR codes using a webcam.
- Image-Based Scanning: Decode QR codes from saved image files.
- URL Security Analysis: Inspect decoded URLs for common warning signs.
- HTTPS Check: Identify whether a URL uses HTTPS.
- IP Address Detection: Flag URLs that use an IP address instead of a domain name.
- URL Shortener Detection: Identify known URL-shortening services.
- Suspicious Pattern Detection: Check for suspicious characters and keywords.
- URL Encoding Detection: Identify encoded URL content that may warrant closer inspection.
- Risk Scoring: Calculate a risk score based on detected indicators.
- Command-Line Interface: Run the tool directly from a terminal.

«Disclaimer: This tool provides heuristic analysis, not a guarantee that a URL is safe or malicious. Always verify suspicious links before opening them.»

🛠️ Technologies Used

- Python 3
- OpenCV ("cv2")
- QR code decoding libraries
- URL parsing and validation
- Regular expressions

📋 Requirements

- Python 3
- pip
- A webcam for live scanning
- Kali Linux or another compatible operating system

⚙️ Installation

1. Clone the repository

git clone https://github.com/sanay73/qr_analyzer.git
cd qr_analyzer

2. Create a virtual environment

python3 -m venv venv

3. Activate the virtual environment

source venv/bin/activate

4. Install dependencies

If the project contains a "requirements.txt" file:

pip install -r requirements.txt

If it doesn't, install the dependencies specified by your Python source code. For example, if your tool uses OpenCV:

pip install opencv-python

▶️ Usage

Run the main Python script using the filename in your project. For example:

python3 qr_analyzer.py

If your script supports command-line options for image scanning or camera selection, use the options implemented in your version.

🔍 How It Works

1. The tool reads a QR code from a webcam or image.
2. It extracts the encoded text or URL.
3. It parses the URL and checks selected security indicators.
4. It calculates a heuristic risk score.
5. It displays the analysis results in the terminal.

🛡️ Security Notes

- Do not open suspicious URLs just to test them.
- HTTPS does not guarantee that a website is trustworthy.
- A low risk score does not guarantee that a URL is safe.
- Risk scores are indicators for further investigation, not definitive verdicts.
- Test only with QR codes and systems you are authorized to analyze.

🗺️ Roadmap

- Improve URL reputation checks.
- Add more QR image formats and error handling.
- Improve risk scoring and reporting.
- Add unit tests for URL analysis.
- Add optional report export functionality.

🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome. Please test changes before submitting a pull request.

📄 License

Choose and add an appropriate open-source license before distributing this project.

---

Developed as a cybersecurity learning project.
