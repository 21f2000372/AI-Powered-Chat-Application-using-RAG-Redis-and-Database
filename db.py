import sqlite3

def init_db():
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            question TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_message(user_id, question, answer):
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (user_id, question, answer) VALUES (?, ?, ?)", 
                (user_id, question, answer))
    conn.commit()
    conn.close()

def get_messages(user_id):
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()
    cur.execute("SELECT question, answer FROM messages WHERE user_id=?", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [{"question": q, "answer": a} for q, a in rows]
