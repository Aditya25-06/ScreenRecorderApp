import tkinter as tk
from tkinter import filedialog
import threading
from recorder import record_screen

stop_flag = {"stop": False}

def start_recording():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".avi",
        filetypes=[("AVI files", "*.avi")]
    )
    
    if not file_path:
        return

    stop_flag["stop"] = False
    status_label.config(text="Status: Recording...", fg="green")

    threading.Thread(target=record_screen, args=(stop_flag, file_path)).start()

def stop_recording():
    stop_flag["stop"] = True
    status_label.config(text="Status: Stopped", fg="red")

# Create UI
app = tk.Tk()
app.title("Screen Recorder")
app.geometry("300x250")
app.resizable(False, False)

title = tk.Label(app, text="Screen Recorder", font=("Arial", 16))
title.pack(pady=10)

start_btn = tk.Button(app, text="▶ Start Recording", bg="green", fg="white",
                      width=20, command=start_recording)
start_btn.pack(pady=10)

stop_btn = tk.Button(app, text="⏹ Stop Recording", bg="red", fg="white",
                     width=20, command=stop_recording)
stop_btn.pack(pady=10)

status_label = tk.Label(app, text="Status: Idle", font=("Arial", 10))
status_label.pack(pady=20)

app.mainloop()
