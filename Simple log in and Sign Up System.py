import json
import os
from datetime import datetime, timedelta

# File paths for data storage
USERS_FILE = 'users.json'
APPOINTMENTS_FILE = 'appointments.json'

# Initialize data files if they don't exist
def initialize_files():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)
    if not os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'w') as f:
            json.dump([], f)

# Load users from file
def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

# Save users to file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# Load appointments from file
def load_appointments():
    with open(APPOINTMENTS_FILE, 'r') as f:
        return json.load(f)

# Save appointments to file
def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, 'w') as f:
        json.dump(appointments, f, indent=2)

# Create account
def create_account():
    print('\n=== Create Account ===')
    users = load_users()

    username = input('Enter username: ').strip()
    if username in users:
        print('Username already exists. Please try a different username.')
        return None

    password = input('Enter password: ').strip()
    if not password:
        print('Password cannot be empty.')
        return None

    users[username] = {'password': password}
    save_users(users)
    print('Your account has been created successfully!')
    return username

# Login
def login():
    print('\n=== Login ===')
    users = load_users()

    username = input('Enter username: ').strip()
    password = input('Enter password: ').strip()

    if username in users and users[username]['password'] == password:
        print('Logged in successfully!')
        return username
    else:
        print('Invalid credentials.')
        return None

# View available time slots
def view_available_slots():
    print('\n=== Available Time Slots ===')
    appointments = load_appointments()
    booked_slots = {apt['datetime'] for apt in appointments}

    # Generate next 7 days of slots
    available_slots = []
    current_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

    for day in range(7):
        for hour in range(9, 17):  # 9 AM to 5 PM
            slot_time = current_date + timedelta(days=day, hours=hour-9)
            slot_str = slot_time.strftime('%Y-%m-%d %H:%M')
            if slot_str not in booked_slots:
                available_slots.append(slot_str)

    if not available_slots:
        print('No available slots at the moment.')
        return []

    print('Available appointment slots:')
    for i, slot in enumerate(available_slots[:20], 1):  # Show first 20 slots
        print(f'{i}. {slot}')

    return available_slots[:20]

# Book appointment
def book_appointment(username):
    print('\n=== Book Appointment ===')
    available_slots = view_available_slots()

    if not available_slots:
        return

    try:
        choice = int(input('\nEnter slot number to book (or 0 to cancel): '))
        if choice == 0:
            print('Booking cancelled.')
            return

        if 1 <= choice <= len(available_slots):
            selected_slot = available_slots[choice - 1]
            reason = input('Enter reason for appointment: ').strip()

            appointments = load_appointments()
            new_appointment = {
                'username': username,
                'datetime': selected_slot,
                'reason': reason,
                'status': 'scheduled'
            }
            appointments.append(new_appointment)
            save_appointments(appointments)

            print(f'\nAppointment booked successfully for {selected_slot}!')
        else:
            print('Invalid slot number.')
    except ValueError:
        print('Invalid input. Please enter a number.')

# View my appointments
def view_my_appointments(username):
    print('\n=== My Appointments ===')
    appointments = load_appointments()
    user_appointments = [apt for apt in appointments if apt['username'] == username]

    if not user_appointments:
        print('You have no appointments.')
        return []

    print('Your appointments:')
    for i, apt in enumerate(user_appointments, 1):
        print(f"{i}. {apt['datetime']} - {apt['reason']} (Status: {apt['status']})")

    return user_appointments

# Cancel appointment
def cancel_appointment(username):
    print('\n=== Cancel Appointment ===')
    appointments = load_appointments()
    user_appointments = [apt for apt in appointments if apt['username'] == username]

    if not user_appointments:
        print('You have no appointments to cancel.')
        return

    print('Your appointments:')
    for i, apt in enumerate(user_appointments, 1):
        print(f"{i}. {apt['datetime']} - {apt['reason']} (Status: {apt['status']})")

    try:
        choice = int(input('\nEnter appointment number to cancel (or 0 to go back): '))
        if choice == 0:
            return

        if 1 <= choice <= len(user_appointments):
            apt_to_cancel = user_appointments[choice - 1]
            appointments = [apt for apt in appointments if not (
                apt['username'] == username and
                apt['datetime'] == apt_to_cancel['datetime']
            )]
            save_appointments(appointments)
            print('Appointment cancelled successfully!')
        else:
            print('Invalid appointment number.')
    except ValueError:
        print('Invalid input. Please enter a number.')

# Main menu after login
def main_menu(username):
    while True:
        print('\n=== Main Menu ===')
        print('1. Book Appointment')
        print('2. View My Appointments')
        print('3. Cancel Appointment')
        print('4. Logout')

        choice = input('\nEnter your choice: ').strip()

        if choice == '1':
            book_appointment(username)
        elif choice == '2':
            view_my_appointments(username)
        elif choice == '3':
            cancel_appointment(username)
        elif choice == '4':
            print('Logged out successfully!')
            break
        else:
            print('Invalid choice. Please try again.')

# Main program
def main():
    initialize_files()

    print('=== Welcome to Appointment Booking System ===')

    while True:
        print('\n1. Create Account')
        print('2. Login')
        print('3. Exit')

        choice = input('\nEnter your choice: ').strip()

        if choice == '1':
            create_account()
        elif choice == '2':
            username = login()
            if username:
                main_menu(username)
        elif choice == '3':
            print('Thank you for using our system. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
