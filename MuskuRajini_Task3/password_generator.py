import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text=" Random Password Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Include Letters",
    variable=letters_var
).pack()

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var
).pack()

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var
).pack()

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=40,
    font=("Arial", 12)
)
password_entry.pack(pady=15)


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length should be at least 4"
            )
            return

        chars = ""

        if letters_var.get():
            chars += string.ascii_letters

        if numbers_var.get():
            chars += string.digits

        if symbols_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror(
                "Error",
                "Select at least one character type"
            )
            return

        password = ''.join(
            random.choice(chars)
            for _ in range(length)
        )

        password_var.set(password)

        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid number"
        )


def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo(
            "Success",
            "Password copied to clipboard!"
        )


generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)
generate_btn.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password
)
copy_btn.pack(pady=5)

root.mainloop()