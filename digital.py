import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')  # Get the current time
    clock_label.config(text=current_time)     # Update the label text
    root.after(1000, update_time)             # Schedule the function to run again in 1000 ms (1 second)

# Create a GUI window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for displaying the time
clock_label = tk.Label(root, font=('Arial', 48), bg='black', fg='white')
clock_label.pack(pady=20)

# Run the update_time function to initialize the clock
update_time()

# Start the GUI main loop
root.mainloop()
