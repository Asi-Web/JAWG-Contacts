##Asiwome Agbleze
## CMSC 111/1
## Final Project -app.py

# Import the Flask tools we need to build web pages, handle forms,
# manage user sessions, and show messages to the user.
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Import sqlite3 so we can connect to a small local database file.
import sqlite3

# Import password tools so we do not store plain-text passwords.
from werkzeug.security import generate_password_hash, check_password_hash


# Create the Flask application.
app = Flask(__name__)

# Secret key is used for sessions and flash messages.
# In a real production app, this should be hidden in an environment variable.
app.secret_key = "jawg_secret_key"

# Name of the SQLite database file.
DATABASE = "database.db"


# This function creates and returns a connection to the SQLite database.
# row_factory lets us access columns by name instead of only by number.
def get_db_connection():
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as error:
        print("Database connection error:", error)
        return None


# This function creates the tables if they do not already exist.
# We create one table for users and one table for contacts.
def init_db():
    connection = get_db_connection()

    # If connection fails, stop the function early.
    if connection is None:
        print("Could not initialize the database.")
        return

    try:
        cursor = connection.cursor()

        # Create the users table.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)

        # Create the contacts table.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                organization TEXT NOT NULL,
                role TEXT NOT NULL,
                email TEXT NOT NULL,
                connection TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

        connection.commit()
        print("Database initialized successfully.")

    except sqlite3.Error as error:
        print("Database setup error:", error)

    finally:
        connection.close()


# This route shows the home page.
@app.route("/")
def home():
    return render_template("index.html")


# This route allows a new user to register.
# GET shows the form, POST processes the form.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get the values entered in the form.
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Basic form validation.
        if not username or not email or not password:
            flash("All fields are required.", "danger")
            return render_template("register.html")

        # Hash the password before storing it.
        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        if connection is None:
            flash("Could not connect to the database.", "danger")
            return render_template("register.html")

        try:
            cursor = connection.cursor()

            # Insert the new user into the users table.
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )

            connection.commit()
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("login"))

        # This error happens if the email already exists because email is unique.
        except sqlite3.IntegrityError:
            flash("That email is already registered.", "warning")

        except sqlite3.Error as error:
            flash("Database error while registering user.", "danger")
            print("Register error:", error)

        finally:
            connection.close()

    return render_template("register.html")


