import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

query = 'SELECT name FROM tasks'

tasks = cur.execute(query)

for task in tasks:
    print(task[0])

## Działa