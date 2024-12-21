import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
import time
import threading

def open_second_window():
    subprocess.Popen(['python','game2.py'])
root = tk.Tk()
root.title("Waiting For Player")
def wait_and_open():
    time.sleep(1)
    open_second_window()
    root.destroy()

# Screen size
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="gray23")

# Loading function
def loading_screen(root):
    label_frame = tk.Frame(root)
    label_frame.pack(expand=True)
    label_frame.configure(bg="gray90")

    label = ttk.Label(label_frame, text="MATCHING ...", font=("Arial", 40), background="gray90")
    label.pack(side=tk.TOP, padx=30, pady=25)
    
    # Progress bar style
    s = ttk.Style()
    s.theme_use('alt')
    s.configure("blue.Horizontal.TProgressbar", background='#d0d1d3', troughcolor= "gray23", thickness=5)

    progress = ttk.Progressbar(label_frame, orient='horizontal', value=100, length=500, style='blue.Horizontal.TProgressbar', mode='indeterminate')
    progress.pack(side=tk.TOP, padx=30, pady=25)
    progress.start(12)  # Adjust the speed of the progress bar animation by changing the value
    
# Delay 10s then open the game file
loading_screen(root)
thread = threading.Thread(target=wait_and_open)
thread.start()
root.mainloop()
# exit(0)

# root.destroy()

# def join_matchmaking(player_name):
#     url = 'http://localhost:5000/join'
#     payload = {'player_name': player_name}
#     response = requests.post(url, json=payload)
#     if response.status_code == 200:
#         print("Joined matchmaking successfully.")
#     else:
#         print(f"Failed to join matchmaking. Status code: {response.status_code}")

# def matchmake_players():
#     url = 'http://localhost:5000/matchmake'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         player1 = data['player1']
#         player2 = data['player2']
#         print(f"Matched players: {player1} and {player2}")
#     else:
#         print(f"Failed to perform matchmaking. Status code: {response.status_code}")

# def start_client():
#     player_name = "Player 1"  # Replace with the actual player name
#     join_matchmaking(player_name)
#     matchmake_players()

# # Start the client in a separate thread
# client_thread = threading.Thread(target=start_client)
# client_thread.start()



