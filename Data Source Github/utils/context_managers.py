from contextlib import contextmanager
import sqlite3
@contextmanager
def cursor_handler():
    conn = sqlite3.connect('Output Files/github_database.db')
    c = conn.cursor()
    yield c
    conn.commit()
    c.close()
    conn.close()

@contextmanager
def connection_handler():
    conn = sqlite3.connect('Output Files/github_database.db')
    yield conn
    conn.commit()
    conn.close()
