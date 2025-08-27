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
        # screen.fill(black)
        set_solid_background(black, screen)
        

        bg_secondary = (60,0,0)
        set_shifting_gradient(bg_secondary, screen,dims,bg_offset)

#  refreshes screen 
        bg_offset += .6  # increase for faster movement

        run_loop(90,clock)
        # clock.tick(90)  # limit to 60 FPS
        # pygame.display.flip()
if __name__ == "__main__":
    main()
