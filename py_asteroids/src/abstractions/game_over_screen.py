import pygame
from src.abstractions.constants import *

def game_over_screen(screen, score, survival_time):
    font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    
    selected = 0  # 0 = Restart, 1 = Exit
    options = ["Restart", "Exit"]
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # black background
        
        # Draw title
        title_text = font.render("GAME OVER", True, (255, 0, 0))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        screen.blit(title_text, title_rect)
        
        stats_text = small_font.render(f"Score: {score}   Time: {survival_time:.2f}s", True, (255, 255, 255))
        stats_rect = stats_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
        screen.blit(stats_text, stats_rect)
        
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text = small_font.render(option, True, color)
            rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i * 50))
            screen.blit(text, rect)
        
        pygame.display.flip()
        clock.tick(60)
        
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # exit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return True  # restart
                    else:
                        pygame.quit()
                        return False  # exit