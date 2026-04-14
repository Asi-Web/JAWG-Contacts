## Asiwome Agbleze
## CMSC 111/1
## Assignment 2 -Capstone Project - Loops and functions
from datetime import datetime
# # JAWG Contacts -Milestone 2
# Simple text-based contact tracker for internship partners

# This functin displays the welcome message
# 1. Greet user and explain what the program is about
today = datetime.now()
print("Welcome to JAWG Contacts!")
print("This simple program helps you track people and organizations from JAWG.")
print ("Today's date:"), today.strftime("%B %d, %Y")
print()

# 2. Inquire what the user wants (menu)
def show_menu():
print("What would you like to do?")
print("1. Add a new contact")
print("2. View an example contact")
print("3. Exist")

action_choice = input("Enter 1 or 2: ")

# This function creates and returns a contact dictionary
def add_contact ():
    print("\nGreat! Let's add a new contact.\n")

    contact_name = input("Contact's name: ")
    organization = input("Organization: ")
    role = input("Role (for example: mentor, provider, interviewee): ")
    email = input("Email address: ")
    connection_not = input("How are you connected to this person or organization? ")


return {
    "name": contact_name,
    "organization": organization,
    "role": role,
    "email": email,
    "connection": connection_note
    }

# This function displays one contact
def display_contact(contact):
    print("\nContact information:")
print(f"Name: {contact['name']}")
print(f"Organization: {contact['organization']}")
print(f"Role: {contact['role']}")
print(f"Email: {contact['email']}")
print(f"Connection: {contact['connection']}")
print()

# This function shows the example contact
def show_example_contact():
    example_contact = {
"Name: Dr. Wairimu Mwangi")
"Organization: JAWG Community Health Clinic")
"Role: Mentor")
"Email: mwangiwairimutri@gmail.com")
"Connection: Supervises my internship project.")
}
display_contact(example_contact)

# Main program
show_welcome()

running = True
contacts = []

while running:
    show_menu90
    action_action = input("Enter 1, 2, 3:")

    if action_choice == "1":
        new_contact = add_contact()
        contacts.append(new_contact)
        print("\nYou added this contact to JAWG Contacts:")
        display_contact(new_contact)

    elif action_choice == "2":
        show_example_contact()

    elif action_choice == "3":
        print("\nGoodbye! Thanks for using JAWG Contacts.")
        running = False

    else:
        print("\nThat was not a valid option.")
        print("Please choose 1, 2, or 3.\n")





