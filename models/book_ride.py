from database.connection import get_db_connection

class Booking:
    def __init__(self, driver_id, student_name, pick_up, drop_off):
        self.driver_id = driver_id
        self.student_name = student_name
        self.pick_up = pick_up
        self.drop_off = drop_off

    @staticmethod
    def book_ride(driver_id,student_name, pick_up, drop_off,cost,ride_type):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (driver_id,student_name, pick_up, drop_off,cost,ride_type) VALUES ( ?, ?, ?, ?, ?, ? )", (driver_id, student_name, pick_up, drop_off, cost,ride_type))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        conn.close()
        return bookings
    
    @staticmethod
    def delete_booking(booking_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
        conn.close()
        print("Booking deleted successfully.")
