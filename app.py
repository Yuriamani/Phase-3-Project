import colorama
from database.setup import create_tables
from models.display_drivers import Driver
from models.book_ride import Booking
from colorama import Fore, Style
colorama.init()

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
