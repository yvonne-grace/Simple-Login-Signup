"""
Demo script to showcase the appointment booking system.
This script simulates a user session without requiring interactive input.
"""

import json
import os
from datetime import datetime, timedelta

print("=" * 60)
print("APPOINTMENT BOOKING SYSTEM - DEMO")
print("=" * 60)

# Clean up any existing files
for file in ['users.json', 'appointments.json']:
    if os.path.exists(file):
        os.remove(file)

# Step 1: Initialize system
print("\n[SYSTEM] Initializing system...")
with open('users.json', 'w') as f:
    json.dump({}, f)
with open('appointments.json', 'w') as f:
    json.dump([], f)
print("✓ System initialized")

# Step 2: Create user accounts
print("\n[STEP 1] Creating user accounts...")
users = {
    'john_doe': {'password': 'john123'},
    'jane_smith': {'password': 'jane456'}
}
with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)
print("✓ Created accounts for: john_doe, jane_smith")

# Step 3: Book appointments for john_doe
print("\n[STEP 2] Booking appointments for john_doe...")
appointments = []

# Book 3 appointments
appointment_times = [
    (datetime.now() + timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0),
    (datetime.now() + timedelta(days=2)).replace(hour=14, minute=0, second=0, microsecond=0),
    (datetime.now() + timedelta(days=3)).replace(hour=11, minute=0, second=0, microsecond=0),
]

reasons = [
    'Annual checkup',
    'Follow-up consultation',
    'Dental cleaning'
]

for time, reason in zip(appointment_times, reasons):
    apt = {
        'username': 'john_doe',
        'datetime': time.strftime('%Y-%m-%d %H:%M'),
        'reason': reason,
        'status': 'scheduled'
    }
    appointments.append(apt)
    print(f"  ✓ Booked: {apt['datetime']} - {apt['reason']}")

# Book 1 appointment for jane_smith
jane_time = (datetime.now() + timedelta(days=4)).replace(hour=15, minute=0, second=0, microsecond=0)
appointments.append({
    'username': 'jane_smith',
    'datetime': jane_time.strftime('%Y-%m-%d %H:%M'),
    'reason': 'Specialist consultation',
    'status': 'scheduled'
})
print(f"  ✓ Booked for jane_smith: {jane_time.strftime('%Y-%m-%d %H:%M')} - Specialist consultation")

with open('appointments.json', 'w') as f:
    json.dump(appointments, f, indent=2)

# Step 4: View john_doe's appointments
print("\n[STEP 3] Viewing john_doe's appointments...")
with open('appointments.json', 'r') as f:
    all_appointments = json.load(f)

john_appointments = [apt for apt in all_appointments if apt['username'] == 'john_doe']
print(f"john_doe has {len(john_appointments)} appointments:")
for i, apt in enumerate(john_appointments, 1):
    print(f"  {i}. {apt['datetime']} - {apt['reason']} (Status: {apt['status']})")

# Step 5: Cancel one appointment
print("\n[STEP 4] Canceling john_doe's second appointment...")
apt_to_cancel = john_appointments[1]
remaining_appointments = [apt for apt in all_appointments if not (
    apt['username'] == 'john_doe' and apt['datetime'] == apt_to_cancel['datetime']
)]

with open('appointments.json', 'w') as f:
    json.dump(remaining_appointments, f, indent=2)
print(f"✓ Cancelled appointment on {apt_to_cancel['datetime']}")

# Step 6: View updated appointments
print("\n[STEP 5] Viewing updated appointments for john_doe...")
with open('appointments.json', 'r') as f:
    all_appointments = json.load(f)

john_appointments = [apt for apt in all_appointments if apt['username'] == 'john_doe']
print(f"john_doe now has {len(john_appointments)} appointments:")
for i, apt in enumerate(john_appointments, 1):
    print(f"  {i}. {apt['datetime']} - {apt['reason']} (Status: {apt['status']})")

# Step 7: Show available slots
print("\n[STEP 6] Checking available slots...")
booked_slots = {apt['datetime'] for apt in all_appointments}
available_count = 0
print("Sample available slots:")

current_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
for day in range(7):
    for hour in range(9, 17):
        slot_time = current_date + timedelta(days=day, hours=hour-9)
        slot_str = slot_time.strftime('%Y-%m-%d %H:%M')
        if slot_str not in booked_slots:
            if available_count < 10:  # Show first 10
                print(f"  • {slot_str}")
            available_count += 1

print(f"Total available slots: {available_count}")

# Step 8: Show system statistics
print("\n[SYSTEM STATISTICS]")
print(f"Total users: {len(users)}")
print(f"Total appointments: {len(all_appointments)}")
print(f"Active appointments: {len([apt for apt in all_appointments if apt['status'] == 'scheduled'])}")

# Cleanup
print("\n[CLEANUP] Removing demo files...")
for file in ['users.json', 'appointments.json']:
    if os.path.exists(file):
        os.remove(file)
print("✓ Demo files cleaned up")

print("\n" + "=" * 60)
print("DEMO COMPLETED SUCCESSFULLY")
print("=" * 60)
print("\nTo run the actual application, execute:")
print('  python3 "Simple log in and Sign Up System.py"')
print("=" * 60)
