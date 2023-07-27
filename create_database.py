import sqlite3 as sql
import pandas as pd

class Database:
    def __init__(self, db_name):
        self.conn = sql.connect(db_name)
        self.c = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        self.c.execute('''
              CREATE TABLE IF NOT EXISTS users
              (user_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, favorite_food TEXT)
              ''')
        self.conn.commit()

        self.c.execute('''
                  INSERT OR REPLACE INTO users (user_id, first_name, last_name, favorite_food)
                  VALUES
                  (1, 'nick', 'manfredi', 'french fries'),
                  (2, 'jess', 'nelson', 'pasta'),
                  (3, 'zeke', 'the greek', 'cheese')
                  ''')

        self.c.execute('''
                       DELETE from users where user_id > 3
                       ''')

        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

