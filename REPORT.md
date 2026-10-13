# Assignment 1 - Mini Project: Console Record-Management Application

**Name:** Abhinav Benny Pallikkadavath
**Course:** MCA
**Project:** Student Record Management System

## 1. Introduction
This project is a console application that manages student records. It
combines the core Python concepts covered in the course in one working
program: variables and data types, conditionals and loops, functions,
exception handling and file I/O, all behind a menu-driven interface.

## 2. Objectives
- Provide a menu to add, view, search, update and delete records
- Store records in a file so they persist between runs
- Validate all user input and handle errors without crashing

## 3. Design

### 3.1 Data structure
Each record is a dictionary; the collection is a list of dictionaries.

| Field  | Type  | Notes                      |
|--------|-------|----------------------------|
| id     | int   | Auto-generated, unique     |
| name   | str   | Non-empty                  |
| course | str   | Non-empty                  |
| email  | str   | Basic format check         |
| marks  | float | Range 0-100                |

### 3.2 Storage
Records are saved as JSON in `data/records.json`. The file is loaded at
start-up and rewritten after every add, update or delete.

### 3.3 Functions
| Function | Purpose |
|----------|---------|
| `load_records`, `save_records` | File I/O |
| `get_non_empty_string`, `get_integer`, `get_float`, `get_email` | Validated input |
| `generate_id`, `find_by_id`, `print_record` | Record helpers |
| `add_record`, `view_records`, `search_records`, `update_record`, `delete_record` | Operations |
| `show_menu`, `main` | Menu loop |

## 4. Concepts Applied
- **Data types and variables:** `int`, `float`, `str`, `list`, `dict`, constants (`DATA_FILE`).
- **Conditionals and loops:** `while True` for the menu and input retry loops; `for` to search and display; `if/elif` for menu and validation logic.
- **Functions:** each task is a separate function with a docstring.
- **Exception handling:** `ValueError` for bad numbers; `FileNotFoundError`, `JSONDecodeError` and `OSError` for file problems; `EOFError`/`KeyboardInterrupt` for ending input; a general `Exception` handler in the menu loop as a safety net.
- **File I/O:** `open()` inside `with` blocks, `json.load` and `json.dump`, `os.makedirs` to create the data folder.
- **Menu-driven design:** a dictionary maps menu numbers to functions.

## 5. Testing
| Test | Input | Result |
|------|-------|--------|
| View with no data | Option 2 | "No records found." |
| Add valid record | Valid values | Record added, saved to file |
| Invalid email | `bad-email` | Rejected, asked again |
| Marks out of range | `105` | Rejected, asked again |
| Marks not a number | `abc` | Rejected, asked again |
| Empty name | blank | Rejected, asked again |
| Search by name | `nai` | Matching record shown |
| Search unknown ID | `99` | "No matching record found." |
| Update record | New course and marks | Values changed and saved |
| Update unknown ID | `99` | "Record not found." |
| Delete, answer `n` | - | Deletion cancelled |
| Delete, answer `y` | - | Record removed and saved |
| Menu choice `9` | - | "Value must be at most 6." |
| Corrupted data file | `{bad` | Warning shown, starts empty |
| Restart program | - | Saved records still present |

Add screenshots of these runs in the `screenshots/` folder.

## 6. Conclusion
The application meets the requirements: it is menu-driven, uses functions,
validates input, handles file and runtime errors, and keeps data between
runs. Possible improvements: sorting, exporting to CSV, and a graphical
interface.
