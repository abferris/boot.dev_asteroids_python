import pygame

from src.core.constants import *

from src.game.circleshape import CircleShape
from src.game.player.shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, pacifist_mode = False):
        super().__init__(x, y , PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = PLAYER_ACCELERATION
        self.max_speed = PLAYER_MAX_SPEED
        self.friction = PLAYER_DRAG
        self.score = 0
        self.survival_time = 0
        self.pacifist_mode = pacifist_mode


    def add_score(self, num):
        self.score += num

    def draw(self,screen,color="white",width=2):
        pygame.draw.polygon(screen,color, self.triangle(), width)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def  move(self,dt, thrust = 1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * thrust * dt
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)


    def update(self, dt):
        if self.paused:
            return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s]or keys[pygame.K_DOWN]:
            self.move(dt,-1)
        if keys[pygame.K_SPACE] and not self.pacifist_mode :
            self.shoot()

        self.velocity *= self.friction ** dt
        self.position += self.velocity * dt

        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        
        self.survival_time+= dt

    def shoot(self):
        tip = self.triangle()[0]
        
        if self.shoot_cooldown <= 0:
            shot = Shot(tip.x,tip.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation) 
            shot.velocity = forward * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN 
