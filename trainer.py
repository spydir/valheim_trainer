import argparse
import subprocess

# Define the path to the keypress.py script
KEYPRESS_SCRIPT_PATH = "keypress.py"
window_title = "Valheim"

def run_keypress_script(keystroke_to_send, num_keystrokes, delay_between_keypresses):
    # Execute the keypress.py script with the specified parameters
    subprocess.run(["python", KEYPRESS_SCRIPT_PATH, window_title, keystroke_to_send, str(num_keystrokes), str(delay_between_keypresses)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valheim Trainer")
    parser.add_argument("action", choices=["jump", "run", "sneak"], help="Choose the action to perform")
    parser.add_argument("--keystrokes", type=int, default=1000, help="Number of keystrokes")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between keypresses in seconds")

    args = parser.parse_args()

    if args.action == "jump":
        run_keypress_script("space", 3, 2.8)

    elif args.action == "run":
        run_keypress_script("w", 3, 10)

    elif args.action == "sneak":
        run_keypress_script("ctrl", 1, 1)
        run_keypress_script("w", 4, 1)
