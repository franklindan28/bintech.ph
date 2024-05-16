import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('user_db.db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            rfid TEXT UNIQUE
                            )''')
        self.conn.commit()

    def register_user(self, username, password, rfid):
        try:
            self.cur.execute('''INSERT INTO users (username, password, rfid)
                                VALUES (?, ?, ?)''', (username, password, rfid))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login_user(self, username, password, rfid):
        self.cur.execute('''SELECT * FROM users WHERE username = ? AND password = ? AND rfid = ?''', (username, password, rfid))
        user = self.cur.fetchone()
        return user is not None

    def __del__(self):
        self.conn.close()
