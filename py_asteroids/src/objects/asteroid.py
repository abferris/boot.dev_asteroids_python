import pygame
from src.abstractions.constants import *
from src.objects.circleshape import CircleShape
from src.objects.player import Player

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,):
        super().__init__(x,y,radius)

    def draw(self,screen,color=ASTEROID_COLOR,width=0):
        pygame.draw.circle(screen,color,(self.position.x, self.position.y),self.radius, width)

    def update(self, dt):
        if self.paused:
            return
        self.position += self.velocity * dt

        # Horizontal wrapping
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        # Vertical wrapping
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def get_hit(self,dt, player:Player):
        player.add_score(self.radius)
        if self.radius > ASTEROID_MIN_RADIUS:
            child_radius = self.radius - ASTEROID_MIN_RADIUS

            direction = self.velocity.normalize()

            velocity1 = direction.rotate(45) * self.velocity.length() * 2
            velocity2 = direction.rotate(-45) * self.velocity.length() * 2
            pos1 = self.position + velocity1.normalize() * child_radius
            pos2 = self.position + velocity2.normalize() * child_radius
            #create child 1
            # new radius is child radius
            #  child 1 position is 45 degrees from current velocity counter clockwise
            # set child 1 velocity 45 degrees from current velocity counter clockwise at 2x the speed of the original asteroid

            #  child 2 position is 45 degrees from current velocity clockwise
            # set child 2 velocity 45 degrees from current velocity clockwise at 2x the speed of the original asteroid
            child1 = Asteroid(pos1.x, pos1.y, child_radius)
            child1.velocity = velocity1

            child2 = Asteroid(pos2.x, pos2.y, child_radius)
            child2.velocity = velocity2
            self.kill()
            return [child1, child2]

        self.kill()
        return []
