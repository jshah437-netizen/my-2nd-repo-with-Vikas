import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # Works on Windows. For Linux/Mac replace with os.system sound command.

# ---------------- CLOCK -----------------
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# ---------------- ALARM -----------------
def alarm_thread(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "⏰ Time's up!")
            try:
                for i in range(5):   # Beep 5 times
                    winsound.Beep(1000, 500)
            except:
                print("Beep not supported, showing message only.")
            break
        time.sleep(1)

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    threading.Thread(target=alarm_thread, args=(alarm_time,), daemon=True).start()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

# ---------------- GUI -----------------
root = tk.Tk()
root.title("Clock + Alarm")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="black")

# Clock Display
clock_label = tk.Label(root, font=("Arial", 48), fg="cyan", bg="black")
clock_label.pack(pady=10)

# Alarm Inputs
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

hour = tk.StringVar(value="07")
minute = tk.StringVar(value="30")
second = tk.StringVar(value="00")

tk.Entry(frame, textvariable=hour, width=3, font=("Arial", 20)).grid(row=0, column=0, padx=5)
tk.Label(frame, text=":", font=("Arial", 20), fg="white", bg="black").grid(row=0, column=1)
tk.Entry(frame, textvariable=minute, width=3, font=("Arial", 20)).grid(row=0, column=2, padx=5)
tk.Label(frame, text=":", font=("Arial", 20), fg="white", bg="black").grid(row=0, column=3)
tk.Entry(frame, textvariable=second, width=3, font=("Arial", 20)).grid(row=0, column=4, padx=5)

# Set Alarm Button
tk.Button(root, text="Set Alarm", command=set_alarm, font=("Arial", 14), bg="green", fg="white").pack(pady=10)

update_time()
root.mainloop()
