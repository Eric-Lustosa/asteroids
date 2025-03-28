import pygame
from constants import *
from pygame import surface 


def main():
    print('"Starting Asteroids!"')
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()