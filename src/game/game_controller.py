import pygame

from src.core.constants import *
from src.core.background import set_solid_background, set_shifting_gradient
from src.core.highscore import update_highscore

from src.game.player.player import Player
from src.game.enemies.asteroid import Asteroid
from src.game.enemies.asteroidfield import AsteroidField
from src.game.player.shot import Shot

from src.ui.menu import Menu
from src.ui.score_hud import draw_hud




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

def handle_pause(screen, clock, player):
    pause_options,pause_results = ["Resume", "Restart", "Quit"],  ["resume", "restart", "quit"]
    pause_menu = Menu("Paused", pause_options, pause_results, f"Current Score: {player.score}")
    if player.pacifist_mode:
        choice = pause_menu.run_menu(screen, clock, 0)
    else:
        choice = pause_menu.run_menu(screen, clock, 1)

    if choice == "resume":
       return False
    elif choice == "restart":
        return "restart"
    elif choice == "quit":
        return "quit"

def handle_game_over(screen,clock,player):
    final_score = player.score
    final_time = player.survival_time
    pacifist_mode = player.pacifist_mode
    game_over_options, game_over_results = ["Restart", "Exit"],  [True, False]
    if not pacifist_mode:
            scoreline = f"Score: {player.score} | Time: {player.survival_time:.2f}s"
            pacifist_option = 0
    else:
        scoreline = f"Time: {player.survival_time:.2f}s"
        pacifist_option = 1
    if update_highscore(final_score,final_time,pacifist_mode):
            scoreline = f"NEW HIGH SCORE!\n{scoreline}"

    game_over_menu = Menu("Game Over", game_over_options, game_over_results, scoreline, (255, 0, 0))

    
    restart = game_over_menu.run_menu(screen, clock, pacifist_option)


    if restart:
        return "restart"
    else:
        return "quit"

