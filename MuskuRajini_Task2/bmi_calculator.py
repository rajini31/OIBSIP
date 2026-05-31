from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Function to calculate BMI
def calculate_bmi():
    try:
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be positive values.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        with open("bmi_records.txt", "a") as file:
            file.write(
                f"Date: {current_time}\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Weight: {weight} kg\n"
                f"Height: {height} m\n"
                f"BMI: {bmi:.2f}\n"
                f"Category: {category}\n"
                f"{'-'*40}\n"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Function to view records
def view_records():
    try:
        with open("bmi_records.txt", "r") as file:
            records = file.read()

        record_window = Toplevel(root)
        record_window.title("BMI Records")
        record_window.geometry("600x400")

        text_area = Text(record_window)
        text_area.pack(fill=BOTH, expand=True)

        text_area.insert(END, records)

    except FileNotFoundError:
        messagebox.showinfo("Info", "No records found.")

# Main Window
root = Tk()
root.title("Advanced BMI Calculator")
root.geometry("450x550")

# Heading
Label(
    root,
    text="Advanced BMI Calculator",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Name
Label(root, text="Name").pack()
name_entry = Entry(root, width=30)
name_entry.pack()

# Age
Label(root, text="Age").pack()
age_entry = Entry(root, width=30)
age_entry.pack()

# Gender
Label(root, text="Gender").pack()

gender_var = StringVar()
gender_var.set("Female")

Radiobutton(
    root,
    text="Female",
    variable=gender_var,
    value="Female"
).pack()

Radiobutton(
    root,
    text="Male",
    variable=gender_var,
    value="Male"
).pack()

# Weight
Label(root, text="Weight (kg)").pack()
weight_entry = Entry(root, width=30)
weight_entry.pack()

# Height
Label(root, text="Height (m)").pack()
height_entry = Entry(root, width=30)
height_entry.pack()

# Buttons
Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    width=20
).pack(pady=10)

Button(
    root,
    text="View Records",
    command=view_records,
    width=20
).pack()

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=20)

root.mainloop()