import tkinter as tk
from tkinter import Label
import psutil
import time

# Fenster erstellen
root = tk.Tk()
root.title("Mini System-Monitor")
root.geometry("400x200")  # Größe des Fensters
root.configure(bg="black")

# Labels
clock_label = Label(root, font=("Arial", 30), fg="lime", bg="black")
cpu_label = Label(root, font=("Arial", 20), fg="cyan", bg="black")
ram_label = Label(root, font=("Arial", 20), fg="yellow", bg="black")
temp_label = Label(root, font=("Arial", 20), fg="orange", bg="black")

clock_label.pack(pady=10)
cpu_label.pack()
ram_label.pack()
temp_label.pack()

def update():
    # Uhrzeit
    clock_label.config(text=time.strftime("%H:%M:%S"))
    
    # CPU-Auslastung
    cpu_label.config(text=f"CPU: {psutil.cpu_percent()}%")
    
    # RAM-Auslastung
    ram = psutil.virtual_memory()
    ram_label.config(text=f"RAM: {ram.percent}%")
    
    # CPU-Temperatur (nur auf Raspberry Pi)
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
        temp_label.config(text=f"Temp: {temp:.1f}°C")
    except:
        temp_label.config(text="Temp: N/A")

    # Alle 1 Sekunde aktualisieren
    root.after(1000, update)

update()
root.mainloop()
