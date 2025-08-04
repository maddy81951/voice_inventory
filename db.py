import sqlite3
import os
#print(sqlite3.sqlite_version)

def create_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            quantity TEXT NOT NULL,
            location TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            qr_path TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(item, quantity, location, timestamp, qr_path):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO inventory (item, quantity, location, timestamp, qr_path)
        VALUES (?, ?, ?, ?, ?)
    ''', (item, quantity, location, timestamp, qr_path))
    conn.commit()
    conn.close()
