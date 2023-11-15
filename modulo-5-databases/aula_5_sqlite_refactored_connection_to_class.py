from sqlite_modules.SqliteConnection import SqliteConnection


table_name = 'customers'

connection = SqliteConnection('modulo5.sqlite3')
result = connection.exec(f'SELECT * FROM {table_name}')


for row in result.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

result.close()
