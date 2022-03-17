from contextlib import contextmanager
import sqlite3
import utils
@contextmanager
def cursor_handler():
    conn = sqlite3.connect('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application/Data/HushHush.db')
    c = conn.cursor()
    yield c
    conn.commit()
    c.close()
    conn.close()

@contextmanager
def connection_handler():
    conn = sqlite3.connect('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application/Data/HushHush.db')
    yield conn
    conn.commit()
    conn.close()
