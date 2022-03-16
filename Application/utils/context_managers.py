from contextlib import contextmanager
import sqlite3
@contextmanager
def cursor_handler():
    conn = sqlite3.connect('Data/hushHush.db')
    c = conn.cursor()
    yield c
    conn.commit()
    c.close()
    conn.close()

@contextmanager
def connection_handler():
    conn = sqlite3.connect('Data/HushHush.db')
    yield conn
    conn.commit()
    conn.close()