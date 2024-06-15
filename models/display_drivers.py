from database.connection import get_db_connection

class Driver:
    def __init__(self, name, contact, vehicle):
        self.name = name
        self.contact = contact
        self.vehicle = vehicle

    @staticmethod
    def add_driver(name, contact, vehicle):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO drivers (name, contact, vehicle) VALUES (?, ?, ?)", (name, contact, vehicle))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drivers")
        drivers = cursor.fetchall()
        conn.close()
        return drivers
    
    @staticmethod
    def delete_driver(driver_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))

        conn.commit()
        conn.close()
        print("Driver deleted successfully.")

    @staticmethod
    def rate_driver(driver_id, rating):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Update the driver's rating in the database
            cursor.execute("UPDATE drivers SET rating = ? WHERE id = ?", (rating, driver_id))
            conn.commit()
            print(f"Driver with ID {driver_id} rated successfully!")

        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")

        finally:
            conn.close()    
