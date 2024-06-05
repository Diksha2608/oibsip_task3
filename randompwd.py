import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
import string

password_length_entry = None 

def setup_gui(root):
    global password_entry, use_uppercase, use_lowercase, use_digits, use_special, password_length_entry

    # Password complexity variables
    use_uppercase = tk.BooleanVar(value=True)
    use_lowercase = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_special = tk.BooleanVar(value=True)
    password_length = tk.IntVar(value=12)
    
    # Title label
    tk.Label(root, text="Advanced Password Generator", font=("Helvetica", 23)).grid(row=0, columnspan=2, pady=10)

    # Password complexity options
    tk.Checkbutton(root, text="Include Uppercase Letters",font='arial 12', variable=use_uppercase).grid(row=1, column=0, sticky='w')
    tk.Checkbutton(root, text="Include Lowercase Letters",font='arial 12', variable=use_lowercase).grid(row=2, column=0, sticky='w')
    tk.Checkbutton(root, text="Include Digits",font='arial 12', variable=use_digits).grid(row=3, column=0, sticky='w')
    tk.Checkbutton(root, text="Include Special Characters",font='arial 12', variable=use_special).grid(row=4, column=0, sticky='w')

    # Password length option
    tk.Label(root, font='arial 15', text="Specify Password Length:").grid(row=5, column=0, sticky='w', pady=4)
    password_length_entry = tk.Text(root, height=1.5, width=5, font=("Helvetica", 16)) 
    password_length_entry.grid(row=5, column=1, sticky='w')
    password_length_entry.tag_configure("center", justify='center')
    password_length_entry.insert("1.0", "12", "center")  
    
    # Generate password button
    tk.Button(root,font='arial 14', text="Generate Password", command=generate_password).grid(row=6, columnspan=2, pady=15)

    # Generated password display
    password_entry = tk.Entry(root, width=30, font=("Helvetica", 14), justify='center')
    password_entry.grid(row=7, columnspan=2, pady=8)
    password_entry.config(state='readonly')

    # Copy to clipboard button
    tk.Button(root,font='arial 14', text="Copy to Clipboard", command=copy_to_clipboard).grid(row=8, columnspan=2, pady=5)

def generate_password():
    global password_length_entry  
    length_text = password_length_entry.get("1.0", "end-1c")  
    try:
        length = int(length_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return

    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1")
        return

    characters = ""
    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "At least one character set must be selected")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()  
    messagebox.showinfo("Info", "Password copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Advanced Password Generator")
    root.geometry("430x440+550+150")
    root.resizable(False, False)
    image_icon = PhotoImage(file="images/password.png")
    root.iconphoto(False, image_icon)

    setup_gui(root)
    root.mainloop()
