import pygame
from constants import *
from pygame import surface 
from player import Player  
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print('"Starting Asteroids!"')
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    relog = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Get dt and limit FPS in one call
        AsteroidField()
        dt = relog.tick(60) / 1000
         # Update game state
        updatable.update(dt)
        # Draw everything
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()