# boot.dev_asteroids_python
**Author:** Aaron Ferris
**Github:** [github.com/abferris](https://github.com/abferris)
**Version:** 1.0
## Objective

The point is to learn how to make a program in python. This will be accomplished by following a guide to making a clone of asteroids, using the boot.dev tutorial

## Rules of the game

This is the arcade classic, asteroids. For those of you who know, that's all you need.

For those who don't know this game, you are a ship in space. The map wraps horizontally and vertically. Asteroids spawn at random on the edges of the map and at increasing rates as time goes on. 

If you are hit by an asteroid, you blow up. Your ship moves with accelleration, and has drag, which will eventually slow it down. You can accellerate forward, backwards, or rotate clockwise or counterclockwise.

Your ship (unless you are in pacifist mode) has a weapon. When the weapon shot it will go off the screen twice before disappearing.

If it comes into a contact with an asteroid, the asteroid will be hit. There are multiple sizes of asteroids. If the asteroid is hit, it will become 2 asteroids one size smaller. They fly at 45 degrees from the asteroid's original trajectory in both directions at twice the original speed.

If the asteroid is the smallest size, there will be no children asteroids created.

The game goes on until you are destroyed by hitting an asteroid.

##

Controls:

Accelleration (forward): Up Arrow or W
Decelleration (accellerate backwards): Down Arrow or S
Rotate Clockwise: Right Arrow or D
Rotate Counter Clockwise: Left Arrow or A
Shoot: Space Bar (This can be held down)
Pause: Escape or P

Menu Navigation:
Change Selection: Up/Down Arrow or Mouse Movement
Select Option: Enter or Click

## Pre-Requirement Installs

- python 
  - https://www.python.org/downloads/
- pip installer
  - https://pip.pypa.io/en/stable/installation/
- uv
  - pip install uv


## Running Instructions

Assuming you have python and pip
Commands to run to get this to work:
- git clone https://github.com/abferris/boot.dev_asteroids_python py_asteroids
- cd py_asteroids
- pip install uv
- uv run main

## Customization 

High scores are stored inside of the file highscores.json.
To reset your highscores, delete the content of data/highscores.json, or the file itself.

If you would like to modify the game, you can change some of the constants in the constants.py file.
Do not edit the bottom of that file!

Most constants are self evident, but this is a list of constants to change
- Screen Dimension
  - Width
  - Height
- Asteroid
  - Attributes
    - Minimum size
    - Number of different sizes 
      - larger sizes of asteroids are extra by the min size
      - example: 20 original size, wtih 4 kinds (20,40,60,80)
  - Spawn Attributes
    - base asteroid spawn rate (in seconds)
    - minimum asteroid spawn rate (in seconds)
    - time it takes for the spawn rate to get shorter (in seconds)
    - amount the spawn rate lessens by (in seconds)
- Player
  - size
  - movement
    - speed
    - accelleration
    - max speed
    - drag/friction
  - shot
    - shot cooldown (minimum time between shots)
    - shot speed (how fast it travels)
    - shot size

- background
  - secondary color
    - if shot secondary color doesn't exist, it will just be black
    - if the secondary color exists, the backgroudn will be a gradient that moves upwards
  - rate at which the background moves 



## Folder Structure

        py_asteroids/
        ├── main.py
        ├── pyproject.toml
        ├── src/
        │   ├── highscore.py
        │   ├── abstractions/
        │   │   ├── __init__.py
        │   │   ├── constants.py   # game constants which can be changed to mod the game
        │   │   ├── background.py  
        │   │   ├── input-helpers.py
        │   │   ├── menu_helpers.py
        │   │   └── score.hud.py
        │   ├── data/
        |   │   └── highscores.json # this is ignored and will be created when you first run the game
        │   └── objects
        │       ├── __init__.py   
        │       ├── asteroid.py
        │       ├── circleshape.py
        │       ├── menu.py
        │       ├── player.py
        |       └── shot.py
        ├── pyproject.toml
        └── README.md

## Future Improvements
- add the ability to use assets
  - potential to add background asset
  - replace triangle with a ship image
  - be able to replace asteroid circles with assets
    - potential for multiple asteroid assets
  - change the shot
    - make the shot color change
    - add a small explosion for shots connecting
- make an option for playing with lives
  - potentially gain a life after a certain amount of points
- make the singular highscore into a leaderboard
- allow for initials to be inserted with a high score
- powerups/debuffs
  - shot mods
    - multiple 
    - shot speed up
    - homing
    - explosive shot
  - ship mods
    - shield
    - accelleration
- allow for fullscreen mode/screen size changes
  - set up minimum screen size

## Screen Shots
Fig. 1: Home Screen

<img width="1286" height="748" alt="Screenshot 2025-08-30 014732" src="https://github.com/user-attachments/assets/9a1435cb-703f-43a8-84ec-3727b0c57326" />

Fig. 2: Gameplay

<img width="1287" height="750" alt="Screenshot 2025-08-30 014656" src="https://github.com/user-attachments/assets/c96220e7-1ecf-4750-95b7-a2a0790befa8" />

Fig. 3: Pause Screen

<img width="1287" height="749" alt="Screenshot 2025-08-30 014748" src="https://github.com/user-attachments/assets/7fc6bbbe-8726-450a-b8ee-861f169f4105" />

Fig. 4: Game Over menu

<img width="1289" height="750" alt="Screenshot 2025-08-30 014708" src="https://github.com/user-attachments/assets/1060a2a0-a4c2-4722-8d43-e551b0608dc0" />

