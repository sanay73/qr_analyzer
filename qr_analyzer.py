
import cv2
import re
import ipaddress
from urllib.parse import urlparse, unquote

from colorama import Fore, Style, init


# =========================================================
# COLORAMA
# =========================================================

init(autoreset=True)


# =========================================================
# CUSTOM BANNER
# =========================================================

def banner():

    print(Fore.CYAN + r"""
▄█▓▓▒░███▄ ██▓▓▒░███▄      ▄█▓▓▒░███▄ █▓▄   █▓▒░ ▄█▓▓▒░███▄ ██▓▓       ██▓▓  ▓▒░█ █▓▒░████▄ ▄█▓▓▒░████ ██▓▓▒░███▄
▓▓▒▒  █░░█ ▓▓▒▒  █░░█      ▓▓▒▒  █ ██ ▓▒░█▄ ▓▒░█ ▓▓▒▒  █ ██ ▓▓▒▒       ▓▓▒▒  ▒░░█      █▓▓█ ▓▓▒▒  █▓▓█ ▓▓▒▒  █░░█
▒▒░░  █▒▒█ ▒▒░░█████▀      ▒▒░░██████ ▒░██▀░▒░▒█ ▒▒░░██████ ▒▒░░       ▀▒░░██░▒▒█ ▄▓▒░████▀ ▒▒░░█      ▒▒░░█████▀
░░██▀██▓▓▀ ░░██  █▒▒█      ░░██  █▓▓█ ░███  ░▓▓█ ░░██  █▓▓█ ░░██  █▓▓█ ▄▄▄▄  █▓▓  ▓▒░█      ░░██  █▒▒█ ░░██  █▒▒█
▀████▀████ ████  ████      ████  ████ ████  ████ ████  ████ ▀█████████ ▓▒░██████▀ ▀░████▓▒░ ▀██████▓▓█ ████  ████
""")

    print(
        Fore.CYAN +
        "                 QR SECURITY ANALYZER"
    )

    print(
        Fore.WHITE +
        "                 Version 1.0"
    )

    print(
        Fore.WHITE +
        "                 Defensive Security Tool"
    )

    print(Fore.CYAN + "=" * 70)


# =========================================================
# QR IMAGE DECODER
# =========================================================

def decode_image(image_path):

    image = cv2.imread(image_path)

    if image is None:

        print(
            Fore.RED +
            "\n[!] Error: Could not open image."
        )

        return None

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if data:

        return data

    return None


# =========================================================
# CAMERA QR SCANNER
# =========================================================

def scan_camera():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        print(
            Fore.RED +
            "\n[!] Camera could not be opened."
        )

        return None

    detector = cv2.QRCodeDetector()

    print(
        Fore.CYAN +
        "\n[*] Camera started."
    )

    print(
        Fore.YELLOW +
        "[*] Show a QR code to the camera."
    )

    print(
        Fore.YELLOW +
        "[*] Press Q to cancel."
    )

    while True:

        ret, frame = camera.read()

        if not ret:

            print(
                Fore.RED +
                "[!] Could not read camera."
            )

            break

        data, points, _ = detector.detectAndDecode(frame)

        cv2.imshow(
            "QR Security Scanner - Press Q to Exit",
            frame
        )

        # QR detected
        if data:

            camera.release()
            cv2.destroyAllWindows()

            return data

        # Press Q
        if cv2.waitKey(1) & 0xFF == ord("q"):

            break

    camera.release()

    cv2.destroyAllWindows()

    return None


# =========================================================
# URL DETECTION
# =========================================================

def is_url(data):

    return bool(
        re.match(
            r"^(https?://|www\.)",
            data,
            re.IGNORECASE
        )
    )


# =========================================================
# IP ADDRESS CHECK
# =========================================================

def check_ip(host):

    try:

        ipaddress.ip_address(host)

        return True

    except ValueError:

        return False


# =========================================================
# URL SHORTENER CHECK
# =========================================================

def check_shortener(host):

    shorteners = {

        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "ow.ly",
        "is.gd",
        "cutt.ly",
        "rb.gy",
        "shorturl.at",
        "buff.ly"

    }

    return host.lower() in shorteners


