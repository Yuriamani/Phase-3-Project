# Phase-3-Project

# SchoolRide

SchoolRide is a command-line interface (CLI) application designed to manage transportation services for students. It allows users to add drivers, book rides, display driver and booking information, delete drivers or bookings, and exit the program.

## Features

1. **Add Driver**:
   - Collects and stores information about new drivers, including name, contact, and vehicle details.

2. **Book Ride**:
   - Allows users to book rides by specifying driver ID, student name, pick-up location, and drop-off location.

3. **Display Drivers**:
   - Retrieves and displays a list of all registered drivers, including their IDs, names, contact details, and vehicles.

4. **Display Bookings**:
   - Retrieves and displays a list of all bookings made, including booking IDs, driver IDs, student names, pick-up locations, and drop-off locations.

5. **Delete Driver**:
   - Allows users to delete a driver from the database by entering the driver's ID.

6. **Delete Booking**:
   - Allows users to delete a booking from the database by entering the booking ID.

7. **Exit**:
   - Terminates the program and exits gracefully.

## Technical Details

### Implementation

- **Colorama**: Used for colorizing text output in the terminal for improved readability.
- **Readline**: Enables enhanced input handling, including catching interrupts like Ctrl+C.
- **Database Setup**: Utilizes PostgreSQL via the `create_tables` function to initialize database tables.
- **Models**: Interacts with `Driver` and `Booking` models to perform CRUD operations.
- **Exception Handling**: Implemented to manage errors and user interruptions gracefully.

### Usage

To run the SchoolRide application:
1. Ensure Python and necessary dependencies (`colorama`, `psycopg2`, etc.) are installed.
2. Execute `python app.py` in your terminal to start the program.
3. Follow the on-screen prompts to navigate through menu options, enter data, and manage drivers and bookings.

### Next Steps

- **Enhancements**: Consider adding features such as updating driver details, editing bookings, or implementing more advanced scheduling options.
- **Testing**: Expand test coverage to ensure robustness and reliability.
- **Feedback**: Gather user feedback to improve usability and functionality.

## Conclusion

SchoolRide aims to streamline school transportation management through a simple yet effective CLI interface. It prioritizes ease of use, data integrity, and user convenience to ensure a seamless experience for students, parents, and administrators alike.

