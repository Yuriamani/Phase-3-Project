import colorama
from colorama import Fore, Style
colorama.init()
import random
from .display_drivers import Driver
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

    #Boook a ride
    @classmethod   
    def book_ride(cls):
        try:
            print(Fore.GREEN + "===== Booking a Ride =====" + Style.RESET_ALL)
            student_name = input(Fore.CYAN + "Enter student's name: " + Style.RESET_ALL)
            pick_up = input(Fore.CYAN + "Enter pick-up location: " + Style.RESET_ALL)
            drop_off = input(Fore.CYAN + "Enter drop-off location: " + Style.RESET_ALL)
            
            generate_random_cost = lambda: random.uniform(10.0, 50.0) # Function to generate random cost within a specified range
            cost = generate_random_cost() # Generate a random cost for the ride
            
            cursor.execute("SELECT * FROM drivers")
            drivers = cursor.fetchall()

            ride_type = 'individual'
            if drivers:
                selected_driver = random.choice(drivers)#Assighning a driver
                driver_id = selected_driver[0] #'id'
                cursor.execute("INSERT INTO bookings (driver_id,student_name, pick_up, drop_off,cost,ride_type) VALUES ( ?, ?, ?, ?, ?, ? )", (driver_id, student_name, pick_up, drop_off, cost, ride_type))
                conn.commit()
                print(f"Driver assigned: {selected_driver[1]}")
            # Simulating ETA calculation (replace with actual logic if needed)
            eta_minutes = random.randint(5, 30)  # Random ETA between 5 to 30 minutes
            print(f"Estimated Time of Arrival (ETA): {eta_minutes} minutes" + "\n" + f"Ride booked successfully! Cost: ${cost:.2f}")
            
            Driver.rate_driver(driver_id)# Ask user to rate the driver

        except ValueError:
            print("Invalid input. Please enter a valid driver ID.")
        except Exception as e:
            print(f"Error: {e}")

    #Book ride pooling
    @classmethod
    def book_ride_pooling(cls):
        
        students = []
        # Allow the user to input multiple students
        while True:
            student_name = input(Fore.CYAN + "Enter student's name (or 'done' to finish): " + Style.RESET_ALL)
            if student_name.lower() == 'done':
                break
            students.append(student_name)
        
        pick_up = input(Fore.CYAN + "Enter pick-up location: " + Style.RESET_ALL)
        drop_off = input(Fore.CYAN + "Enter drop-off location: " + Style.RESET_ALL)
        
        generate_random_cost = lambda: random.uniform(10.0, 50.0) # Function to generate random cost within a specified range
        
        cost = generate_random_cost()  # Generate a random cost for the ride pooling
        
        cursor.execute("SELECT * FROM drivers")
        drivers = cursor.fetchall()
        ride_type = 'pooling'
        if drivers:
            selected_driver = random.choice(drivers) #Assighning a driver
            driver_id = selected_driver[0] #'id'
            print(f"Driver assigned: {selected_driver[1]}")
            # Book the ride for each student in the list
            for student in students:
                cursor.execute("INSERT INTO bookings (driver_id,student_name, pick_up, drop_off,cost,ride_type) VALUES ( ?, ?, ?, ?, ?, ? )", (driver_id, student_name, pick_up, drop_off, cost, ride_type))
                conn.commit()
                print(f"Student '{student}' added to the ride pooling.")
        # Simulating ETA calculation (replace with actual logic if needed)
        eta_minutes = random.randint(5, 30)  # Random ETA between 5 to 30 minutes
        print(f"Estimated Time of Arrival (ETA): {eta_minutes} minutes" + "\n" + f"Ride pooling booked successfully! Cost per student: ${cost:.2f}")
        
        Driver.rate_driver(driver_id) # Ask users to rate the driver

    #Display bookings
    @classmethod
    def display_bookings(cls):
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        print(Fore.GREEN + "Bookings:" + Style.RESET_ALL)
        for booking in bookings:
            print(f"ID: {booking[0]}\t| Driver ID: {booking[1]}\t| Student Name: {booking[2]}\t| Pick-up: {booking[3]}\t| Drop-off: {booking[4]}")

    
    @classmethod
    def delete_booking(cls,booking_id):
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
        print("Booking deleted successfully.")
