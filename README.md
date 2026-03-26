# Simple Login and Signup System with Appointment Booking

A command-line application that provides user authentication and online appointment booking functionality.

## Features

### User Management
- **Create Account**: Register a new user with username and password
- **Login**: Authenticate existing users
- **Data Persistence**: User credentials are stored securely in JSON format

### Appointment Booking
- **View Available Slots**: Browse available appointment times for the next 7 days (9 AM - 5 PM)
- **Book Appointment**: Select a time slot and provide a reason for the appointment
- **View My Appointments**: See all your scheduled appointments
- **Cancel Appointment**: Cancel any of your scheduled appointments

## How to Run

1. Make sure you have Python 3 installed on your system

2. Run the application:
   ```bash
   python "Simple log in and Sign Up System.py"
   ```

3. Follow the on-screen menu:
   - Choose option 1 to create a new account
   - Choose option 2 to login
   - Once logged in, you can book, view, or cancel appointments

## Data Storage

The application uses two JSON files for data persistence:
- `users.json`: Stores user credentials
- `appointments.json`: Stores appointment details

These files are automatically created when you first run the application.

## System Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Example Usage

1. Create an account with your desired username and password
2. Login with your credentials
3. From the main menu, select "Book Appointment"
4. Choose from the available time slots
5. Enter the reason for your appointment
6. View your appointments anytime from the main menu
7. Cancel appointments if needed

## Improvements from Original

This version includes the following improvements over the original simple login system:
- Fixed password validation bug in original code
- Added persistent data storage using JSON files
- Implemented complete appointment booking system
- Added proper menu navigation
- Enhanced user experience with clear prompts and feedback
- Input validation and error handling
