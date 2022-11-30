import sqlite3
import datetime

dt=18000
def dateToday():
    return str(datetime.datetime.utcfromtimestamp(datetime.datetime.timestamp(datetime.datetime.today())+dt).strftime('%H:%M:%S %d-%m-%Y'))
def get_date(tms):
    return datetime.datetime.utcfromtimestamp(tms).strftime('%H:%M:%S %d-%m-%Y')
def add_notes(note: str) -> bool:
    if note: 
        date = str(datetime.datetime.timestamp(datetime.datetime.today())+dt)
        with sqlite3.connect('usNotes.db') as db:
            sql = db.cursor()
            sql.execute(f"INSERT INTO notes(note, date) VALUES (?, ?)", (note, date))
            db.commit()
        return True
    return False
def listNotesFunc():
    with sqlite3.connect('usNotes.db') as db:
        sql = db.cursor()
        sql.execute(f"SELECT * from notes order by date")
        return sql

def del_note(noteId) -> bool:
    if noteId:
        with sqlite3.connect('usNotes.db') as db:
            sql = db.cursor()
            sql.execute(f"delete from notes where id_note==?",(noteId,))
            db.commit()
            return True
    return False
def changeType_note(noteId, done) -> bool:
    if done==0:
        done=1
    else:
        done=0
    if noteId:
        with sqlite3.connect('usNotes.db') as db:
            sql = db.cursor()
            sql.execute(f"UPDATE notes set done==? where id_note==?",(done, noteId))
            db.commit()
            return True
    return False