import pydirectinput
import time
import win32gui
import win32con

def send_keystrokes(window_title, keystroke_to_send, num_keystrokes, delay_between_keypresses):
    # Find the window handle by its title
    window_handle = win32gui.FindWindow(None, window_title)

    if window_handle == 0:
        print(f"Window '{window_title}' not found.")
        return

    # Bring the target window to the foreground
    win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(window_handle)

    # Wait for a moment to focus on the window
    time.sleep(1)

    # Send the designated keystroke repeatedly
    for _ in range(num_keystrokes):
        pydirectinput.press(keystroke_to_send)
        time.sleep(delay_between_keypresses)

if __name__ == "__main__":
    window_title = "Valheim"
    keystroke_to_send = "space"
    num_keystrokes = 10000
    delay_between_keypresses = 2.8

    send_keystrokes(window_title, keystroke_to_send, num_keystrokes, delay_between_keypresses)
