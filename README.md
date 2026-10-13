# DSA-Assignment-1
# Student Record Management System

## Project Description
A menu-driven console application written in Python for managing student
records. Records can be added, viewed, searched, updated and deleted, and are
stored in a JSON file so data is kept after the program closes.

## Features
- Menu-driven interface (options 1-6)
- Add a record (ID is generated automatically)
- View all records
- Search by ID or by full/partial name (case-insensitive)
- Update a record (press Enter to keep a field unchanged)
- Delete a record with a confirmation prompt
- Input validation: empty values, invalid numbers, marks outside 0-100, bad emails
- Persistent storage in `data/records.json`
- Handles a missing, corrupted or unwritable data file without crashing

## Technologies / Concepts Used
- Python 3 (standard library only: `json`, `os`)
- Data types and variables: `int`, `float`, `str`, `list`, `dict`
- Conditional statements and loops: `if/elif/else`, `while`, `for`
- Functions: one function per operation and per input helper
- Exception handling: `ValueError`, `FileNotFoundError`, `json.JSONDecodeError`,
  `OSError`, `EOFError`, `KeyboardInterrupt`
- File I/O: reading and writing JSON with context managers (`with open`)
- Menu-driven console design with a dictionary mapping choices to functions

## How to Run
1. Install Python 3.8 or newer.
2. Clone the repository and open the folder:
   ```
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. Run:
   ```
   python3 record_manager.py
   ```
   (On Windows use `python record_manager.py`.)

The `data/` folder and `records.json` are created automatically on first save.

## Project Structure
```
record_manager.py   # application source code
data/records.json   # data file (created automatically)
screenshots/        # screenshots of the running application
REPORT.md           # assignment report
README.md
```

## Sample Input / Output
```
===== Student Record Management =====
1. Add record
2. View all records
3. Search records
4. Update record
5. Delete record
6. Exit
Enter your choice (1-6): 1

--- Add New Record ---
Name: Asha Nair
Course: MCA
Email: bad-email
Invalid email. Example: name@example.com
Email: asha@example.com
Marks (0-100): 105
Value must be between 0 and 100.
Marks (0-100): 88.5
Record added successfully with ID 1.

Enter your choice (1-6): 2

--- All Records ---
ID: 1    Name: Asha Nair            Course: MCA        Email: asha@example.com          Marks: 88.5
Total records: 1
```

## Screenshots
Add your screenshots to the `screenshots/` folder and link them here:

![Menu](screenshots/menu.png)
![Add record](screenshots/add.png)
![View records](screenshots/view.png)

## GitHub Repository
Repository: `<paste your repository link here>`
Author: Abhinav Benny Pallikkadavath
