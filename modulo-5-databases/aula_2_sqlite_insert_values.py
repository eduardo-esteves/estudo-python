import sqlite3
from pathlib import Path


# CPBA 387
ROOT_DIR = Path(__file__).resolve().parent
DB_FILE = Path(ROOT_DIR, 'modulo5.sqlite3')
table_name = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# SQL Commands Here
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {table_name} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL)'
)

con.commit()

cursor.execute(
    f'INSERT INTO {table_name}'
    '(name, weight)'
    'VALUES '
    '("Eduardo Esteves", 92),'
    '("Vitor Esteves", 30)'
)

con.commit()

cursor.close()
con.close()
