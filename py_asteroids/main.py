import pygame

from src.abstractions.constants import *
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
        screen.fill(black)

# background with draw line function for a blue to black gradient
        # for y in range(SCREEN_HEIGHT):
        #     b_cval = int(127 * (y / SCREEN_HEIGHT))
        #     blue = (0, 0, b_cval)
        #     pygame.draw.line(screen, blue, (0, y), (SCREEN_WIDTH, y))

# shifting background with gradient
        for y in range(SCREEN_HEIGHT):
            grad_height = SCREEN_HEIGHT
            half_grad_height = SCREEN_HEIGHT / 2

            grad_pos = (y + bg_offset) % grad_height

            if grad_pos < grad_height/2 :
                b_cval = int(127 * (grad_pos / (half_grad_height)))
            else :
                b_cval = int(127 * (1 - (grad_pos - half_grad_height) / (half_grad_height)))
            blue = (0, 0, b_cval)
            pygame.draw.line(screen, blue, (0, y), (SCREEN_WIDTH, y))

#  refreshes screen 
        pygame.display.flip()

        bg_offset += 1  # increase for faster movement
        clock.tick(40)  # limit to 60 FPS
if __name__ == "__main__":
    main()
