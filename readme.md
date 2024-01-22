# Valheim Skill Training Script

This Python script is designed to assist players in training their skills within the popular video game Valheim, which can be found on [Steam](https://store.steampowered.com/app/892970/Valheim/). The script utilizes the `pydirectinput` library and Windows API calls to automate key presses within the Valheim game window.

*Note: This is a proof of concept and a bit of a "template" that can be modified to fit other games in the future. If you're looking for a speed-run to 100 in all skills, just use the devcommands. 

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- The `pydirectinput` library installed. You can install it using pip:
  ```bash
  pip install pydirectinput
  ```
- Valheim installed and running on your Windows PC.

## In Game Setup

To get the best out of this training script, you need to build a two-square training room. Make sure it's in a safe location and that you have good fortifications or you'll wake up to a pile of rubble and no bed to respawn to. This two, square training room will help with Jump, Run, and Sneak.
![alt text](https://github.com/spydir/valheim_trainer/blob/main/screenshots/training_room.png)

## Usage
1. Launch Valheim and enter the game.
2. Make sure the Valheim game window is active and visible.
3. Enter your training room and close the door. This will keep your character contained.
4. Open the `trainer.py` script in your preferred code editor or IDE.
5. Follow the example usage from below.
6. Monitor the game to observe the skill training progress.

## Example Usage
To use trainer.py, run it from the command line with the desired action and optional parameters. Here are some examples:

- To perform a jump action:
`python trainer.py jump`

- To perform a run action:
`python trainer.py run`

- To perform a sneak action:
`python trainer.py sneak`

Remember to follow the game's terms of service and any community guidelines while using scripts for skill training.

## Disclaimer

This script is for educational and illustrative purposes. It's essential to use it responsibly and within the game's terms of service. Automated gameplay may be subject to game developer policies, and misuse could lead to consequences such as account suspension or banning.

Please use this script responsibly and enjoy your skill training in Valheim!