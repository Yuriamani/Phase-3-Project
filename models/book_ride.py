
import sqlite3
conn = sqlite3.connect('./database/schoolride.db')
cursor = conn.cursor()

class Booking:
    def __init__(self, driver_id, student_name, pick_up, drop_off, cost, ride_type):
        self.driver_id = driver_id
        self.student_name = student_name
        self.pick_up = pick_up
        self.drop_off = drop_off
        self.cost = cost
        self.ride_type = ride_type

    def save(self):
        cursor.execute("INSERT INTO bookings (driver_id,student_name, pick_up, drop_off,cost,ride_type) VALUES ( ?, ?, ?, ?, ?, ? )", (self.driver_id, self.student_name, self.pick_up, self.drop_off, self.cost, self.ride_type))
        conn.commit()

    @classmethod
    def get_all(cls):
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        return bookings
    
    @classmethod
    def delete_booking(cls,booking_id):
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
        print("Booking deleted successfully.")
