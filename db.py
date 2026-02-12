import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    fav_style INTEGER DEFAULT 0
)
""")

conn.commit()

def add_user(user_id: int):
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def set_fav(user_id: int, idx: int):
    add_user(user_id)
    cur.execute("UPDATE users SET fav_style=? WHERE user_id=?", (idx, user_id))
    conn.commit()

def get_fav(user_id: int):
    add_user(user_id)
    cur.execute("SELECT fav_style FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    return row[0] if row else 0

def total_users():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]
