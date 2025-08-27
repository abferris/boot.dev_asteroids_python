import pygame

from src.abstractions.constants import *
from src.abstractions.background import *

def main():
    pygame.init()
    dims = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(dims)
    clock = pygame.time.Clock()
    bg_offset = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# background with fill function plain black
        black = (0, 0, 0)
        set_solid_background(black, screen)
        
        # secondary color is a dark blue 
        bg_secondary = (0,0,82)
        bg_speed = .8
        # this sets up the gradient and makes it shift
        bg_offset = set_shifting_gradient(bg_secondary, screen,dims,bg_offset,bg_speed)

#  refreshes screen 
        # 90 fps
        run_loop(90,clock)
        # clock.tick(90)  # limit to 60 FPS
        # pygame.display.flip()
if __name__ == "__main__":
    main()
