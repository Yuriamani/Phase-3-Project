import sqlite3
import colorama
from colorama import Fore, Style
colorama.init()
conn = sqlite3.connect('./database/schoolride.db')
cursor = conn.cursor()

class Driver:
    def __init__(self, name, contact, vehicle):
        self.name = name
        self.contact = contact
        self.vehicle = vehicle

    # Register driver
    @classmethod
    def add_driver(cls):
        print(Fore.GREEN + "===== Driver's Registration =====" + Style.RESET_ALL)
        name = input(Fore.CYAN +"Enter driver's name: "+ Style.RESET_ALL)
        contact = input(Fore.CYAN +"Enter driver's contact: "+ Style.RESET_ALL)
        vehicle = input(Fore.CYAN +"Enter driver's vehicle: "+ Style.RESET_ALL)
        cursor.execute("INSERT INTO drivers (name, contact, vehicle) VALUES (?, ?, ?)", (name, contact, vehicle))
        conn.commit()
        print("Driver added successfully!")

    #Display drivers   
    @classmethod
    def display_drivers(cls):
        cursor.execute("SELECT * FROM drivers")
        drivers = cursor.fetchall()
        print(Fore.GREEN + "Drivers:" + Style.RESET_ALL)
        for driver in drivers:
            print(f"ID: {driver[0]}\t| Name: {driver[1]}\t| Vehicle: {driver[3]}\t| Rating: {driver[4]}")

    #Remove drivers registration
    @classmethod
    def delete_driver(cls):
        driver_id = input("Enter driver's ID to delete: ")
        cursor.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))
        conn.commit()
        print("Driver deleted successfully.")

    @classmethod
    #Rate driver
    def rate_driver(cls,driver_id):
        while True:    
            try:
                rating = int(input("Rate the driver (1-5 stars): "))
                if 1 <= rating <= 5:
                    try:
                    # Update the driver's rating in the database
                        cursor.execute("UPDATE drivers SET rating = ? WHERE id = ?", (rating, driver_id))
                        conn.commit()
                        print(f"Driver with ID {driver_id} rated successfully!")
                    except Exception as e:
                        conn.rollback()
                        print(f"Error: {e}")
                
                    print("Driver rated successfully!")
                    break
                else:
                    print("Invalid rating. Please enter a number between 1 and 5")    
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"Error: {e}")
               