# This route logs a user into the application.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the login form values.
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Make sure the fields are not empty.
        if not email or not password:
            flash("Please enter both email and password.", "warning")
            return render_template("login.html")

        connection = get_db_connection()

        if connection is None:
            flash("Could not connect to the database.", "danger")
            return render_template("login.html")

        try:
            # Find the user by email.
            user = connection.execute(
                "SELECT * FROM users WHERE email = ?",
                (email,)
            ).fetchone()

            # Check if user exists and password is correct.
            if user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["username"] = user["username"]

                flash("Login successful.", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid email or password.", "danger")

        except sqlite3.Error as error:
            flash("Database error while logging in.", "danger")
            print("Login error:", error)

        finally:
            connection.close()

    return render_template("login.html")


# This route logs the user out by clearing the session.
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


# This route shows all contacts for the logged-in user.
# It also supports a simple search.
@app.route("/dashboard")
def dashboard():
    # Make sure the user is logged in.
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    # Get search text from the URL if the user typed one.
    search = request.args.get("search", "").strip()

    connection = get_db_connection()

    if connection is None:
        flash("Could not connect to the database.", "danger")
        return render_template("dashboard.html", contacts=[], search=search)

    try:
        # If there is a search term, search by name, organization, or role.
        if search:
            contacts = connection.execute("""
                SELECT * FROM contacts
                WHERE user_id = ?
                AND (
                    name LIKE ?
                    OR organization LIKE ?
                    OR role LIKE ?
                )
            """, (
                session["user_id"],
                f"%{search}%",
                f"%{search}%",
                f"%{search}%"
            )).fetchall()
        else:
            # If no search term, show all contacts for the user.
            contacts = connection.execute(
                "SELECT * FROM contacts WHERE user_id = ?",
                (session["user_id"],)
            ).fetchall()

    except sqlite3.Error as error:
        flash("Database error while loading contacts.", "danger")
        print("Dashboard error:", error)
        contacts = []

    finally:
        connection.close()

    return render_template("dashboard.html", contacts=contacts, search=search)


# This route allows the logged-in user to add a new contact.
@app.route("/add", methods=["GET", "POST"])
def add_contact():
    # Make sure the user is logged in.
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Get the form values.
        name = request.form.get("name", "").strip()
        organization = request.form.get("organization", "").strip()
        role = request.form.get("role", "").strip()
        email = request.form.get("email", "").strip()
        connection_note = request.form.get("connection", "").strip()

        # Basic validation so user cannot submit empty fields.
        if not name or not organization or not role or not email or not connection_note:
            flash("All contact fields are required.", "warning")
            return render_template("add_contact.html")

        connection = get_db_connection()

        if connection is None:
            flash("Could not connect to the database.", "danger")
            return render_template("add_contact.html")

        try:
            # Insert the new contact into the contacts table.
            connection.execute("""
                INSERT INTO contacts (name, organization, role, email, connection, user_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, organization, role, email, connection_note, session["user_id"]))

            connection.commit()
            flash("Contact added successfully.", "success")
            return redirect(url_for("dashboard"))

        except sqlite3.Error as error:
            flash("Database error while adding contact.", "danger")
            print("Add contact error:", error)

        finally:
            connection.close()

    return render_template("add_contact.html")


# This route allows the user to edit a contact by its ID.
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_contact(id):
    # Make sure the user is logged in.
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    connection = get_db_connection()

    if connection is None:
        flash("Could not connect to the database.", "danger")
        return redirect(url_for("dashboard"))

    try:
        # Find the contact that belongs to the current user.
        contact = connection.execute(
            "SELECT * FROM contacts WHERE id = ? AND user_id = ?",
            (id, session["user_id"])
        ).fetchone()

        # If the contact does not exist, show a message.
        if contact is None:
            flash("Contact not found.", "danger")
            return redirect(url_for("dashboard"))

        if request.method == "POST":
            # Get updated values from the form.
            name = request.form.get("name", "").strip()
            organization = request.form.get("organization", "").strip()
            role = request.form.get("role", "").strip()
            email = request.form.get("email", "").strip()
            connection_note = request.form.get("connection", "").strip()

            # Make sure no field is left empty.
            if not name or not organization or not role or not email or not connection_note:
                flash("All fields are required.", "warning")
                return render_template("edit_contact.html", contact=contact)

            # Update the contact in the database.
            connection.execute("""
                UPDATE contacts
                SET name = ?, organization = ?, role = ?, email = ?, connection = ?
                WHERE id = ? AND user_id = ?
            """, (name, organization, role, email, connection_note, id, session["user_id"]))

            connection.commit()
            flash("Contact updated successfully.", "success")
            return redirect(url_for("dashboard"))

        return render_template("edit_contact.html", contact=contact)

    except sqlite3.Error as error:
        flash("Database error while editing contact.", "danger")
        print("Edit contact error:", error)
        return redirect(url_for("dashboard"))

    finally:
        connection.close()


# This route deletes a contact by its ID.
@app.route("/delete/<int:id>", methods=["POST"])
def delete_contact(id):
    # Make sure the user is logged in.
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    connection = get_db_connection()

    if connection is None:
        flash("Could not connect to the database.", "danger")
        return redirect(url_for("dashboard"))

    try:
        # Delete only the contact that belongs to the current user.
        connection.execute(
            "DELETE FROM contacts WHERE id = ? AND user_id = ?",
            (id, session["user_id"])
        )

        connection.commit()
        flash("Contact deleted successfully.", "info")

    except sqlite3.Error as error:
        flash("Database error while deleting contact.", "danger")
        print("Delete contact error:", error)

    finally:
        connection.close()

    return redirect(url_for("dashboard"))


# This custom error page handles "Page Not Found" errors.
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1><p>Page not found.</p>", 404


# This custom error page handles general server errors.
@app.errorhandler(500)
def internal_server_error(error):
    return "<h1>500 Error</h1><p>Something went wrong on the server.</p>", 500


# This starts the Flask app.
# It also makes sure the database is created before the app runs.
if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5050, debug=True)

