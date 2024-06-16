import colorama
from database.setup import create_tables
from models.display_drivers import Driver
from models.book_ride import Booking
from colorama import Fore, Style
colorama.init()
import random

# inputs = []

# def get_input(prompt):
#     while True:
#         try:
#             user_input = input(prompt)
#             inputs.append(user_input)
#             return user_input
#         except KeyboardInterrupt:
#             print("\nKeyboardInterrupt")
#             try:
#                 # Ask user to confirm exit
#                 user_choice = input("Press 'Enter' again to exit, type 'back' to go back, or enter any other key to continue: ")
#                 if user_choice == 'back':
#                     handle_ctrl_c()
#                 elif user_choice == '':
#                     print("Exiting...")
#                     print("Program Terminated.")
#                     exit()

#                 else:
#                     print("\nContinuing...")
#             except KeyboardInterrupt:
#                 print("\nContinuing...")
#             except Exception as e:
#                 print(f"Error: {e}")   
#         except Exception as e:
#             print(f"Error: {e}")   
                
# def handle_ctrl_c():
#     if inputs:
#         edited_input = input(f"Edit your input: [{inputs[-1]}] ")
#         inputs[-1] = edited_input
#         print("Input edited successfully!")  

#program Terminated          
def exited():
    print("Exiting...")
    exit()      


def main():
    create_tables()  # Create tables before interacting with them
    
    #Menu Display
    choice = 0

    menu_options = [
    (1, Fore.RED, "Register as a Driver", Driver.add_driver),
    (2, Fore.BLUE, "Instant Ride Requests", Booking.book_ride),
    (3, Fore.RED, "Display Drivers", Driver.display_drivers),
    (4, Fore.RED, "Display Bookings", Booking.display_bookings),
    (5, Fore.RED, "Delete Driver", Driver.delete_driver),
    (6, Fore.RED, "Delete Booking", Booking.delete_booking),
    (7, Fore.RED, "Exit", exited),
    (8, Fore.YELLOW, "Book Ride (Ride Pooling)", Booking.book_ride_pooling)  # Option for ride pooling
]
    
    while choice != 7 :
        try:
            print(Fore.GREEN + Style.BRIGHT + "===== Welcome to SchoolRide =====" + Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM + "\nAvailable Options:" + Style.RESET_ALL)
            for option in menu_options:
                print(f"{Fore.MAGENTA}{option[0]}{Style.RESET_ALL}. {option[1]}{option[2]}{Style.RESET_ALL}")
            print('"To go back or exit \'ctrl c\'."\n')

            while True:    
                choice = int(input("\nEnter your choice: "))
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
        


if __name__ == "__main__":
    main()
