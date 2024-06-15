import colorama
from database.setup import create_tables
from models.display_drivers import Driver
from models.book_ride import Booking
from colorama import Fore, Style
colorama.init()
import readline
import random

inputs = []

def get_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            inputs.append(user_input)
            return user_input
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            try:
                # Ask user to confirm exit
                user_choice = input("Press 'Enter' again to exit, type 'back' to go back, or enter any other key to continue: ")
                if user_choice == 'back':
                    handle_ctrl_c()
                elif user_choice == '':
                    print("Exiting...")
                    print("Program Terminated.")
                    exit()

                else:
                    print("\nContinuing...")
            except KeyboardInterrupt:
                print("\nContinuing...")
            except Exception as e:
                print(f"Error: {e}")   
        except Exception as e:
            print(f"Error: {e}")   
                
def handle_ctrl_c():
    if inputs:
        edited_input = input(f"Edit your input: [{inputs[-1]}] ")
        inputs[-1] = edited_input
        print("Input edited successfully!")

def display_menu():

    choice = 0

    menu_options = [
    (1, Fore.RED, "Register as a Driver", add_driver),
    (2, Fore.BLUE, "Instant Ride Requests", book_ride),
    (3, Fore.RED, "Display Drivers", display_drivers),
    (4, Fore.RED, "Display Bookings", display_bookings),
    (5, Fore.RED, "Delete Driver", delete_driver),
    (6, Fore.RED, "Delete Booking", delete_booking),
    (7, Fore.RED, "Exit", exited),
    (8, Fore.YELLOW, "Book Ride (Ride Pooling)", book_ride_pooling)  # Option for ride pooling
]
    
    while choice != 7 :
        try:
            print(Fore.GREEN + Style.BRIGHT + "===== Welcome to SchoolRide =====" + Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM + "\nAvailable Options:" + Style.RESET_ALL)
            for option in menu_options:
                print(f"{Fore.MAGENTA}{option[0]}{Style.RESET_ALL}. {option[1]}{option[2]}{Style.RESET_ALL}")
            print('"To go back or exit \'ctrl c\'."\n')

            while True:    
                choice = int(get_input("\nEnter your choice: "))
                # Find the chosen option in the menu_options list
                selected_option = next((opt for opt in menu_options if opt[0] == choice), None)
                if not selected_option:
                    print("Invalid choice. Please try again.")   
                else:    
                    selected_option[3]()
                    
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print('"You are always welcomed, come again,,,"\n')   
          
def exited():
    print("Exiting...")
    exit()      

def delete_driver():
    driver_id = input("Enter driver's ID to delete: ")
    Driver.delete_driver(driver_id)

def delete_booking():
    booking_id = input("Enter booking ID to delete: ")
    Booking.delete_booking(booking_id)    

def add_driver():
    print(Fore.GREEN + "===== Driver's Registration =====" + Style.RESET_ALL)
    name = get_input(Fore.CYAN +"Enter driver's name: "+ Style.RESET_ALL)
    contact = get_input(Fore.CYAN +"Enter driver's contact: "+ Style.RESET_ALL)
    vehicle = get_input(Fore.CYAN +"Enter driver's vehicle: "+ Style.RESET_ALL)
    Driver.add_driver(name, contact, vehicle)
    print("Driver added successfully!")
   
def book_ride():
    try:
        print(Fore.GREEN + "===== Booking a Ride =====" + Style.RESET_ALL)
        student_name = get_input(Fore.CYAN + "Enter student's name: " + Style.RESET_ALL)
        pick_up = get_input(Fore.CYAN + "Enter pick-up location: " + Style.RESET_ALL)
        drop_off = get_input(Fore.CYAN + "Enter drop-off location: " + Style.RESET_ALL)
        # Lambda function for generating a random cost within a specified range
        generate_random_cost = lambda: random.uniform(10.0, 50.0)
        cost = generate_random_cost()
        # Simulating random driver assignment (replace with actual logic if needed)
        drivers = Driver.get_all()
        if drivers:
            selected_driver = random.choice(drivers)
            driver_id = selected_driver['id']
            # Assuming Booking.book_ride handles the database interaction
            Booking.book_ride(driver_id, student_name, pick_up, drop_off,cost, "individual")
            print(f"Driver assigned: {selected_driver['name']}")
        # Simulating ETA calculation (replace with actual logic if needed)
        eta_minutes = random.randint(5, 30)  # Random ETA between 5 to 30 minutes
        print(f"Estimated Time of Arrival (ETA): {eta_minutes} minutes" + "\n" + f"Ride booked successfully! Cost: ${cost:.2f}")
        # Ask user to rate the driver
        rate_driver(driver_id)

    except ValueError:
        print("Invalid input. Please enter a valid driver ID.")
    except Exception as e:
        print(f"Error: {e}")

def book_ride_pooling():
    # Initialize an empty list to store students
    students = []
    # Allow the user to input multiple students
    while True:
        student_name = get_input(Fore.CYAN + "Enter student's name (or 'done' to finish): " + Style.RESET_ALL)
        if student_name.lower() == 'done':
            break
        students.append(student_name)
    
    pick_up = get_input(Fore.CYAN + "Enter pick-up location: " + Style.RESET_ALL)
    drop_off = get_input(Fore.CYAN + "Enter drop-off location: " + Style.RESET_ALL)
    # Lambda function for generating a random cost within a specified range
    generate_random_cost = lambda: random.uniform(10.0, 50.0)
    # Generate a random cost for the ride pooling
    cost = generate_random_cost()  # Function to generate random cost
    # Simulating random driver assignment (replace with actual logic if needed)
    drivers = Driver.get_all()
    if drivers:
        selected_driver = random.choice(drivers)
        driver_id = selected_driver['id']
        # Assuming Booking.book_ride handles the database interaction
        print(f"Driver assigned: {selected_driver['name']}")
        # Book the ride for each student in the list
        for student in students:
            Booking.book_ride(driver_id, student, pick_up, drop_off, cost, "pooling")
            print(f"Student '{student}' added to the ride pooling.")
    # Simulating ETA calculation (replace with actual logic if needed)
    eta_minutes = random.randint(5, 30)  # Random ETA between 5 to 30 minutes
    print(f"Estimated Time of Arrival (ETA): {eta_minutes} minutes" + "\n" + f"Ride pooling booked successfully! Cost per student: ${cost:.2f}")

def rate_driver(driver_id):
    while True:    
        try:
            rating = int(get_input("Rate the driver (1-5 stars): "))
            if 1 <= rating <= 5:
                # Assuming Driver.rate_driver updates the driver's rating in the database
                Driver.rate_driver(driver_id, rating)
                print("Driver rated successfully!")
                break
            else:
                    print("Invalid rating. Please enter a number between 0.0 and 5.0.")    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")

def display_drivers():
    try:
        drivers = Driver.get_all()
        print(Fore.GREEN + "Drivers:" + Style.RESET_ALL)
        for driver in drivers:
            print(f"ID: {driver['id']}\t| Name: {driver['name']}\t| Vehicle: {driver['vehicle']}\t| Rating: {driver['rating']}")
    except Exception as e:
        print(f"Error: {e}")

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
