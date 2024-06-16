import sqlite3
conn = sqlite3.connect('./database/schoolride.db')
cursor = conn.cursor()

class Driver:
    def __init__(self, name, contact, vehicle):
        self.name = name
        self.contact = contact
        self.vehicle = vehicle

    def save(self):
        cursor.execute("INSERT INTO drivers (name, contact, vehicle) VALUES (?, ?, ?)", (self.name, self.contact, self.vehicle))
        conn.commit()
       
    @classmethod
    def get_all(cls):
        cursor.execute("SELECT * FROM drivers")
        drivers = cursor.fetchall()
        return drivers
    
    @classmethod
    def delete_driver(cls,driver_id):
        cursor.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))
        conn.commit()
        print("Driver deleted successfully.")

    @classmethod
    def rate_driver(cls,driver_id, rating):
        try:
            # Update the driver's rating in the database
            cursor.execute("UPDATE drivers SET rating = ? WHERE id = ?", (rating, driver_id))
            conn.commit()
            print(f"Driver with ID {driver_id} rated successfully!")
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")
               
