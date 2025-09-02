import pygame
from src.abstractions.constants import *
from src.abstractions.background import *
from src.abstractions.score_hud import *

from src.objects.player import Player
from src.objects.asteroid import Asteroid
from src.objects.asteroidfield import *
from src.objects.menu import Menu
from src.objects.shot import Shot

from src.highscore import load_highscore, update_highscore




def run_game(screen, clock, pacifist_mode):
    paused = False
    dimensions = SCREEN_WIDTH, SCREEN_HEIGHT
    bg_offset = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, pacifist_mode)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    last_time = pygame.time.get_ticks()
    running = True

    while running:
        now = pygame.time.get_ticks()
        if not paused:
            dt = (now - last_time) / 1000 
        else:
            dt = 0
        dt = min(dt, 0.05)
        last_time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    pause = handle_pause(screen,clock,player)
                    if pause:
                        return pause
     
        if not paused:
            updatable.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                return handle_game_over(screen,clock,player)
                
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    asteroid.get_hit(dt, player)
                    shot.kill()

        set_solid_background((0, 0, 0), screen)
        if BG_SECONDARY:
            bg_offset = set_shifting_gradient(BG_SECONDARY, screen, dimensions, bg_offset, BG_SPEED)

        for obj in drawable:
            obj.draw(screen)
        draw_hud(screen, player)

        pygame.display.flip()

def handle_pause(screen,clock,player):
    pause_options,pause_results = ["Resume", "Restart", "Quit"],  ["resume", "restart", "quit"]
    pause_menu = Menu("Paused", pause_options, pause_results, f"Current Score: {player.score}")

    choice = pause_menu.run_menu(screen, clock)

    if choice == "resume":
       return False
    elif choice == "restart":
        return "restart"
    elif choice == "quit":
        return "quit"

def handle_game_over(screen,clock,player):
    final_score = player.score
    game_over_options, game_over_results = ["Restart", "Exit"],  [True, False]
    scoreline = f"Score: {player.score} | Time: {player.survival_time:.2f}s"

    if update_highscore(final_score):
        scoreline = f"NEW HIGH SCORE!\n{scoreline}"

    game_over_menu = Menu("Game Over", game_over_options, game_over_results, scoreline, (255, 0, 0))

    restart = game_over_menu.run_menu(screen, clock)
    
    if restart:
        return "restart"
    else:
        return "quit"

