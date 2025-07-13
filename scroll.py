import pyautogui
import time
import keyboard  # Library to detect keypresses

# Settings for the scroll
scroll_amount = -100  # Scroll step (negative for down)
scroll_speed = 0.8  # Time delay between scrolls (lower is faster)

def smooth_scroll():
    # Get the current position of the mouse
    x, y = pyautogui.position()

    while True:  # Infinite loop for endless scrolling
        if keyboard.is_pressed('q'):  # Check if 'q' key is pressed
            print("Stopping the scrolling.")
            break  # Exit the loop and stop scrolling

        pyautogui.scroll(scroll_amount, x, y)  # Scroll down at the current mouse position
        time.sleep(scroll_speed)  # Wait for a short time to make it smooth

# Run the smooth scroll function
smooth_scroll()
