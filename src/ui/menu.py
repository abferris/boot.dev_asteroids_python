import pygame

from src.core.constants import *
from src.core.background import set_solid_background

from src.ui.menu_inputs import handle_keyboard_inputs, calc_mouse_actions
from src.ui.menu_helpers import draw_menu, process_selection, draw_highscore



class Menu():
    def __init__(self, title:str, options:list, option_results:list, sub_title:str = None,title_color:tuple =(255,255,255)):
        self.options = options
        self.option_results = option_results
        self.selected = 0
        self.running = True
        self.title = title
        self.title_color = title_color
        self.sub_title = sub_title

    def run_menu(self, screen:pygame.Surface, clock:pygame.time.Clock, pacifist_mode):
        while self.running:
            set_solid_background((0,0,0), screen)

            option_rects = draw_menu(screen,self.title,self.sub_title,self.title_color,self.options,self.selected)

            # Highscores are being loaded repeatedly. Refactor to only do this once
            draw_highscore(screen, pacifist_mode)
            
            hovered,clicked = calc_mouse_actions(option_rects)   

            if hovered != -1:
                self.selected = hovered
            if clicked:
                return process_selection(self.selected,self.option_results)

            self.selected,key_action = handle_keyboard_inputs(self.selected,self.options,self.option_results)     

            if key_action == "enter":
                output = process_selection(self.selected, self.option_results)
                return output
            elif key_action == "quit":
                return False, False

            draw_menu(screen,self.title,self.sub_title,self.title_color,self.options,self.selected)

            pygame.display.flip()