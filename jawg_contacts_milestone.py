## Asiwome Agbleze
## CMSC 111/1
## Asignment 7 - Mileston(data, APIs, or Automation)

from datetime import datetime
import json
import os
from collections import Counter
import matplotlib.pyplot as pltp

FILENAME = "jawg_contacts.json"
CHART_FILE = "jawg_contacts_chart.png"


class Contact:
    """Represents a single JAWG contact."""

    def __init__(self, name, organization, role, email, connection):
        self.name = name.strip()
        self.organization = organization.strip()
        self.role = role.strip()
        self.email = email.strip()
        self.connection = connection.strip()

    def to_dict(self):
        """Convert the Contact object into a dictionary."""
        return {
            "name": self.name,
            "organization": self.organization,
            "role": self.role,
            "email": self.email,
            "connection": self.connection
        }

    def display(self):
        """Display one contact in a readable format."""
        print("-" * 40)
        print(f"Name: {self.name}")
        print(f"Organization: {self.organization}")
        print(f"Role: {self.role}")
        print(f"Email: {self.email}")
        print(f"Connection: {self.connection}")


def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("Error: The contact file is not in a valid JSON format.")
        return []
    except OSError as e:
        print("Error reading file:", e)
        return []


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4)
    except OSError as e:
        print("Error saving contacts:", e)


def add_contact():
    """Add a new contact."""
    print("\nAdd a New Contact")
    name = input("Name: ")
    organization = input("Organization: ")
    role = input("Role (mentor, provider, interviewee, etc.): ")
    email = input("Email: ")
    connection = input("Connection note: ")

    new_contact = Contact(name, organization, role, email, connection)
    contacts = load_contacts()
    contacts.append(new_contact.to_dict())
    save_contacts(contacts)

    print("\nContact added successfully.")


def view_contacts():
    """Display all saved contacts."""
    contacts = load_contacts()

    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nAll JAWG Contacts")
    for contact_data in contacts:
        contact = Contact(
            contact_data["name"],
            contact_data["organization"],
            contact_data["role"],
            contact_data["email"],
            contact_data["connection"]
        )
        contact.display()


def search_contact():
    """Search contacts by name or organization."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts available to search.")
        return

    keyword = input("\nEnter a name or organization to search: ").strip().lower()
    matches = []

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["organization"].lower():
            matches.append(contact)

    if matches:
        print("\nSearch Results:")
        for contact_data in matches:
            contact = Contact(
                contact_data["name"],
                contact_data["organization"],
                contact_data["role"],
                contact_data["email"],
                contact_data["connection"]
            )
            contact.display()
    else:
        print("\nNo matching contact found.")


def edit_contact():
    """Edit an existing contact by name."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts available to edit.")
        return

    name_to_edit = input("\nEnter the name of the contact to edit: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name_to_edit:
            print("\nLeave a field blank if you do not want to change it.")

            new_name = input(f"New name [{contact['name']}]: ").strip()
            new_org = input(f"New organization [{contact['organization']}]: ").strip()
            new_role = input(f"New role [{contact['role']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()
            new_connection = input(f"New connection note [{contact['connection']}]: ").strip()

            if new_name:
                contact["name"] = new_name
            if new_org:
                contact["organization"] = new_org
            if new_role:
                contact["role"] = new_role
            if new_email:
                contact["email"] = new_email
            if new_connection:
                contact["connection"] = new_connection

            save_contacts(contacts)
            print("\nContact updated successfully.")
            return

    print("\nContact not found.")


def delete_contact():
    """Delete a contact by name."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts available to delete.")
        return

    name_to_delete = input("\nEnter the name of the contact to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name_to_delete:
            contacts.remove(contact)
            save_contacts(contacts)
            print("\nContact deleted successfully.")
            return

    print("\nContact not found.")


def filter_by_role():
    """Filter contacts by role."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts available to filter.")
        return

    role_filter = input("\nEnter a role to filter by: ").strip().lower()
    matches = [c for c in contacts if c["role"].lower() == role_filter]

    if matches:
        print(f"\nContacts with role: {role_filter}")
        for contact_data in matches:
            contact = Contact(
                contact_data["name"],
                contact_data["organization"],
                contact_data["role"],
                contact_data["email"],
                contact_data["connection"]
            )
            contact.display()
    else:
        print("\nNo contacts found for that role.")


def analyze_contacts():
    """Analyze contacts by role and create a bar chart."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts available to analyze.")
        return

    roles = [contact["role"] for contact in contacts]
    role_counts = Counter(roles)

    print("\nContact Analysis by Role")
    for role, count in role_counts.items():
        print(f"{role}: {count}")

    try:
        plt.figure(figsize=(8, 5))
        plt.bar(role_counts.keys(), role_counts.values(), color="skyblue")
        plt.title("JAWG Contacts by Role")
        plt.xlabel("Role")
        plt.ylabel("Number of Contacts")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(CHART_FILE)
        plt.show()
        print(f"\nChart saved as {CHART_FILE}")
    except Exception as e:
        print("\nCould not create chart.")
        print("Details:", e)


def display_menu():
    """Show the program menu."""
    print("\nJAWG Contacts Menu")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Filter contacts by role")
    print("7. Analyze contacts by role")
    print("8. Exit")


def main():
    """Main program loop."""
    today = datetime.now()
    print("Welcome to JAWG Contacts!")
    print("This program helps you track internship contacts and organizations.")
    print("Today's date:", today.strftime("%B %d, %Y"))

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            filter_by_role()
        elif choice == "7":
            analyze_contacts()
        elif choice == "8":
            print("\nGoodbye! Thanks for using JAWG Contacts.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
    
