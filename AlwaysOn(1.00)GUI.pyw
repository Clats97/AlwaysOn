import tkinter as tk
from tkinter import font
import threading
import time
import pyautogui

jiggler_running = False
exit_event = threading.Event()

def jiggler_loop():
    global jiggler_running
    while not exit_event.is_set():
        if jiggler_running:
            pyautogui.moveRel(10, 0, duration=0.2)  # move right
            time.sleep(2)
            pyautogui.moveRel(-10, 0, duration=0.2)  # move left
            time.sleep(2)
        else:
            time.sleep(0.1)

jiggler_thread = threading.Thread(target=jiggler_loop, daemon=True)
jiggler_thread.start()

def start_jiggler():
    global jiggler_running
    jiggler_running = True
    status_label.config(text="Status: Mouse Jiggler started. It is moving your mouse.")

def stop_jiggler():
    global jiggler_running
    jiggler_running = False
    status_label.config(text="Status: Mouse Jiggler stopped.")

def exit_program():
    exit_event.set()
    jiggler_thread.join(timeout=3)
    root.destroy()

def on_closing():
    exit_program()


root = tk.Tk()
root.title("AlwaysOn Mouse Jiggler v1.00")
root.protocol("WM_DELETE_WINDOW", on_closing)


frame = tk.Frame(root)
frame.pack(padx=10, pady=10)


ascii_art = r"""
 █████╗ ██╗     ██╗    ██╗ █████╗ ██╗   ██╗███████╗     ██████╗ ███╗   ██╗ 
██╔══██╗██║     ██║    ██║██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔═══██╗████╗  ██║
███████║██║     ██║ █╗ ██║███████║ ╚████╔╝ ███████╗    ██║   ██║██╔██╗ ██║
██╔══██║██║     ██║███╗██║██╔══██║  ╚██╔╝  ╚════██║    ██║   ██║██║╚██╗██║
██║  ██║███████╗╚███╔███╔╝██║  ██║   ██║   ███████║    ╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═╝  ╚═══╝

     ██╗██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗                      
     ██║██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗                     
     ██║██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝                     
██   ██║██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗                     
╚█████╔╝██║╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║                     
 ╚════╝ ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝                     
"""

credit_text = "By Joshua M Clatney - Ethical Pentesting Enthusiast"
version_text = "Version 1.00"
instructions_text = (
    "Instructions:\n"
    "  1. Click 'Start Jiggler' to start the mouse jiggler.\n"
    "  2. Click 'Stop Jiggler' to stop the jiggler.\n"
    "  3. Click 'Exit' to exit the program.\n"
)

monospace_font = font.Font(family="Courier", size=10)
ascii_label = tk.Label(frame, text=ascii_art, font=monospace_font, justify="left")
ascii_label.pack()

credit_label = tk.Label(frame, text=credit_text, fg="blue", font=("Helvetica", 12))
credit_label.pack(pady=(10, 0))

version_label = tk.Label(frame, text=version_text, fg="red", font=("Helvetica", 12))
version_label.pack()

instructions_label = tk.Label(frame, text=instructions_text, justify="left")
instructions_label.pack(pady=(10, 20))

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

start_button = tk.Button(buttons_frame, text="Start Jiggler", command=start_jiggler, width=15)
start_button.grid(row=0, column=0, padx=5)

stop_button = tk.Button(buttons_frame, text="Stop Jiggler", command=stop_jiggler, width=15)
stop_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(buttons_frame, text="Exit", command=exit_program, width=15)
exit_button.grid(row=0, column=2, padx=5)

status_label = tk.Label(root, text="Status: Idle", font=("Helvetica", 12))
status_label.pack(pady=10)

root.mainloop()