# =========================================================
# SUSPICIOUS CHARACTER CHECK
# =========================================================

def check_suspicious_characters(url):

    warnings = []

    if "@" in url:

        warnings.append(
            "@ symbol"
        )

    if "\\" in url:

        warnings.append(
            "Backslash"
        )

    if "%" in url:

        warnings.append(
            "URL encoding"
        )

    if url.count("-") >= 3:

        warnings.append(
            "Many hyphens"
        )

    return warnings


# =========================================================
# SUSPICIOUS KEYWORD CHECK
# =========================================================

def check_keywords(url):

    keywords = [

        "login",
        "signin",
        "verify",
        "verification",
        "account",
        "password",
        "secure",
        "update",
        "confirm",
        "payment",
        "wallet",
        "credential"

    ]

    found = []

    lower_url = url.lower()

    for keyword in keywords:

        if keyword in lower_url:

            found.append(keyword)

    return found


# =========================================================
# URL ANALYSIS
# =========================================================

def analyze_url(url):

    score = 100

    warnings = []

    # Add HTTP if URL starts with www
    if url.lower().startswith("www."):

        url = "http://" + url

    parsed = urlparse(url)

    host = parsed.hostname

    if not host:

        return 0, ["Invalid URL"]

    print("\n")

    print(
        Fore.CYAN +
        "=" * 55
    )

    print(
        Fore.CYAN +
        "                 URL ANALYSIS"
    )

    print(
        Fore.CYAN +
        "=" * 55
    )

    # -----------------------------------------------------
    # HTTPS
    # -----------------------------------------------------

    if parsed.scheme.lower() == "https":

        print(
            Fore.GREEN +
            "[+] HTTPS              : PASS"
        )

    else:

        print(
            Fore.YELLOW +
            "[!] HTTPS              : WARNING"
        )

        score -= 15

        warnings.append(
            "HTTPS not enabled"
        )

    # -----------------------------------------------------
    # IP ADDRESS
    # -----------------------------------------------------

    if check_ip(host):

        print(
            Fore.RED +
            "[!] IP Address         : WARNING"
        )

        score -= 25

        warnings.append(
            "URL uses an IP address"
        )

    else:

        print(
            Fore.GREEN +
            "[+] IP Address         : PASS"
        )

    # -----------------------------------------------------
    # URL SHORTENER
    # -----------------------------------------------------

    if check_shortener(host):

        print(
            Fore.YELLOW +
            "[!] URL Shortener      : WARNING"
        )

        score -= 20

        warnings.append(
            "Known URL shortener"
        )

    else:

        print(
            Fore.GREEN +
            "[+] URL Shortener      : PASS"
        )

    # -----------------------------------------------------
    # SUSPICIOUS CHARACTERS
    # -----------------------------------------------------

    suspicious = check_suspicious_characters(url)

    if suspicious:

        print(
            Fore.YELLOW +
            "[!] Suspicious Pattern : WARNING"
        )

        score -= min(
            len(suspicious) * 10,
            25
        )

        for item in suspicious:

            warnings.append(item)

    else:

        print(
            Fore.GREEN +
            "[+] Suspicious Pattern : PASS"
        )

    # -----------------------------------------------------
    # SECURITY KEYWORDS
    # -----------------------------------------------------

    keywords = check_keywords(url)

    if keywords:

        print(
            Fore.YELLOW +
            "[!] Security Keywords  : WARNING"
        )

        score -= min(
            len(keywords) * 5,
            20
        )

        warnings.append(
            "Security-related keywords found"
        )

    else:

        print(
            Fore.GREEN +
            "[+] Security Keywords  : PASS"
        )

    # -----------------------------------------------------
    # URL ENCODING
    # -----------------------------------------------------

    decoded = unquote(url)

    if decoded != url:

        print(
            Fore.YELLOW +
            "[!] Encoded Content    : WARNING"
        )

        score -= 10

        warnings.append(
            "Encoded URL detected"
        )

    else:

        print(
            Fore.GREEN +
            "[+] Encoded Content    : PASS"
        )

    # Keep score between 0 and 100

    score = max(
        0,
        min(score, 100)
    )

    return score, warnings


# =========================================================
# RISK LEVEL
# =========================================================

