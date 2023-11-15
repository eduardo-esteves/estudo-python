import sqlite3
from pathlib import Path


# CPBA 392
ROOT_DIR = Path(__file__).resolve().parent
DB_FILE = Path(ROOT_DIR, 'modulo5.sqlite3')
table_name = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

values = [
    {"name": "Edson Esteves", "weight": 62},
    {"name": "Larissa Esteves", "weight": 60}
]

# SQL Commands Here
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {table_name} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL)'
)

con.commit()

cursor.executemany(
    f'INSERT INTO {table_name}'
    '(name, weight)'
    'VALUES '
    '(:name, :weight)',
    values
)

con.commit()

cursor.close()
con.close()
