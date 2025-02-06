# -------------------------------------
# Medical System
# -------------------------------------
# This program manages workers and patients in a medical facility.
# Features:
# 1. Workers can sign in, check availability, view schedules, and clock out.
# 2. Patients can sign in and be listed in the system.
# 3. A main menu provides an interactive system for user interaction.

# -------------------------------------
# Data Storage
# -------------------------------------
# Workers Dictionary:
# - Key: Worker Name
# - Value: (ID Number, Room Number, Availability)
#
# Patients Dictionary:
# - Key: Patient Name
# - Value: Reason for Visit
# -------------------------------------

workers = {}
patients = {}

# -------------------------------------
# Worker Management Functions
# -------------------------------------

def add_worker():
    """
    Adds a worker to the system with an ID and assigned room.
    """
    name = input("\nEnter your name: ").strip()
    try:
        id_num = int(input("Enter your ID number: "))
        room_num = int(input("Enter your assigned room number: "))
    except ValueError:
        print("Invalid input! Please enter numbers for ID and Room.")
        return

    workers[name] = {"ID": id_num, "Room": room_num, "Availability": "No"}
    print(f"\n{name} has been successfully added to the system!")

def is_available():
    """
    Updates a worker's availability in the system.
    """
    name = input("\nEnter your name: ").strip()
    if name in workers:
        availability = input("Are you available? (Y/N): ").strip().lower()
        if availability in ("y", "yes"):
            workers[name]["Availability"] = "Yes"
            print(f"{name} is now available!")
        elif availability in ("n", "no"):
            workers[name]["Availability"] = "No"
            print(f"{name} is not available.")
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    else:
        print(f"{name} is not registered in the system.")

def view_workers():
    """
    Displays all registered workers along with their details.
    """
    if not workers:
        print("\nNo workers are currently registered.")
        return

    print("\n-----------------------------------------")
    print("| Name           | ID       | Room  | Availability |")
    print("-----------------------------------------")
    for name, details in workers.items():
        print(f"| {name:<14} | {details['ID']:<7} | {details['Room']:<5} | {details['Availability']:<11} |")
    print("-----------------------------------------")

def clock_out():
    """
    Removes a worker from the system when they clock out.
    """
    name = input("\nEnter your name: ").strip()
    if name in workers:
        workers.pop(name)
        print(f"\n{name} has successfully clocked out.")
    else:
        print(f"{name} is not registered or has already clocked out.")

# -------------------------------------
# Patient Management Functions
# -------------------------------------

def add_patient():
    """
    Registers a new patient with their reason for visiting.
    """
    name = input("\nEnter your name: ").strip()
    reason = input("What is the reason for your visit?: ").strip()

    if name in patients:
        print(f"{name} is already registered in the system.")
    else:
        patients[name] = reason
        print(f"\n{name} has been registered. Please wait to be called.")

def view_patients():
    """
    Displays all registered patients and their reasons for visiting.
    """
    if not patients:
        print("\nNo patients are currently registered.")
        return

    print("\n-----------------------------------------")
    print("| Patient Name   | Reason for Visit      |")
    print("-----------------------------------------")
    for name, reason in patients.items():
        print(f"| {name:<14} | {reason:<20} |")
    print("-----------------------------------------")

# -------------------------------------
# Main Menu System
# -------------------------------------

def main_menu():
    """
    Provides an interactive menu for managing workers and patients.
    """
    while True:
        print("\n--- Medical System Menu ---")
        print("1. Add Worker")
        print("2. Check Worker Availability")
        print("3. View Workers")
        print("4. Clock Out")
        print("5. Add Patient")
        print("6. View Patients")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_worker()
        elif choice == "2":
            is_available()
        elif choice == "3":
            view_workers()
        elif choice == "4":
            clock_out()
        elif choice == "5":
            add_patient()
        elif choice == "6":
            view_patients()
        elif choice == "7":
            print("\nExiting the Medical System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-7).")

# -------------------------------------
# Program Entry Point
# -------------------------------------
if __name__ == "__main__":
    main_menu()
