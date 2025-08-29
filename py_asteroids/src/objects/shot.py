import pygame
from src.abstractions.constants import *
from src.objects.circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,radius=SHOT_RADIUS):
        super().__init__(x,y,radius)
        self.edge_hits = 0

    def draw(self,screen,color="white",width=2):
        pygame.draw.circle(screen,color,self.position,self.radius, width)

    def update(self,dt):
        if self.paused:
            return
        
        self.position += self.velocity * dt
        if self.edge_hits >= 2:
            self.kill()
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
            self.edge_hits += 1
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
            self.edge_hits += 1            
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
            self.edge_hits += 1
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
            self.edge_hits += 1
