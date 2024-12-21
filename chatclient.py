import tkinter as tk
import requests
from datetime import datetime

# Create the main window
window = tk.Tk()
window.title("Chat App")
window.configure(bg='#29292e')

# Create GUI elements
name_label = tk.Label(window, text="Enter your name:", background='#29292e', foreground='white')
name_label.pack(pady=7)

name_entry = tk.Entry(window)
name_entry.pack(pady=(0, 10))

message_label = tk.Label(window, text="Enter your message:", background='#29292e', foreground='white')
message_label.pack(pady=7)

message_entry = tk.Entry(window)
message_entry.pack(pady=(0, 10))

serverip = "10.145.52.231"

ip_label = tk.Label(window, text="Enter server IP:", background='#29292e', foreground='white')
ip_label.pack(pady=7)

ip_entry = tk.Entry(window)
ip_entry.insert(0, serverip)
ip_entry.pack(pady=(0, 10))

result_label = tk.Label(window, text="", background='#29292e')
result_label.pack()

chat_history_label = tk.Label(window, text="Chat History:", background='#29292e', foreground='white')
chat_history_label.pack(pady=(0, 10))

chat_history_text = tk.Text(window, height=10, width=50, foreground='white', background='#29292e')
chat_history_text.pack(pady=(0, 10))

s = requests.session()


def send_message():
    global serverip
    serverip = ip_entry.get()
    name = name_entry.get()
    message = message_entry.get()
    response = s.post('http://' + serverip + ':5000/send', json={'name': name, 'message': message})
    if response.status_code == 200:
        result_label.config(text="Message sent successfully.")
        update_chat_history(name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message)
        message_entry.delete(0, tk.END)  # Clear the input box
    else:
        result_label.config(text=f"Failed to send message. Status code: {response.status_code}")


def update_chat_history(sender, timestamp, message):
    formatted_message = f"{sender} ({timestamp}): {message}\n"
    chat_history_text.insert(1.0, formatted_message)  # Insert at the beginning


def get_messages():
    response = s.get('http://' + serverip + ':5000/get')
    if response.status_code == 200:
        messages = response.json()
        chat_history_text.delete(1.0, tk.END)  # Clear previous chat history
        for message in messages:
            sender = message['sender']
            timestamp = message['timestamp']
            text = message['text']
            update_chat_history(sender, timestamp, text)

    else:
        result_label.config(text=f"Failed to retrieve messages. Status code: {response.status_code}")


def auto_get_messages():
    get_messages()  # Retrieve messages initially
    window.after(5000, auto_get_messages)  # Schedule the next retrieval after 5 seconds


# Create GUI buttons
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Call auto_get_messages to start automatic retrieval
auto_get_messages()

# Create the GUI event loop
window.mainloop()