from src.abstractions.constants import *
import pygame

def run_loop(fps,clock):
    clock.tick(fps)  
    pygame.display.flip()



def set_solid_background(rgb,screen):
    screen.fill(rgb)


def set_shifting_gradient(rgb,screen,dims, bg_offset = 0, speed=.3 ) :
    # assumes black background base
    win_width, win_height = dims
    for y in range(win_height):
            grad_height = win_height
            half_grad_height = win_height / 2

            grad_pos = (y + bg_offset) % grad_height
            rgb_list = []
            if grad_pos < half_grad_height :
                for val in rgb:
                    temp = int(val * (grad_pos / (half_grad_height)))
                    rgb_list.append(temp)
            else :
                for val in rgb:
                    temp = int(val * (1 - (grad_pos - half_grad_height) / (half_grad_height)))
                    rgb_list.append(temp)
            mod_rgb = tuple(rgb_list)
            pygame.draw.line(screen, mod_rgb, (0, y), (SCREEN_WIDTH, y))

    return bg_offset + speed

