import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, radius:int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def draw(self, screen:pygame.Surface):
        pass

    def update(self, dt:float):
        pass
        
    def collision_check(self, other):
        centers_distance = self.position.distance_to(other.position)
        return centers_distance <= self.radius + other.radius
