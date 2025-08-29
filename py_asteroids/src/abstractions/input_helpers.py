import pygame
from src.abstractions.constants import *

def handle_mouse_click(mouse_pos, mouse_pressed, option_rects):
    selected_index = -1
    clicked = False
    for i, rect in enumerate(option_rects):
        if rect.collidepoint(mouse_pos):
            selected_index = i
            if mouse_pressed[0]:
                clicked = True
            break
    return selected_index, clicked

def calc_mouse_actions(option_rects):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    hovered, clicked = handle_mouse_click(mouse_pos,mouse_pressed,option_rects)
    return hovered,clicked

def handle_keyboard_inputs(selected,options,option_results):
    action = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return selected,'quit'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected = (selected - 1) % len(options)
            if event.key == pygame.K_DOWN:
                selected = (selected + 1) % len(options)
            if event.key == pygame.K_RETURN:
                action = "enter"
    return selected, action