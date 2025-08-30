import sys
import pygame

from src.abstractions.constants import *
from src.abstractions.background import *
from src.abstractions.score_hud import *

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


pause_options,pause_results = ["Resume", "Restart", "Quit to Main Menu"],  ["resume", "restart", "quit"]

g_o_options, g_o_results = ["Restart", "Exit"],  [True, False]

def main():
    paused = False

    pygame.init()

    main_menu = Menu("Asteroids",main_menu_options, main_menu_options_results)

    dims = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(dims)
    clock = pygame.time.Clock()

    font = pygame.font.Font(None,36)
    bg_offset = 0
    highscore = load_highscore()

    play, pacifist_mode = main_menu.run_menu(screen, clock)
    
    if not play:
        return  
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,pacifist_mode)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    running = True

    
    last_time = pygame.time.get_ticks()

    while running:
        now = pygame.time.get_ticks()
        if not paused:
            dt = (now - last_time) / 1000  # seconds since last frame
            dt = min(dt, 0.05)
        else:
            dt = 0  # freeze time while paused
        last_time = now


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:

                    pause_menu = Menu("Paused", pause_options, pause_results,f"Current Score: {player.score}")
                    paused = not paused
                    choice = pause_menu.run_menu(screen, clock)
                    if choice == "resume":
                        paused = False
                    elif choice == "restart":
                        main()  
                        return
                    elif choice == "quit":
                        return 
                    continue

                        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                final_score = player.score
                scoreline = f"Score: {player.score} | Time: {player.survival_time:.2f}s"
                if update_highscore(final_score):
                    scoreline = f'''NEW HIGH SCORE!\n{scoreline}'''

                game_over_menu = Menu("Game Over",g_o_options, g_o_results, scoreline,(255, 0, 0))
                restart = game_over_menu.run_menu(screen,clock)
                if restart:
                    main()  
                else:
                    sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    asteroid.get_hit(dt,player)
                    shot.kill()

        black = (0, 0, 0)
        set_solid_background(black, screen)

        if BG_SECONDARY:
            bg_offset = set_shifting_gradient(BG_SECONDARY, screen,dims,bg_offset, BG_SPEED)

        for obj in drawable:
            obj.draw(screen)

        draw_hud(screen,player)
        pygame.display.flip()

    
    return output
        
if __name__ == "__main__":
    main()
