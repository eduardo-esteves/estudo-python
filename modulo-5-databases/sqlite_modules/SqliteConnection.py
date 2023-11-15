import sqlite3
from pathlib import Path


class SqliteConnection:

    __root_dir = Path(__file__).resolve().parent.parent

    def __init__(self, database):
        db_file = Path(SqliteConnection.__root_dir, database)
        con = sqlite3.connect(db_file)
        self._cursor = con.cursor()

    def exec(self, command: str) -> object:
        return self._cursor.execute(command)
