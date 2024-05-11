import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = int(complexity_scale.get())

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

complexity_label = tk.Label(root, text="Password Complexity (1-4):")
complexity_label.pack()

complexity_scale = tk.Scale(root, from_=1, to=4, orient=tk.HORIZONTAL)
complexity_scale.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

# Run the main event loop
root.mainloop()
