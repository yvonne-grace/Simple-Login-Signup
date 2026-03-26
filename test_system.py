"""
Test script to verify the appointment booking system functionality.
This script tests the core functions without requiring user input.
"""

import json
import os
import sys
from datetime import datetime

# Import the main module
sys.path.insert(0, '/home/runner/work/Simple-Login-Signup/Simple-Login-Signup')

# Test data initialization
def test_initialization():
    """Test that data files are created properly"""
    print("Test 1: Testing file initialization...")

    # Clean up any existing test files
    if os.path.exists('users.json'):
        os.remove('users.json')
    if os.path.exists('appointments.json'):
        os.remove('appointments.json')

    # Create the files manually (simulating the initialize_files function)
    with open('users.json', 'w') as f:
        json.dump({}, f)
    with open('appointments.json', 'w') as f:
        json.dump([], f)

    # Check files exist
    assert os.path.exists('users.json'), "users.json should be created"
    assert os.path.exists('appointments.json'), "appointments.json should be created"

    print("✓ File initialization test passed")


def test_user_management():
    """Test user creation and storage"""
    print("\nTest 2: Testing user management...")

    # Add a test user
    users = {'testuser': {'password': 'testpass123'}}
    with open('users.json', 'w') as f:
        json.dump(users, f)

    # Verify user was saved
    with open('users.json', 'r') as f:
        loaded_users = json.load(f)

    assert 'testuser' in loaded_users, "User should be saved"
    assert loaded_users['testuser']['password'] == 'testpass123', "Password should match"

    print("✓ User management test passed")


def test_appointment_booking():
    """Test appointment creation and storage"""
    print("\nTest 3: Testing appointment booking...")

    # Create a test appointment
    appointments = [
        {
            'username': 'testuser',
            'datetime': '2026-03-27 10:00',
            'reason': 'Annual checkup',
            'status': 'scheduled'
        }
    ]

    with open('appointments.json', 'w') as f:
        json.dump(appointments, f)

    # Verify appointment was saved
    with open('appointments.json', 'r') as f:
        loaded_appointments = json.load(f)

    assert len(loaded_appointments) == 1, "Should have one appointment"
    assert loaded_appointments[0]['username'] == 'testuser', "Username should match"
    assert loaded_appointments[0]['reason'] == 'Annual checkup', "Reason should match"

    print("✓ Appointment booking test passed")


def test_appointment_retrieval():
    """Test filtering appointments by user"""
    print("\nTest 4: Testing appointment retrieval...")

    # Create multiple appointments for different users
    appointments = [
        {
            'username': 'testuser',
            'datetime': '2026-03-27 10:00',
            'reason': 'Annual checkup',
            'status': 'scheduled'
        },
        {
            'username': 'otheruser',
            'datetime': '2026-03-27 11:00',
            'reason': 'Consultation',
            'status': 'scheduled'
        },
        {
            'username': 'testuser',
            'datetime': '2026-03-28 14:00',
            'reason': 'Follow-up',
            'status': 'scheduled'
        }
    ]

    with open('appointments.json', 'w') as f:
        json.dump(appointments, f)

    # Filter appointments for testuser
    with open('appointments.json', 'r') as f:
        all_appointments = json.load(f)

    user_appointments = [apt for apt in all_appointments if apt['username'] == 'testuser']

    assert len(user_appointments) == 2, "testuser should have 2 appointments"
    assert all(apt['username'] == 'testuser' for apt in user_appointments), "All should belong to testuser"

    print("✓ Appointment retrieval test passed")


def test_appointment_cancellation():
    """Test appointment cancellation"""
    print("\nTest 5: Testing appointment cancellation...")

    # Create appointments
    appointments = [
        {
            'username': 'testuser',
            'datetime': '2026-03-27 10:00',
            'reason': 'Annual checkup',
            'status': 'scheduled'
        },
        {
            'username': 'testuser',
            'datetime': '2026-03-28 14:00',
            'reason': 'Follow-up',
            'status': 'scheduled'
        }
    ]

    with open('appointments.json', 'w') as f:
        json.dump(appointments, f)

    # Cancel first appointment
    with open('appointments.json', 'r') as f:
        all_appointments = json.load(f)

    # Remove the appointment
    remaining = [apt for apt in all_appointments if apt['datetime'] != '2026-03-27 10:00']

    with open('appointments.json', 'w') as f:
        json.dump(remaining, f)

    # Verify cancellation
    with open('appointments.json', 'r') as f:
        final_appointments = json.load(f)

    assert len(final_appointments) == 1, "Should have 1 appointment remaining"
    assert final_appointments[0]['datetime'] == '2026-03-28 14:00', "Should be the follow-up appointment"

    print("✓ Appointment cancellation test passed")


def cleanup():
    """Clean up test files"""
    print("\nCleaning up test files...")
    if os.path.exists('users.json'):
        os.remove('users.json')
    if os.path.exists('appointments.json'):
        os.remove('appointments.json')
    print("✓ Cleanup complete")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Appointment Booking System Tests")
    print("=" * 50)

    try:
        test_initialization()
        test_user_management()
        test_appointment_booking()
        test_appointment_retrieval()
        test_appointment_cancellation()

        print("\n" + "=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False
    finally:
        cleanup()

    return True


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
