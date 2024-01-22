import argparse
import subprocess
import keypress

# Define the path to the keypress.py script
KEYPRESS_SCRIPT_PATH = "keypress.py"
window_title = "Valheim"

def run_keypress_script(keystroke_to_send, num_keystrokes, delay_between_keypresses):
    # Execute the keypress.py script with the specified parameters
    keypress.send_keystrokes(window_title, keystroke_to_send, str(num_keystrokes), str(delay_between_keypresses))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valheim Trainer")
    parser.add_argument("action", choices=["jump", "run", "sneak"], help="Choose the action to perform")
    parser.add_argument("--keystrokes", type=int, default=1000, help="Number of keystrokes")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between keypresses in seconds")

    args = parser.parse_args()

    if args.action == "jump":
        keypress.send_keystrokes(window_title, "space", 3, 2.8)
    
    elif args.action == "run":
        keypress.send_keystrokes(window_title, "w", 3, 10)
        run_keypress_script("w", 3, 10)

    elif args.action == "sneak":
        keypress.send_keystrokes(window_title, "ctrl", 1, 1)
        keypress.send_keystrokes(window_title, "w", 3, 10)
