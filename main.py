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
    relog = pygame.time.Clock()
    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        relog.tick(60)
        dt = relog.tick(60) / 1000

if __name__ == "__main__":
    main()