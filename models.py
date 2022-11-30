import sqlite3

with sqlite3.connect('usNotes.db') as db:
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS notes (
        id_note INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT NOT NULL,
        date REAL NOT NULL,
        done INTEGER DEFAULT 0
        )""")
    db.commit()