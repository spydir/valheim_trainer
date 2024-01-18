# Valheim Skill Training Script

This Python script is designed to assist players in training their skills within the popular video game Valheim, which can be found on [Steam](https://store.steampowered.com/app/892970/Valheim/). The script utilizes the `pydirectinput` library and Windows API calls to automate key presses within the Valheim game window.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- The `pydirectinput` library installed. You can install it using pip:
  ```bash
  pip install pydirectinput
  ```
- Valheim installed and running on your Windows PC.

## Usage

1. Launch Valheim and enter the game.
2. Make sure the Valheim game window is active and visible.
3. Open the Python script in your preferred code editor or IDE.
4. Customize the following parameters within the script according to your specific skill training requirements:

   - `window_title`: Set this to match the title of your Valheim game window.
   - `delay_between_keypresses`: Adjust the delay (in seconds) between each keypress to control the rate of skill training.
   - `keystroke_to_send`: Define the key you want to send to the game. By default, it's set to "space" for jumping.
   - `num_keystrokes`: Specify the number of times you want to send the keystroke.

5. Save your changes.

6. Run the script. It will focus on the Valheim window, wait for a moment to ensure proper focus, and then start sending the designated keystroke repeatedly for the specified number of times.

7. Monitor the game to observe the skill training progress.

## Example Usage

The provided script is set to repeatedly press the spacebar (default) in Valheim for 10,000 times with a delay of 2.8 seconds between each press. You can modify the script to train other skills or use different keys as needed.

Remember to follow the game's terms of service and any community guidelines while using scripts for skill training.

## Disclaimer

This script is for educational and illustrative purposes. It's essential to use it responsibly and within the game's terms of service. Automated gameplay may be subject to game developer policies, and misuse could lead to consequences such as account suspension or banning.

Please use this script responsibly and enjoy your skill training in Valheim!