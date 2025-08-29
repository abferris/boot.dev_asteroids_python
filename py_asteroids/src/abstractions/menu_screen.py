import pygame

from src.abstractions.background import *
from src.abstractions.constants import *
from src.abstractions.input_helpers import *
from src.abstractions.menu_helpers import *


def menu_screen(screen,clock):

    font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)
    
    options = ["Play", "Pacifist Mode", "Exit"]
    option_results = [(True,False), (True,True),(False,False)]
    selected = 0  
    
    running = True
    while running:
        set_solid_background((0,0,0)
        ,screen)
        
        title_text = font.render("ASTEROIDS", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        screen.blit(title_text, title_rect)

        
        
        option_rects = draw_menu(screen,options,selected,small_font)
        
        pygame.display.flip()
        clock.tick(60)

            
        hovered,clicked = handle_mouse_hover(option_rects)        

        if hovered != -1:
            selected = hovered
        if clicked:
            return process_selection(selected)

     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False, False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    return process_selection(selected)

    