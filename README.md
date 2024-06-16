# Phase-3-Project

# SchoolRide CLI Application

SchoolRide is a command-line interface (CLI) application designed to manage transportation services for students. It offers functionalities to register drivers, manage ride bookings, and display relevant information about drivers and bookings. The application is built with simplicity and user-friendliness in mind, aiming to provide a seamless experience for users involved in school transportation management.

## Features

- **Driver Management:**
  - Register new drivers.
  - Display existing drivers.
  - Delete drivers from the system.

- **Booking Management:**
  - Book instant rides.
  - Display current bookings.
  - Delete bookings as needed.
  - Book rides with pooling options for cost efficiency.

- **User Interface:**
  - Color-coded interface using Colorama for better user experience.
  - Interactive menu system for easy navigation.

## Installation

To run SchoolRide on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SchoolRide

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Initialize the database:**
   ```bash
   python -m database.setup

Usage
Run the application:

bash
Copy code
python main.py
Follow the on-screen instructions to navigate through the menu and use the application:

Upon running the application, you will be presented with a menu displaying various options.
Use the number keys to select an option and press Enter.
Depending on the chosen option, follow the prompts to register drivers, book rides, display information, or exit the application.
For any unexpected behavior or errors, refer to the error messages displayed for troubleshooting.

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

