Always On Jiggler  v1.02
By Joshua M Clatney - Ethical Pentesting Enthusiast
Modified by ik3a & IcedZ

Press Enter to start/stop the jiggler.
Type q + Enter to quit.


Running.

Stopped.
q
Exiting.
➜  ~ nano jiggly2.py
➜  ~ cat jiggly2.py
import threading
import pyautogui
import math
import time
import random

LTGRN, YELLOW, GREEN, RESET = "\033[92m", "\033[33m", "\033[0;32m", "\033[0m"

BANNER = (
    f"{LTGRN}Always On Jiggler{RESET}  v1.02\n"
    f"{YELLOW}By Joshua M Clatney - Ethical Pentesting Enthusiast{RESET}\n"
    f"{GREEN}Modified by ik3a & IcedZ{RESET}\n"
)

HEART_SIZE = 60
STEPS = 80
DRAW_DURATION = 3.0
PAUSE = random.randint(1, 42)

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0


def draw_heart(active, stop):
    """Move the cursor along a heart-shaped path."""

    start_x, start_y = pyautogui.position()

    points = []

    # Generate a parametric heart
    for i in range(STEPS + 1):
        t = 2 * math.pi * i / STEPS

        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        points.append((x, y))

    # Scale both axes to approximately 50 pixels
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    scale_x = HEART_SIZE / 32
    scale_y = HEART_SIZE / (max_y - min_y)

    # Place the heart relative to the current cursor position
    pixel_points = [
        (
            round(x * scale_x),
            round(-y * scale_y)
        )
        for x, y in points
    ]

    # Move to the first point
    prev_x, prev_y = 0, 0

    for x, y in pixel_points:
        if stop.is_set() or not active.is_set():
            break

        dx = x - prev_x
        dy = y - prev_y

        pyautogui.moveRel(dx, dy, duration=0)

        prev_x, prev_y = x, y

        if stop.wait(DRAW_DURATION / STEPS):
            break

    # Return to the original cursor position
    if not stop.is_set():
        pyautogui.moveTo(start_x, start_y, duration=0.2)


def jiggle(active, stop):
    """Repeatedly draw hearts while active."""

    while not stop.is_set():
        if active.is_set():
            draw_heart(active, stop)
            stop.wait(PAUSE)
        else:
            stop.wait(0.1)


def main():
    print(BANNER)
    print("Press Enter to start/stop the jiggler.")
    print("Type q + Enter to quit.\n")

    active = threading.Event()
    stop = threading.Event()

    thread = threading.Thread(
        target=jiggle,
        args=(active, stop),
        daemon=True
    )
    thread.start()

    try:
        while input().strip().lower() != "q":
            if active.is_set():
                active.clear()
                print("Stopped.")
            else:
                active.set()
                print("Running.")

    except (KeyboardInterrupt, EOFError):
        pass

    finally:
        stop.set()
        thread.join(timeout=2)
        print("Exiting.")


if __name__ == "__main__":
    main()
