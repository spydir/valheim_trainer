import pydirectinput
import time
import win32gui
import win32con

# Define the target window's title (you can find this in the window's title bar)
window_title = "Valheim"

# Find the window handle by its title
window_handle = win32gui.FindWindow(None, window_title)

if window_handle == 0:
    print(f"Window '{window_title}' not found.")
    exit()

# Set the delay between key presses (in seconds)
delay_between_keypresses = 2.8


# Define the keystroke to send (you can change this to the desired key)
keystroke_to_send = "space"

# Number of times to send the keystroke
num_keystrokes = 10000

# Bring the target window to the foreground
win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(window_handle)

# Wait for a moment to focus on the window
time.sleep(1)

# Send the designated keystroke repeatedly
for _ in range(num_keystrokes):
    pydirectinput.press(keystroke_to_send)
    time.sleep(delay_between_keypresses)

print(f"Sent '{keystroke_to_send}' {num_keystrokes} times to '{window_title}'.")
