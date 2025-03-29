import pygame
from constants import *
from pygame import surface 
from player import Player  


def main():
    print('"Starting Asteroids!"')
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    relog = pygame.time.Clock()
    dt = 0
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Get dt and limit FPS in one call
        dt = relog.tick(60) / 1000
         # Update game state
        player.update(dt)
        # Draw everything
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()