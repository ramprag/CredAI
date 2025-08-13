import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("credit_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            income FLOAT,
            expenses FLOAT,
            loan_amount FLOAT,
            credit_util FLOAT,
            missed_payments INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_user_data(user_id, data):
    conn = sqlite3.connect("credit_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_data (user_id, income, expenses, loan_amount, credit_util, missed_payments, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, data["income"], data["expenses"], data["loan_amount"], data["credit_util"], data["missed_payments"], datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_user_history(user_id):
    conn = sqlite3.connect("credit_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data WHERE user_id = ? ORDER BY timestamp DESC", (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history