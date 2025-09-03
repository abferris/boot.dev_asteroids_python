import sys
import pygame

from src.core.constants import *
from src.core.background import *

from src.game.game_controller import run_game, handle_pause

from src.ui.menu import Menu
from src.core.highscore import load_highscore



main_menu_options, main_menu_options_results = (
    ["Play", "Pacifist Mode", "Exit"], 
    [(True,False), (True,True),(False,False)]
)






def main():
    dimensions = SCREEN_WIDTH, SCREEN_HEIGHT

    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    clock = pygame.time.Clock()

    highscore,pacifist_highscore = load_highscore()

    while True:
        main_menu = Menu("Asteroids",main_menu_options, main_menu_options_results)

        play, pacifist_mode = main_menu.run_menu(screen, clock, 2)
   
        if not play:
            return  
    
        result = run_game(screen, clock, pacifist_mode)

        if result == "quit":
            break
        elif result == "restart":
            continue

    pygame.quit()
    sys.exit()        
        
if __name__ == "__main__":
    main()
