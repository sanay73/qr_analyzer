# 🛡️ QR Security Analyzer

A Python-based cybersecurity tool that scans QR codes using a webcam or image file and analyzes embedded URLs for potentially suspicious characteristics.

The tool helps users inspect QR code contents before visiting a website.

## ✨ Features

* 📷 Scan QR codes directly using a webcam
* 🖼️ Scan QR codes from image files
* 🔗 Decode embedded QR data
* 🔒 Check HTTPS usage
* 🌐 Detect IP-address-based URLs
* 🔀 Identify known URL shorteners
* ⚠️ Detect suspicious URL characters and patterns
* 🔍 Check security-related keywords
* 📊 Generate a heuristic security score
* 🚨 Classify results as SAFE, SUSPICIOUS, or HIGH RISK
* 💻 Run directly from the terminal

## 🧰 Technologies Used

* Python 3
* OpenCV
* `re`
* `ipaddress`
* `urllib.parse`

## 📋 Requirements

* Python 3
* OpenCV Python package
* A webcam for direct scanning, or an image containing a QR code

## 🚀 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd qr-security-analyzer
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required package:

```bash
python3 -m pip install opencv-python
```

## ▶️ Run the Tool

```bash
python3 qr_security_analyzer.py
```

## 🖥️ Usage

After starting the tool, select an option from the menu:

```text
========================================
         QR SECURITY ANALYZER
========================================

1. Scan QR using Camera
2. Scan QR from Image
3. Exit

Select option:
```

### Camera Scanning

1. Select option `1`.
2. Show a QR code to your webcam.
3. The tool extracts the QR data.
4. Review the security analysis in the terminal.

### Image Scanning

1. Select option `2`.
2. Enter the path to your QR image.
3. The tool decodes the QR content.
4. Review the analysis results.

## 📊 Security Analysis

The tool checks URL characteristics such as:

* HTTPS usage
* IP-address-based URLs
* Known URL shorteners
* Suspicious characters
* Security-related keywords
* URL encoding



## 🔐 Security Notice

* The tool does not automatically open decoded URLs.
* HTTPS does not guarantee that a website is trustworthy.
* Legitimate URLs can trigger warnings.
* A high score does not guarantee that a website is safe.
* The tool uses basic heuristic checks and does not replace professional threat-intelligence services.

## 🎯 Project Objective

The objective of this project is to demonstrate defensive cybersecurity techniques through QR decoding, URL inspection, suspicious-pattern detection, and risk assessment.



## 👨‍💻 Author

Created as a cybersecurity learning project.
