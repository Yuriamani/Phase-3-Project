import sqlite3

conn = sqlite3.connect('./database/schoolride.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def create_tables():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            vehicle TEXT NOT NULL,
            rating REAL 
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            pick_up TEXT NOT NULL,
            drop_off TEXT NOT NULL,
            cost REAL,       
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ride_type TEXT,           
            FOREIGN KEY (id) REFERENCES drivers (id)
        )
    ''')

    conn.commit()
    conn.close()


