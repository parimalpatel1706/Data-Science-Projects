import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # cm to meter
        bmi = weight / (height ** 2)
        result = f"Your BMI is: {bmi:.2f}\n"

        if bmi < 18.5:
            result += "Category: Underweight"
        elif 18.5 <= bmi < 24.9:
            result += "Category: Normal weight"
        elif 25 <= bmi < 29.9:
            result += "Category: Overweight"
        else:
            result += "Category: Obese"

        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x280")
root.configure(bg="#eafaf1")

tk.Label(root, text="BMI Calculator", font=("Helvetica", 18, "bold"), bg="#eafaf1", fg="#2e7d32").pack(pady=10)

frame = tk.Frame(root, bg="#eafaf1")
frame.pack(pady=5)

tk.Label(frame, text="Enter your weight (kg):", bg="#eafaf1", fg="#333", font=("Arial", 11)).grid(row=0, column=0, pady=5, sticky="w")
weight_entry = tk.Entry(frame, font=("Arial", 11), width=20)
weight_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter your height (cm):", bg="#eafaf1", fg="#333", font=("Arial", 11)).grid(row=1, column=0, pady=5, sticky="w")
height_entry = tk.Entry(frame, font=("Arial", 11), width=20)
height_entry.grid(row=1, column=1, pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4caf50", fg="white",
          font=("Arial", 12, "bold"), padx=10, pady=6, activebackground="#66bb6a").pack(pady=20)

root.mainloop()
