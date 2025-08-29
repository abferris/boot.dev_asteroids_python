import sys
import pygame

from src.abstractions.constants import *
from src.abstractions.background import *
from src.abstractions.score_hud import *
from src.abstractions.menu_screen import *
from src.abstractions.game_over_screen import *


from src.objects.player import Player
from src.objects.asteroid import Asteroid
from src.objects.asteroidfield import *
from src.objects.menu import Menu
from src.objects.shot import Shot


main_menu_options, main_menu_options_results = (
    ["Play", "Pacifist Mode", "Exit"], 
    [(True,False), (True,True),(False,False)]
)


def main():
    pygame.init()
    main_menu = Menu("Asteroids",main_menu_options, main_menu_options_results)

    dims = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(dims)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,36)
    bg_offset = 0
    dt = 0
    survival_time = 0
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


    
    box_width, box_height = 200, 60
    box_x = SCREEN_WIDTH - box_width - 10  # 10 px from right
    box_y = 10  # 10 px from top
    box_color = (30, 30, 30)  # dark gray



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                g_o_options = ["Restart", "Exit"]
                g_o_results = [True, False]
                scoreline = f"Score: {player.score} | Time: {player.survival_time:.2f}s"
                game_over_menu = Menu("Game Over",g_o_options, g_o_results, scoreline,(255, 0, 0))
                restart = game_over_menu.run_menu(screen,clock)
                if restart:
                    main()  # restart the game
                else:
                    sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    asteroid.get_hit(dt,player)
                    shot.kill()

        black = (0, 0, 0)
        set_solid_background(black, screen)

        # this sets up the gradient and makes it shift
        if BG_SECONDARY:
            bg_offset = set_shifting_gradient(BG_SECONDARY, screen,dims,bg_offset, BG_SPEED)


        # draws objects
        for obj in drawable:
            obj.draw(screen)

        #score hud
        draw_hud(screen,player)
        
        # run the game loop
        dt = run_loop(60,clock)/1000
      # limit to 60 FPS





def run_loop(fps,clock):
    output = clock.tick(fps)  
    pygame.display.flip()
    return output
        
if __name__ == "__main__":
    main()
