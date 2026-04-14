## Asiwome Agbleze
## CMSC 111/1
## Assignment 6 -Capstone Project -Error Handling
from datetime import datetime
# # JAWG Contacts -Milestone 6
# Simple text-based contact tracker for internship partners

# 1. Greet user and explain what the program is about
today = datetime.now()
print("Welcome to JAWG Contacts!")
print("This simple program helps you track people and organizations from JAWG.")
print ("Today's date:"), today.strftime("%B %d, %Y"))
print()

# 2. Inquire what the user wants 
print("What would you like to do?")
print("1. Add a new contact")
print("2. View an example contact")

action_choice = input("Enter 1 or 2: ")

# 3. Use if/ elif/ else to choose what happens
if action_choice == "1":
    #User wants to add a new contact
    print("\nGreat! Let's add a new contact.\n")

    contact_name = input("Contact's name: ")
    organization = input("Organization: ")
    role = input("Role (for example: mentor, provider, interviewee): ")
    email = input("Email address: ")
    connection_not = input("How are you connected to this person or organization? ")

    # 4. Show a summary using the variables
    print("\nYou added this contact to JAWG Contacts:")
    print(f"Name: {contact_name}")
    print(f"Organization: {organization}")
    print(f"Role: {role}")
    print(f"Email: {email}")
    print(f"Connection: {"connection_note"}")

elif action_choice == "2:":
    # User would chose to view an example instead of adding a contact
    print("\nExample contact in JAWG Contacts:")
    print("Name: Dr. Wairimu Mwangi")
    print("Organization: JAWG Community Healt Clinic")
    print("Role: Mentor")
    print("Email: mwangiwairimutri@gmail.com")
    print("Connection: Supervises my internship project.")

else:
    # User typed something other than 1 or 2
    print("\nThat was not a valid option.")
    print("Please run JAWG Contacts again and choose 1 or 2.")
if contact_name == "" or organization == "" or role == "" or email == "":
    print("\nError: name, organization, role and email cannot be blank.")
else:
    print("\nYou added this contact to JAWG Caontacts:")
    print(f"Name: {contact_name}")
    print(f"organization: {organization}")
    print(f"Role: {role}")
    print(f"Email: {email}")
    print(f"Connection: {connection_note}")
except ValueError:
print("\nInvalid input. Please try again.")

except Exception as e:
    print("\nSomething went wrong:", e)

