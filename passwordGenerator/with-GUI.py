import tkinter as tk
from tkinter import messagebox
import random

# Function to generate password
def generatePassword(length=16):
    lower =  "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-$£&!<>~@?¬"
    
    all = lower + upper + numbers + symbols
    password = "".join(random.sample(all, length))
    
    return password

# Function to handle the button click event
def generate_password():
    try:
        # Get the length from the user input
        length = int(entry_length.get())
        
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length must be greater than 0.")
        else:
            # Generate and display the password
            password = generatePassword(length)
            label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the password length.")

# Set up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")

# Label for instruction
label_instruction = tk.Label(window, text="Enter the length of your password:", font=("Helvetica", 12))
label_instruction.pack(pady=10)

# Entry box for password length
entry_length = tk.Entry(window, font=("Helvetica", 12), width=10)
entry_length.pack(pady=10)

# Button to generate the password
generate_button = tk.Button(window, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
label_result = tk.Label(window, text="Generated Password: ", font=("Helvetica", 12))
label_result.pack(pady=20)

# Start the main loop
window.mainloop()