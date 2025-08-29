import pygame
import random
from src.objects.asteroid import Asteroid
from src.abstractions.constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.spawn_rate = ASTEROID_SPAWN_RATE
        self.difficulty_timer = 0.0
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused
        

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        if hasattr(asteroid, "add"):
            asteroid.add(*asteroid.containers)

    def update(self, dt):
        if self.paused:
            return
        self.spawn_timer += dt
        self.difficulty_timer  += dt
        if self.difficulty_timer > ASTEROID_SPAWN_RATE_INCREASE_TIMER:
            self.spawn_rate = max(ASTEROID_MIN_SPAWN_RATE, self.spawn_rate - ASTEROID_SPAWN_RATE_CHANGE)
            self.difficulty_timer = 0
        if self.spawn_timer > self.spawn_rate:
            self.spawn_timer = 0.0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

