import pygame
from src.abstractions.constants import *

def draw_hud(screen,player):
    font = pygame.font.Font(None,36)

    pygame.draw.rect(screen, HUD_COLOR, (HUD_X, HUD_Y, HUD_WIDTH, HUD_HEIGHT ))
    pygame.draw.rect(screen, (255, 255, 255), (HUD_X, HUD_Y, HUD_WIDTH, HUD_HEIGHT), 2)

    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    time_text = font.render(f"Time: {player.survival_time:.2f}s", True, (255, 255, 255))
    
    screen.blit(score_text, (HUD_X + 10, HUD_Y + 5))
    screen.blit(time_text, (HUD_X + 10, HUD_Y + 30))