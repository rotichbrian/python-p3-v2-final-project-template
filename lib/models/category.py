# category.py
from .database import get_connection
from .task import Task  # Import the Task class

class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO categories (name, description) VALUES (?, ?)
        ''', (self.name, self.description))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        conn.close()
        return rows

    @classmethod
    def find_by_id(cls, category_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    @classmethod
    def delete(cls, category_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        conn.commit()
        conn.close()

    def get_tasks(self):
        return Task.get_all_by_category(self.id)
