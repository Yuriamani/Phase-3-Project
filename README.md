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
   git clone <git@github.com:Yuriamani/Phase-3-Project.git>
   cd SchoolRide

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Initialize the database:**
   ```bash
   python -m database.setup



Follow the on-screen instructions to navigate through the menu and use the application:






### Usage

Run the application:
      ```bash
      python main.py

Follow the on-screen instructions to navigate through the menu and use the application:      
1. Upon running the application, you will be presented with a menu displaying various options.
2. Use the number keys to select an option and press Enter.
3. Depending on the chosen option, follow the prompts to register drivers, book rides, display information, or exit the application.
4. For any unexpected behavior or errors, refer to the error messages displayed for troubleshooting.

### Dependencies

- **Colorama:**: Used for colored terminal text to enhance UI readability.
- **SQLite3:**: Lightweight relational database management system used for local data storage.
- **Feedback**: Gather user feedback to improve usability and functionality.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or find any bugs, please open an issue or a pull request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

