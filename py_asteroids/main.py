import pygame

from src.abstractions.constants import *
from src.abstractions.background import *
from src.objects.player import Player
from src.objects.asteroid import Asteroid
from src.objects.asteroidfield import *

def main():
    pygame.init()
    dims = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(dims)
    clock = pygame.time.Clock()
    bg_offset = 0
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)
# background with fill function plain black
        black = (0, 0, 0)
        set_solid_background(black, screen)
        
        # secondary color is a dark blue 
        bg_secondary = (0,0,82)
        bg_speed = .8
        # this sets up the gradient and makes it shift
        bg_offset = set_shifting_gradient(bg_secondary, screen,dims,bg_offset,bg_speed)
        for obj in drawable:
            obj.draw(screen)
#  refreshes screen 
        # 90 fps
        dt = run_loop(60,clock)/1000
        # clock.tick(90)  # limit to 60 FPS
        # pygame.display.flip()
if __name__ == "__main__":
    main()
