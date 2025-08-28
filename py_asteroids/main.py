import sys
import pygame

from src.abstractions.constants import *
from src.abstractions.background import *
from src.objects.player import Player
from src.objects.asteroid import Asteroid
from src.objects.asteroidfield import *
from src.objects.shot import Shot


def main():
    pygame.init()
    dims = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(dims)
    clock = pygame.time.Clock()
    bg_offset = 0
    dt = 0
    survival_time = 0

    font = pygame.font.Font(None,36)





    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)


    
    box_width, box_height = 200, 60
    box_x = SCREEN_WIDTH - box_width - 10  # 10 px from right
    box_y = 10  # 10 px from top
    box_color = (30, 30, 30)  # dark gray

    # Render score and survival time
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    time_text = font.render(f"Time: {survival_time:.1f}s", True, (255, 255, 255))

    # Blit text into the box
    screen.blit(score_text, (box_x + 10, box_y + 5))
    screen.blit(time_text, (box_x + 10, box_y + 30))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print(f"Game Over! Survived for {survival_time:.2f} seconds!\n Score: {player.score}")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    asteroid.get_hit(dt,player)
                    shot.kill()

        black = (0, 0, 0)
        set_solid_background(black, screen)
        
        # secondary color is a dark blue 
        bg_secondary = (0,0,82)
        bg_speed = .8
        # this sets up the gradient and makes it shift
        bg_offset = set_shifting_gradient(bg_secondary, screen,dims,bg_offset,bg_speed)
        # draws objects
        for obj in drawable:
            obj.draw(screen)

        #score hud
        # draw HUD
        pygame.draw.rect(screen, box_color, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 2)

        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        time_text = font.render(f"Time: {survival_time:.1f}s", True, (255, 255, 255))
        screen.blit(score_text, (box_x + 10, box_y + 5))
        screen.blit(time_text, (box_x + 10, box_y + 30))
        #  refreshes screen 
        dt = run_loop(60,clock)/1000
        survival_time += dt
      # limit to 60 FPS
        # pygame.display.flip()
if __name__ == "__main__":
    main()
