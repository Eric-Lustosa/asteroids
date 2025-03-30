from circleshape import CircleShape
import pygame
from constants import *
import random
angle = random.uniform(20, 50)
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        #self.is_destroyed = False
        

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position.xy, self.radius, width = 2 )
    
    def update(self, dt):
        self.position += self.velocity * dt
        buffer = self.radius * 2  # Give some extra space beyond screen
        if (self.position.x < -buffer or 
            self.position.x > SCREEN_WIDTH + buffer or
            self.position.y < -buffer or
            self.position.y > SCREEN_HEIGHT + buffer):
            # If too far outside, remove from all groups
            self.kill()
    


    def split(self):
        angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        if self.radius == ASTEROID_MAX_RADIUS:
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            Ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            Ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            Ast1.velocity = v1*1.2
            Ast2.velocity = v2*1.2
            return
        
        if self.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS:
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            Ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            Ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            Ast1.velocity = v1*1.2
            Ast2.velocity = v2*1.2

            return
    
