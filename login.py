import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
import subprocess

# Connect to the SQLite database
conn = sqlite3.connect('user_profiles.db')
c = conn.cursor()

# Create the 'user_profiles' table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS user_profiles
             (name TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def register():
    """
    Function to register a new user profile and store it in the database.
    """
    name = name_entry.get()
    password = password_entry.get()

    if name and password:
        # Check username length
        if len(name) > 32:
            messagebox.showerror("Error", "Username must be at most 32 characters long")
        # Check password requirements
        elif not re.search(r"\d", password) or not re.search(r"[!@#$%^&*()_+=\[\]{};':\"\\|,.<>\/?~-]", password):
            messagebox.showerror("Error", "Password must contain a number and a special character")
        else:
            # Check if the user already exists in the database
            c.execute("SELECT * FROM user_profiles WHERE name=?", (name,))
            existing_user = c.fetchone()
            if existing_user:
                messagebox.showerror("Error", "User already exists")
            else:
                # Insert the new user into the database with default wins and loss values
                c.execute("INSERT INTO user_profiles (name, password) VALUES (?, ?)", (name, password))
                conn.commit()
                messagebox.showinfo("Success", "Profile created successfully")
                with open("username.txt", "w") as file:
                    file.write(name)
                with open(f"{name}_wins.txt", "w") as file:
                    file.write("0")
                with open(f"{name}_loss.txt", "w") as file:
                    file.write("0")
                open_main_script()
    else:
        messagebox.showerror("Error", "All fields must be filled")

def login_profile():
    """
    Function to log in with an existing user profile.
    """
    name = name_entry.get()
    password = password_entry.get()

    if name and password:
        # Check if the user exists in the database
        c.execute("SELECT * FROM user_profiles WHERE name=? AND password=?", (name, password))
        result = c.fetchone()
        if result:
            with open(f"{name}_wins.txt", "r") as f:
                wins = f.read()
            with open(f"{name}_loss.txt", "r") as f:
                loss = f.read()
            messagebox.showinfo("Success", "Login successful")
            with open("username.txt", "w") as file:
                    file.write(name)
            with open(f"{name}_wins.txt", "w") as f:
                    f.write(wins)
            with open(f"{name}_loss.txt", "w") as f:
                    f.write(loss)
            open_main_script()
            #fucking nigga u chose int fuck you fuck you
        else:
            messagebox.showerror("Error", "Invalid username or password")
    else:
        messagebox.showerror("Error", "All fields must be filled")

def open_main_script():
    """
    Function to open the main.py script using subprocess.
    """
    subprocess.Popen(["python", "main.py"])
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("User Registration and Login")
root.geometry("300x200")
root.resizable(0, 0)

root.configure(bg='#29292e')

# Create the entry fields
name_label = tk.Label(root, text="Username:", background="#29292e", foreground="white") # Change bg & fg
name_label.pack(pady=(20, 5))

name_entry = tk.Entry(root, bg="#F0F0F0", relief="solid", bd=1)
name_entry.pack(pady=(2, 10))

password_label = tk.Label(root, text="Password:", background="#29292e", foreground="white") # Change bg & fg
password_label.pack()

password_entry = tk.Entry(root, show="*", bg="#F0F0F0", relief="solid", bd=1)
password_entry.pack(pady=(2, 10))

# Create the 'Register' button
register_button = tk.Button(root, text="Register", command=register, bg="#4CAF50", fg="white", relief="raised")
register_button.pack(pady=(0, 7))

# Create the 'Login' button
login_button = tk.Button(root, text="Login", command=login_profile, bg="#2196F3", fg="white", relief="raised")
login_button.pack()

# Start the main loop
root.mainloop()

# Close the connection to the database
conn.close()