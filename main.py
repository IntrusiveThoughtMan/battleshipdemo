import tkinter as tk
import subprocess
from tkinter import messagebox
from tkinter import *
root = tk.Tk()
root.title("Battleship Game")
root.configure(bg='#29292e')

# Screen height & width
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

title_label = tk.Label(root, text="BATTLESHIPS", font=("Arial", 60), background="#29292e", foreground="white")
title_label.pack(pady=20)
def chat() :
    import chatclient as chat 
 
    
def start_game():
    enter = subprocess.Popen(["python", "waiting.py"])
    root.destroy()
def exit_game():
    exit(0)

def open_profile():
    with open("username.txt", "r") as file:
        username = file.read().strip()

    try:    
        with open(f"{username}_wins.txt", "r") as file:
            wins = file.read().strip()
    except FileNotFoundError:
        wins = "0"

    try:
        with open(f"{username}_loss.txt", "r") as file:
            losses = file.read().strip()
    except FileNotFoundError:
        losses = "0"

    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")

    username_label_profile = tk.Label(profile_window, text="Welcome Back, {}!".format(username), font=("Arial", 20))
    username_label_profile.pack(pady=10)

    wins_label = tk.Label(profile_window, text=f"Wins: {wins}", font=("Arial", 20))
    wins_label.pack(pady=10)

    losses_label = tk.Label(profile_window, text=f"Losses: {losses}", font=("Arial", 20))
    losses_label.pack(pady=10)

def open_profile_window():
    with open("username.txt", "r") as file:
        username = file.read().strip()
    if username:
        open_profile()
    else:
        messagebox.showinfo("Profile", "No user found.")

start_button = tk.Button(root, text="Start", font=("Arial", 30), command=start_game, height=1, width=7, background="gray70", foreground="black")
start_button.pack(side=tk.TOP, pady=10)

profile_button = tk.Button(root, text="Profile", font=("Arial", 30), command=open_profile_window, height=1, width=7, background="gray70", foreground="black")
profile_button.pack(side=tk.TOP, pady=10)

chat_button = tk.Button(root, text="Chat", font=("Arial", 30), command=chat, height=1, width=7, background="gray70", foreground="black")
chat_button.pack(side=tk.TOP, pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 30), command=exit_game, height=1, width=7, background="gray70", foreground="black")
exit_button.pack(side=tk.TOP, pady=(0, 15))

advertising_label = tk.Label(root, text="Advertising Goes Here", font=("Arial", 12), background="#29292e", foreground="white")
advertising_label.pack(pady=20)

root.mainloop()