from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
    
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position.xy, SHOT_RADIUS, width = 2 )
    
    def update(self, dt):
        self.position += self.velocity  * dt
