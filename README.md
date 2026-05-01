# JAWG Contacts

A simple, menu-driven contact manager to track people and organizations I work with during my JAWG internship. The program stores contacts in a JSON file and lets me add, view, search, update, delete, filter, and analyze my partners.

## Author

- **Name:** Asiwome Agbleze  
- **Course:** CMSC 1111  
- **Semester:** Spring 2026  
- **Project:** Capstone Project – JAWG Contacts

---

## Project Description

JAWG Contacts is a small console application written in Python. It helps me keep track of key people and organizations related to my internship, such as mentors, providers, interviewees, and community partners.

Each contact stores:

- Name  
- Organization  
- Role (for example: mentor, provider, interviewee)  
- Email address  
- A short note about how we are connected  

Contacts are stored in a JSON file so that they are saved between runs of the program. The application uses object-oriented programming (a `Contact` class), file handling, and simple data analysis to show how many contacts I have by role.

---

## Features Implemented

The final version of JAWG Contacts includes the features I planned in my first milestone:

1. **Add a new partner**
   - Prompts for name, organization, role, email, and a connection note.
   - Saves the new contact into `jawg_contacts.json`.

2. **See a list of all partners**
   - Reads all contacts from the JSON file.
   - Displays each contact in a readable, formatted way.

3. **Look up a specific partner**
   - Lets the user search by **name** or **organization** (case-insensitive).
   - Shows matching contacts, if any.

4. **Edit an existing contact**
   - Finds a contact by name.
   - For each field, the user can press Enter to keep the old value or type a new value.
   - Saves changes back to the JSON file.

5. **Delete a contact**
   - Finds a contact by name.
   - Removes the contact from the list and updates the JSON file.

6. **Filter partners by role**
   - Filters contacts by the role field (for example, "mentor" or "provider").
   - Displays only the contacts that match the selected role.

7. **Analyze contacts (data, APIs, or automation milestone)**
   - Counts how many contacts there are for each role.
   - Prints a summary in the terminal using `collections.Counter`.
   - Uses `matplotlib` to create a simple bar chart image
     (for example, `jawg_contacts_chart.png`) showing the number of contacts per role.

8. **User-friendly menu and loop**
   - Shows a numbered menu of options (1–8).
   - Runs in a loop until the user chooses to exit.
   - Handles invalid choices with a clear message.

---

## Python Modules Used

JAWG Contacts uses several Python modules and libraries:

- `datetime` – to display today’s date in the greeting.  
- `json` – to save and load contacts in a JSON file.  
- `os` – to check if the JSON file exists before loading.  
- `collections.Counter` – to count the number of contacts by role for analysis.  
- `matplotlib.pyplot` – to generate a bar chart showing contacts by role.  

All other functionality uses core Python features: functions, classes, loops, conditionals, lists, and dictionaries.

---

## Files in This Project

- `jawg_contacts.py`  
  Main Python script. Contains the `Contact` class, menu system, and all functions for adding, viewing, searching, editing, deleting, filtering, and analyzing contacts.

- `jawg_contacts.json`  
  JSON data file where contacts are stored. This file is created automatically the first time you add a contact.

- `jawg_contacts_chart.png` (optional / generated)  
  Bar chart image created by the analyze function, showing how many contacts there are for each role.

There may also be earlier milestone files (such as file-handling and OOP versions) included to show the development process across the semester.

---

## How to Run the Program

### Requirements

- **Python 3.x** installed on your computer.  
- **matplotlib** installed for the chart feature:

```bash
pip install matplotlib
```

*(On some systems you may use `python3` and `pip3` instead of `python` and `pip`.)*

### Steps to Run

1. **Download or clone the repository**

```bash
git clone https://github.com/Asi-Web/JAWG-Contacts.git
cd JAWG-Contacts
```

2. **Install `matplotlib` (if needed)**

```bash
pip install matplotlib
```

3. **Run the program**

On Windows:

```bash
python jawg_contacts.py
```

On macOS / Linux:

```bash
python3 jawg_contacts.py
```

4. **Use the menu**

- The program will greet you and show today’s date.
- You will see a numbered menu with options like:
  - 1 – Add a new contact  
  - 2 – View all contacts  
  - 3 – Search for a contact  
  - 4 – Edit a contact  
  - 5 – Delete a contact  
  - 6 – Filter contacts by role  
  - 7 – Analyze contacts by role  
  - 8 – Exit  

Type a number and press Enter to choose an option.

5. **View the saved data (optional)**

- Contacts are saved in `jawg_contacts.json` in the same folder as the script.
- The analysis chart (if created) is saved as `jawg_contacts_chart.png`.

---

## Notes for Presentation

- The project demonstrates:
  - Input/output and user interaction in the console.
  - Strings, lists, dictionaries, and loops.
  - File handling with JSON for persistent storage.
  - Object-Oriented Programming with a `Contact` class.
  - Simple data analysis with `Counter`.
  - A basic visualization using `matplotlib`.
- The code is commented and organized into reusable functions to make it easy to read and extend.

During the presentation, I will:
- Explain the purpose of JAWG Contacts and how it supports my internship work.
- Walk through the menu and show adding, viewing, searching, editing, deleting, filtering, and analyzing contacts.
- Show the JSON file and the bar chart image as examples of data storage and visualization.