def get_risk(score):

    if score >= 80:

        return (
            Fore.GREEN +
            "SAFE" +
            Style.RESET_ALL
        )

    elif score >= 50:

        return (
            Fore.YELLOW +
            "SUSPICIOUS" +
            Style.RESET_ALL
        )

    else:

        return (
            Fore.RED +
            "HIGH RISK" +
            Style.RESET_ALL
        )


# =========================================================
# QR ANALYSIS
# =========================================================

def analyze_qr(data):

    print("\n")

    print(
        Fore.CYAN +
        "=" * 70
    )

    print(
        Fore.CYAN +
        "                         QR RESULT"
    )

    print(
        Fore.CYAN +
        "=" * 70
    )

    print(
        Fore.WHITE +
        "\n[+] Decoded QR Data:"
    )

    print(
        Fore.WHITE +
        data
    )

    # -----------------------------------------------------
    # Check URL
    # -----------------------------------------------------

    if not is_url(data):

        print(
            Fore.YELLOW +
            "\n[*] QR contains text/data instead of a URL."
        )

        print(
            Fore.YELLOW +
            "[*] URL security analysis was not performed."
        )

        print(
            Fore.CYAN +
            "\n" + "=" * 70
        )

        return

    # -----------------------------------------------------
    # URL Analysis
    # -----------------------------------------------------

    score, warnings = analyze_url(data)

    # -----------------------------------------------------
    # Security Result
    # -----------------------------------------------------

    print("\n")

    print(
        Fore.CYAN +
        "=" * 70
    )

    print(
        Fore.CYAN +
        "                     SECURITY RESULT"
    )

    print(
        Fore.CYAN +
        "=" * 70
    )

    # Score color

    if score >= 80:

        score_color = Fore.GREEN

    elif score >= 50:

        score_color = Fore.YELLOW

    else:

        score_color = Fore.RED

    print(
        score_color +
        f"\nSecurity Score : {score}/100"
    )

    print(
        f"Risk Level     : {get_risk(score)}"
    )

    # -----------------------------------------------------
    # Warnings
    # -----------------------------------------------------

    if warnings:

        print(
            Fore.YELLOW +
            "\nWarnings:"
        )

        for warning in warnings:

            print(
                Fore.YELLOW +
                f"  - {warning}"
            )

    else:

        print(
            Fore.GREEN +
            "\n[+] No major warnings detected."
        )

    print(
        Fore.CYAN +
        "\n" + "=" * 70
    )


# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        banner()

        print(
            Fore.WHITE +
            "\n[1] Scan QR using Camera"
        )

        print(
            Fore.WHITE +
            "[2] Scan QR from Image"
        )

        print(
            Fore.WHITE +
            "[3] Exit"
        )

        print(
            Fore.CYAN +
            "-" * 70
        )

        choice = input(
            Fore.CYAN +
            "Select option: "
        ).strip()

        # -------------------------------------------------
        # CAMERA SCAN
        # -------------------------------------------------

        if choice == "1":

            data = scan_camera()

            if data:

                print(
                    Fore.GREEN +
                    "\n[+] QR code detected!"
                )

                analyze_qr(data)

            else:

                print(
                    Fore.RED +
                    "\n[!] No QR code detected."
                )

        # -------------------------------------------------
        # IMAGE SCAN
        # -------------------------------------------------

        elif choice == "2":

            path = input(
                Fore.CYAN +
                "\nEnter QR image path: "
            ).strip()

            data = decode_image(path)

            if data:

                print(
                    Fore.GREEN +
                    "\n[+] QR code detected!"
                )

                analyze_qr(data)

            else:

                print(
                    Fore.RED +
                    "\n[!] Could not detect QR code."
                )

        # -------------------------------------------------
        # EXIT
        # -------------------------------------------------

        elif choice == "3":

            print(
                Fore.CYAN +
                "\n[*] Exiting QR Security Analyzer..."
            )

            print(
                Fore.GREEN +
                "[+] Goodbye!"
            )

            break

        # -------------------------------------------------
        # INVALID OPTION
        # -------------------------------------------------

        else:

            print(
                Fore.RED +
                "\n[!] Invalid option."
            )


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    main()

