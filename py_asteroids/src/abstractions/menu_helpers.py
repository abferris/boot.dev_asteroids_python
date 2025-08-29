from src.abstractions.constants import *
import pygame

def draw_menu(screen,title,sub_title,title_color,options,selected,big_font,small_font,):
    #menu title
    title_text = big_font.render(title, True, title_color)    
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(title_text, title_rect)

    #menu subtitle
    if sub_title:
        sub_title_text = small_font.render((sub_title), True, (255, 255, 255))
        sub_title_rect = sub_title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
        screen.blit(sub_title_text, sub_title_rect)



    # menu items
    output = []
    for i, option in enumerate(options):
        color = (255, 255, 0) if i == selected else (255, 255, 255)
        
        text = small_font.render(option, True, color)
        rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i * 50))
        screen.blit(text, rect)
        output.append(rect)
    return output

def process_selection(selected,options_results):
    if options_results[selected]:
        return options_results[selected]
    else:
        pygame.quit()
        return False, False    

def run_menu_loop(clock):
    pygame.display.flip()

