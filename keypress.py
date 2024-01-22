import pydirectinput
import time
import win32gui
import win32con
import argparse

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
    parser = argparse.ArgumentParser(description="Send keystrokes to a specified window.")
    parser.add_argument("window_title", help="Title of the target application window")
    parser.add_argument("keystroke_to_send", help="Keystroke to send (e.g., 'space', 'w', 's')")
    parser.add_argument("num_keystrokes", type=int, help="Number of times to send the keystroke")
    parser.add_argument("delay_between_keypresses", type=float, help="Delay in seconds between keypresses")

    args = parser.parse_args()

    send_keystrokes(args.window_title, args.keystroke_to_send, args.num_keystrokes, args.delay_between_keypresses)
