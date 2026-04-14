## Asiwome Agbleze
## CMSC 111/1
## Assignment 3 -Capstone Project - Strings and Data Structures
from datetime import datetime
# # JAWG Contacts -Milestone 3
# Simple text-based contact tracker for internship partners

# This functin displays the welcome message
# 1. Greet user and explain what the program is about
today = datetime.now()
print("Welcome to JAWG Contacts!")
print("This simple program helps you track people and organizations from JAWG.")
print ("Today's date:"), today.strftime("%B %d, %Y")
print()

# Create a list to store contacts
contacts = []

# Ask user what they want to do
print("What would you like to do?")
print("1. Add a new contact")
print("2. View an example contact")

action_choice = input("Enter 1 or 2: ")

if action_choice == "1"
    print("\nGreat! Let's add a new contact.\n")

    contact_name = input("Contact's name: ")
    organization = input("Organization: ")
    role = input("Role (for example: mentor, provider, interviewee): ")
    email = input("Email address: ")
    connection_not = input("How are you connected to this person or organization? ")


# Store contact information in a dictionary
contact = {
    "name": contact_name,
    "organization": organization,
    "role": role,
    "email": email,
    "connection": connection_note
    }

# Add dictionary to the list
contacts.append(contact)

# Show the stored contact by looping through the dictionary
print("\nYou added this contact to JAWG Contacts:")
for key, value in contact.items():
    print(f"{key}: {value}")

elif action_choice == "2":
# Store example contact in a dictionary
example_contact {
"Name: Dr. Wairimu Mwangi")
"Organization: JAWG Community Health Clinic")
"Role: Mentor")
"Email: mwangiwairimutri@gmail.com")
"Connection: Supervises my internship project.")
}
# Add example contact to the list
display_contact(example_contact)

# Display example contact using a loop
print("\nExample contact in JAWG Contacts:")
for key, value in example_contact.items ():
    print(f"{key}: {value}")

else:
    print("\nThat was not a valid option.")
    print("Please run JAWG Contacts again and choose 1 or 2.")







