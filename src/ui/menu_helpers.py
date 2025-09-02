import pygame

from src.core.constants import *
from src.core.highscore import load_highscore

def draw_menu(screen,title,sub_title,title_color,options,selected):
    large_font = get_font(LARGE_FONT_SIZE)
    small_font = get_font(SMALL_FONT_SIZE)
    title_text = large_font.render(title, True, title_color)    
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(title_text, title_rect)

    if sub_title:
        sub_x,sub_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/3
        lines = sub_title.split("\n")
        for i, line in enumerate(lines):
            line_text = small_font.render(line, True, (255, 255, 255))
            line_rect = line_text.get_rect(center=(sub_x,sub_y+i*41))
            screen.blit(line_text, line_rect)



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
    

def draw_highscore(screen, pacifist_mode:bool=False):
    font = get_font(SMALL_FONT_SIZE)
    # May be causing a lot of calls to load highscore
    print("drawing highscore")
    highscore,pacifist_highscore = load_highscore()
    if pacifist_mode == 0:
        highscore_text = font.render(f"High Score: {highscore}", True, (255, 255, 255))
    elif pacifist_mode == 1:
        highscore_text = font.render(f"High Score: {pacifist_highscore}s", True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(highscore_text, highscore_rect)
    else:
        highscore_text = font.render(f"High Score: {highscore}", True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        pacifist_highscore_text = font.render(f"High Time: {pacifist_highscore:.2f}s", True, (255, 255, 255))
        pacifist_highscore_rect = highscore_text.get_rect(topright=(SCREEN_WIDTH - 10, 60))

        screen.blit(highscore_text, highscore_rect)
        screen.blit(pacifist_highscore_text, pacifist_highscore_rect)
        

def get_font(font_size):
    return pygame.font.Font(None, font_size)