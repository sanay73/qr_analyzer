import sqlite3
from datetime import datetime


DATABASE = "scan_history.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            data TEXT,
            score INTEGER,
            risk TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_scan(data, score, risk):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO scans
        (date, data, score, risk)
        VALUES (?, ?, ?, ?)
    """, (date, data, score, risk))

    connection.commit()
    connection.close()


def show_history():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, date, data, score, risk
        FROM scans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    if not rows:

        print("\n[!] No scan history.")

        return

    print("\n")
    print("=" * 70)
    print("                         SCAN HISTORY")
    print("=" * 70)

    for row in rows:

        print(f"\nID       : {row[0]}")
        print(f"Date     : {row[1]}")
        print(f"Data     : {row[2]}")
        print(f"Score    : {row[3]}/100")
        print(f"Risk     : {row[4]}")
