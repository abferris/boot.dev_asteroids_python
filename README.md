# boot.dev_asteroids_python

## Objective

The point is to learn how to make a program in python. This will be accomplished by following a guide to making a clone of asteroids, using the boot.dev tutorial

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

If you would like to modify the game, you can change some of the constants in the constants.py file.
Do not edit the bottom of that file!

To reset your highscores, delete the content of data/highscores.json, or the file itself.



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
