import pygame
from src.abstractions.constants import *
from src.objects.player import Player
from src.abstractions.input_helpers import *
from src.abstractions.menu_helpers import *
from src.abstractions.background import *


class Menu():
    def __init__(self,title,  options,option_results, sub_title = None,title_color =(255,255,255) ):
        self.options = options
        self.option_results = option_results
        self.selected = 0
        self.running = True
        self.title = title
        self.font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 36)
        self.title_color = title_color
        self.sub_title = sub_title

    def run_menu(self,screen,clock):
        while self.running:
            set_solid_background((0,0,0), screen)

            option_rects = draw_menu(screen,self.title,self.sub_title,self.title_color,self.options,self.selected,self.font,self.small_font)
            
            hovered,clicked = calc_mouse_actions(option_rects)   
            if hovered != -1:
                self.selected = hovered
            if clicked:
                return process_selection(self.selected,self.option_results)

            self.selected,key_action = handle_keyboard_inputs(self.selected,self.options,self.option_results)     
            if key_action == "enter":
                return process_selection(self.selected, self.option_results)
            elif key_action == "quit":
                return False, Falseg

            draw_menu(screen,self.title,self.sub_title,self.title_color,self.options,self.selected,self.font,self.small_font)


            run_menu_loop(clock)