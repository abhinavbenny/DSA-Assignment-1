"""
Student Record Management System
--------------------------------
A menu-driven console application that lets the user add, view, search,
update and delete student records. Records are stored in a JSON file so
that data is not lost when the program closes.

Concepts used: data types & variables, conditionals & loops, functions,
exception handling, file I/O, menu-driven design.
"""

import json
import os

DATA_FILE = os.path.join("data", "records.json")


# ---------------------------------------------------------------- File I/O
def load_records():
    """Read all records from the JSON file. Returns a list of dicts."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("Data file has an unexpected format.")
        return records
    except FileNotFoundError:
        # First run: no data yet, which is perfectly fine.
        return []
    except (json.JSONDecodeError, ValueError):
        print("Warning: data file is corrupted. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Error reading data file: {error}")
        return []


def save_records(records):
    """Write all records to the JSON file. Returns True on success."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving data: {error}")
        return False


# ---------------------------------------------------------- Input helpers
def get_non_empty_string(prompt):
    """Keep asking until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_integer(prompt, minimum=None, maximum=None):
    """Keep asking until the user enters a valid integer in range."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
        else:
            return value


def get_float(prompt, minimum, maximum):
    """Keep asking until the user enters a valid number in range."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Value must be between {minimum} and {maximum}.")


def get_email(prompt):
    """Ask for an email address with a simple format check."""
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            return email
        print("Invalid email. Example: name@example.com")


# -------------------------------------------------------- Record helpers
def generate_id(records):
    """Return the next unused integer ID."""
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def find_by_id(records, record_id):
    """Return the record with the given ID, or None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def print_record(record):
    """Print a single record in a readable format."""
    print(f"ID: {record['id']:<4} Name: {record['name']:<20} "
          f"Course: {record['course']:<10} Email: {record['email']:<25} "
          f"Marks: {record['marks']}")


# ------------------------------------------------------------ Operations
def add_record(records):
    """Create a new record and save it."""
    print("\n--- Add New Record ---")
    record = {
        "id": generate_id(records),
        "name": get_non_empty_string("Name: "),
        "course": get_non_empty_string("Course: "),
        "email": get_email("Email: "),
        "marks": get_float("Marks (0-100): ", 0, 100),
    }
    records.append(record)
    if save_records(records):
        print(f"Record added successfully with ID {record['id']}.")


def view_records(records):
    """Display every record."""
    print("\n--- All Records ---")
    if not records:
        print("No records found.")
        return
    for record in records:
        print_record(record)
    print(f"Total records: {len(records)}")


def search_records(records):
    """Search by ID or by (partial) name."""
    print("\n--- Search Records ---")
    print("1. Search by ID")
    print("2. Search by name")
    choice = get_integer("Choose (1-2): ", 1, 2)

    if choice == 1:
        record = find_by_id(records, get_integer("Enter ID: "))
        results = [record] if record else []
    else:
        keyword = get_non_empty_string("Enter name (or part of it): ").lower()
        results = [r for r in records if keyword in r["name"].lower()]

    if results:
        for record in results:
            print_record(record)
    else:
        print("No matching record found.")


def update_record(records):
    """Update fields of an existing record. Press Enter to keep a value."""
    print("\n--- Update Record ---")
    record = find_by_id(records, get_integer("Enter ID to update: "))
    if record is None:
        print("Record not found.")
        return

    print("Leave a field blank to keep the current value.")
    name = input(f"Name [{record['name']}]: ").strip()
    course = input(f"Course [{record['course']}]: ").strip()
    email = input(f"Email [{record['email']}]: ").strip()
    marks = input(f"Marks [{record['marks']}]: ").strip()

    if name:
        record["name"] = name
    if course:
        record["course"] = course
    if email:
        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            record["email"] = email
        else:
            print("Invalid email ignored; old value kept.")
    if marks:
        try:
            value = float(marks)
            if 0 <= value <= 100:
                record["marks"] = value
            else:
                print("Marks out of range; old value kept.")
        except ValueError:
            print("Invalid marks ignored; old value kept.")

    if save_records(records):
        print("Record updated successfully.")


def delete_record(records):
    """Delete a record after confirmation."""
    print("\n--- Delete Record ---")
    record = find_by_id(records, get_integer("Enter ID to delete: "))
    if record is None:
        print("Record not found.")
        return

    print_record(record)
    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == "y":
        records.remove(record)
        if save_records(records):
            print("Record deleted.")
    else:
        print("Deletion cancelled.")


# ------------------------------------------------------------------ Menu
def show_menu():
    print("\n===== Student Record Management =====")
    print("1. Add record")
    print("2. View all records")
    print("3. Search records")
    print("4. Update record")
    print("5. Delete record")
    print("6. Exit")


def main():
    records = load_records()
    actions = {
        1: add_record,
        2: view_records,
        3: search_records,
        4: update_record,
        5: delete_record,
    }

    while True:
        show_menu()
        try:
            choice = get_integer("Enter your choice (1-6): ", 1, 6)
        except (EOFError, KeyboardInterrupt):
            print("\nInput ended. Exiting.")
            break

        if choice == 6:
            print("Goodbye!")
            break

        try:
            actions[choice](records)
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            break
        except Exception as error:  # last-resort safety net
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
