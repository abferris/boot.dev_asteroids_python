import pygame

from src.core.constants import *

from src.game.circleshape import CircleShape
from src.game.player.player import Player

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:int):
        super().__init__(x,y,radius)

    def draw(self,screen:pygame.Surface, color:tuple=ASTEROID_COLOR, width:int=0):
        pygame.draw.circle(screen, color,(self.position.x, self.position.y),self.radius, width)

    def update(self, dt:float):
        if self.paused:
            return
        self.position += self.velocity * dt

        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def get_hit(self,dt:float, player:Player):
        output = []

        player.add_score(self.radius)

        if self.radius > ASTEROID_MIN_RADIUS:
            child_radius = self.radius - ASTEROID_MIN_RADIUS

            direction = self.velocity.normalize()

            velocity1 = direction.rotate(45) * self.velocity.length() * 2
            velocity2 = direction.rotate(-45) * self.velocity.length() * 2

            pos1 = self.position + velocity1.normalize() * child_radius
            pos2 = self.position + velocity2.normalize() * child_radius

            child1 = Asteroid(pos1.x, pos1.y, child_radius)
            child1.velocity = velocity1
            output.append(child1)

            child2 = Asteroid(pos2.x, pos2.y, child_radius)
            child2.velocity = velocity2
            output.append(child2)

            self.kill()

            return [child1, child2]

        self.kill()
        return []
