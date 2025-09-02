import sys
import pygame

from src.abstractions.constants import *
from src.abstractions.background import *
from src.abstractions.score_hud import *
from src.abstractions.game_helpers import *

from src.objects.player import Player
from src.objects.asteroid import Asteroid
from src.objects.asteroidfield import *
from src.objects.menu import Menu
from src.objects.shot import Shot

from src.highscore import load_highscore, update_highscore



main_menu_options, main_menu_options_results = (
    ["Play", "Pacifist Mode", "Exit"], 
    [(True,False), (True,True),(False,False)]
)






def main():
    dimensions = SCREEN_WIDTH, SCREEN_HEIGHT

    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    clock = pygame.time.Clock()


    highscore = load_highscore()

    while True:
        main_menu = Menu("Asteroids",main_menu_options, main_menu_options_results)

        play, pacifist_mode = main_menu.run_menu(screen, clock)
    
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
