import tkinter as tk
from tkinter import StringVar
import time
import threading

def update_clock():
    """Updates the clock display every second."""
    while True:
        current_time.set(time.strftime('%H:%M:%S'))
        time.sleep(1)

def start_stopwatch():
    """Starts the stopwatch timer."""
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update_stopwatch()

def stop_stopwatch():
    """Stops the stopwatch timer."""
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time.time() - start_time

def reset_stopwatch():
    """Resets the stopwatch to 00:00:00."""
    global running, elapsed_time
    running = False
    elapsed_time = 0
    stopwatch_time.set("00:00:00")

def update_stopwatch():
    """Updates the stopwatch display while running."""
    while running:
        elapsed = time.time() - start_time
        minutes, seconds = divmod(int(elapsed), 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_time.set(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

# Create main application window
root = tk.Tk()
root.title("Stopwatch & Clock")

# Variables for clock and stopwatch
time_frame = tk.Frame(root)
time_frame.pack()
current_time = StringVar()
stopwatch_time = StringVar(value="00:00:00")

tk.Label(time_frame, textvariable=current_time, font=("Arial", 24)).pack()
threading.Thread(target=update_clock, daemon=True).start()

# Stopwatch UI
tk.Label(root, textvariable=stopwatch_time, font=("Arial", 24)).pack()

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Start", command=start_stopwatch).pack(side=tk.LEFT)
tk.Button(button_frame, text="Stop", command=stop_stopwatch).pack(side=tk.LEFT)
tk.Button(button_frame, text="Reset", command=reset_stopwatch).pack(side=tk.LEFT)

# Stopwatch state variables
running = False
start_time = 0
elapsed_time = 0

# Start the application loop
root.mainloop()
