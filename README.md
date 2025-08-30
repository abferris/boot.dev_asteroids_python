# boot.dev_asteroids_python

## Objective

The point is to learn how to make a program in python. This will be accomplished by following a guide to making a clone of asteroids, using the boot.dev tutorial

## Rules of the game

This is the arcade classic, asteroids. For those of you who know, that's all you need.

For those who don't know this game, you are a ship in space. The map wraps horizontally and vertically. Asteroids spawn at random on the edges of the map and at increasing rates as time goes on. 
If you are hit by an asteroid, you blow up. Your ship moves with accelleration, and has drag, which will eventually slow it down. You can accellerate forward, backwards, or rotate clockwise or counterclockwise.
Your ship (unless you are in pacifist mode) has a weapon. When the weapon shot it will go off the screen twice before disappearing.
If it comes into a contact with an asteroid, the asteroid will be hit. There are multiple sizes of asteroids. If the asteroid is hit, it will become 2 asteroids one size smaller. They fly at 45 degrees from the asteroid's original trajectory in both directions at twice the original speed.
If the asteroid is the smallest size, there will be no children asteroids created.
The game goes on until you are destroyed by hitting an asteroid

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
  - potentially gain a life after a certain amount of points]
- make the singular highscore into a leaderboard
- allow for initials to be inserted with a high score