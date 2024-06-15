import colorama
from database.setup import create_tables
from models.display_drivers import Driver
from models.book_ride import Booking
from colorama import Fore, Style
colorama.init()

 

def display_menu():

    choice = 0

    menu_options = [
    (1, Fore.BLUE, "Add Driver", add_driver),
    (2, Fore.BLUE, "Book Ride", book_ride),
    (3, Fore.BLUE, "Display Drivers", display_drivers),
    (4, Fore.BLUE, "Display Bookings", display_bookings),
    (5, Fore.RED, "Delete Driver", delete_driver),
    (6, Fore.RED, "Delete Booking", delete_booking),
    (7, Fore.RED, "Exit", exit_program)
]
    
    while choice != 7 :
        try:
            print(Fore.GREEN + Style.BRIGHT + "===== Welcome to SchoolRide =====" + Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM + "\nAvailable Options:" + Style.RESET_ALL)
            for option in menu_options:
                print(f"{option[0]}. {option[1]}{option[2]}{Style.RESET_ALL}")
            
            chosen_option = int(input("\nEnter your choice: "))
            # Find the chosen option in the menu_options list
            selected_option = next((opt for opt in menu_options if opt[0] == chosen_option), None)

            if not selected_option:
                print("Invalid choice. Please try again.")
            else:    
                selected_option[3]()    
        except ValueError:
            print("Invalid input. Please enter a number.")


    print("Program Terminated.")
    

def exit_program():
      print("Exiting...")

def delete_driver():
    driver_id = input("Enter driver's ID to delete: ")
    Driver.delete_driver(driver_id)

def delete_booking():
    booking_id = input("Enter booking ID to delete: ")
    Booking.delete_booking(booking_id)    

def add_driver():
    name = input("Enter driver's name: ")
    contact = input("Enter driver's contact: ")
    vehicle = input("Enter driver's vehicle: ")
    Driver.add_driver(name, contact, vehicle)
    print("Driver added successfully!")
   

def book_ride():
    driver_id = int(input(Fore.CYAN + "Enter driver's ID: "))
    student_name = input("Enter student's name: ")
    pick_up = input("Enter pick-up location: ")
    drop_off = input("Enter drop-off location: "+ Style.RESET_ALL)
    Booking.book_ride(driver_id, student_name, pick_up, drop_off)
    print("Ride booked successfully!")

def display_drivers():
    drivers = Driver.get_all()
    print(Fore.GREEN + "Drivers:" + Style.RESET_ALL)
    for driver in drivers:
        print(f"ID: {driver['id']}\t| Name: {driver['name']}\t| Contact: {driver['contact']}\t| Vehicle: {driver['vehicle']}")

def display_bookings():
    bookings = Booking.get_all()
    print(Fore.GREEN + "Bookings:" + Style.RESET_ALL)
    for booking in bookings:
        print(f"ID: {booking['id']}\t| Driver ID: {booking['driver_id']}\t| Student Name: {booking['student_name']}\t| Pick-up: {booking['pick_up']}\t| Drop-off: {booking['drop_off']}")



def main():
    create_tables()  # Create tables before interacting with them
    display_menu() #Menu Display
        


if __name__ == "__main__":
    main()
