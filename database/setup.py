from .connection import get_db_connection

def create_tables():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            vehicle TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            pick_up TEXT NOT NULL,
            drop_off TEXT NOT NULL,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (driver_id) REFERENCES drivers (id)
        )
    ''')

    conn.commit()
    conn.close()


