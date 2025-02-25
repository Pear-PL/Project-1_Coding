import tkinter as tk
from tkinter import messagebox

# Define fuel prices
Diesel = 29.94
G95 = 40.15
G91 = 39.88
E20 = 39.04
E85 = 32.34
Bensin = 47.56

Hybrid = 23
Gas = 15

# Function to calculate price
def calculate_price():
    try:
        # Get user input values
        distance = int(distance_entry.get())
        engine_type = engine_var.get()
        fuel_type = fuel_var.get()

        # Fuel price based on selection
        if fuel_type == "A":  # Diesel
            fuel_price = Diesel
        elif fuel_type == "B":  # G95
            fuel_price = G95
        elif fuel_type == "C":  # G91
            fuel_price = G91
        elif fuel_type == "D":  # E20
            fuel_price = E20
        elif fuel_type == "E":  # E85
            fuel_price = E85
        elif fuel_type == "F":  # Bensin
            fuel_price = Bensin
        else:
            raise ValueError("Invalid fuel type selected")

        # Fuel efficiency based on engine type
        if engine_type == "H":  # Hybrid
            fuel_efficiency = Hybrid
        elif engine_type == "G":  # Gas
            fuel_efficiency = Gas
        else:
            raise ValueError("Invalid engine type selected")

        # Calculate the price
        price = (distance / fuel_efficiency) * fuel_price
        result_label.config(text=f"ราคน้ำมันที่ควรเติมประมาณ: {'%.2f' % price} บาท")

    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")

# Initialize main window
root = tk.Tk()
root.title("คำนวณราคาน้ำมัน")

# Labels
distance_label = tk.Label(root, text="ระยะทาง (กิโลเมตร):")
distance_label.grid(row=0, column=0, padx=10, pady=5)

engine_label = tk.Label(root, text="ประเภทเครื่องยนต์ (G = Gas, H = Hybrid):")
engine_label.grid(row=1, column=0, padx=10, pady=5)

fuel_label = tk.Label(root, text="เลือกน้ำมัน (A = Diesel, B = G95, C = G91, D = E20, E = E85, F = Bensin):")
fuel_label.grid(row=2, column=0, padx=10, pady=5)

# Inputs
distance_entry = tk.Entry(root)
distance_entry.grid(row=0, column=1, padx=10, pady=5)

engine_var = tk.StringVar()
engine_var.set("H")  # Default to Hybrid
engine_menu = tk.OptionMenu(root, engine_var, "H", "G")
engine_menu.grid(row=1, column=1, padx=10, pady=5)

fuel_var = tk.StringVar()
fuel_var.set("A")  # Default to Diesel
fuel_menu = tk.OptionMenu(root, fuel_var, "A", "B", "C", "D", "E", "F")
fuel_menu.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate price
calculate_button = tk.Button(root, text="คำนวณราคา", command=calculate_price)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
