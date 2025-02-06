import pyautogui
import time
import threading


RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"


ascii_art = RED + r"""
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
""" + RESET

credit_text = BLUE + "By Joshua M Clatney - Ethical Pentesting Enthusiast" + RESET
version_text = RED + "Version 1.00" + RESET


print(ascii_art)
print(credit_text)
print(version_text)
print("\nInstructions:")
print("  1. Press Enter to start the mouse jiggler.")
print("  2. Press Enter again to stop the jiggler.")
print("  3. Press Enter once more to exit the script.\n")


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


t = threading.Thread(target=jiggler_loop, daemon=True)
t.start()

try:
    
    input("Press Enter to start the jiggler...")
    jiggler_running = True
    print("Mouse Jiggler started. It will keep moving your mouse.")

    input("Press Enter to stop the jiggler...")
    jiggler_running = False
    print("Mouse Jiggler stopped.")

   
    input("Press Enter to exit the script...")
    print("Exiting script.")
finally:
 
    exit_event.set()
    t.join()