import sqlite3
from pathlib import Path


# CPBA 387
ROOT_DIR = Path(__file__).resolve().parent
DB_FILE = Path(ROOT_DIR, 'modulo5.sqlite3')

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# SQL Commands Here
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL)'
)

con.commit()

cursor.close()
con.close()
