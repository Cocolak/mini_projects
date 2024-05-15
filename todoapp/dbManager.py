import sqlite3
import os


class DBManager:
    def __init__(self, path):
        self.db_path = path
        self.check_if_db_exists()
        # self.conn, self.cursor = self.get_conn_curs()

    def check_if_db_exists(self):
        if not os.path.exists(self.db_path):
            file = open(self.db_path, 'w')
            file.close()

            conn, cursor = self.get_conn_cursor()
            cursor.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, isDone INTEGER)")
            conn.close()

    def get_conn_cursor(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        return conn, cursor

    def get_tasks(self):
        conn, cursor = self.get_conn_cursor()
        query = 'SELECT name, isDone FROM tasks'

        tasks = cursor.execute(query)
        tasks = tasks.fetchall()
        conn.close()
        return tasks

    def add_task(self, task):
        conn, cursor = self.get_conn_cursor()
        query = 'INSERT INTO tasks(name, isDone) VALUES(?, ?)'

        cursor.execute(query, (task, 0))
        conn.commit()
        conn.close()

    def remove_task(self, task):
        conn, cursor = self.get_conn_cursor()
        query = 'DELETE FROM tasks WHERE name = ?'

        cursor.execute(query, (task,))
        conn.commit()
        conn.close()

    def checked_is_changed(self, task_name, new_value):
        conn, cursor = self.get_conn_cursor()
        query = 'UPDATE tasks SET isDone = ? WHERE name = ?'

        cursor.execute(query, (new_value, task_name))
        conn.commit()
        conn.close()

