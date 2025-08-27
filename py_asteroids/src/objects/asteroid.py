import pygame
from src.abstractions.constants import *
from src.objects.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen,color="white",width=2):
        pygame.draw.circle(screen,color,(self.position.x, self.position.y),self.radius, width)

    def update(self,dt):
        self.position += self.velocity * dt