import pygame
from constants import *
from pygame import surface 
from player import Player  
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
from score import *



def main():
    print('"Starting Asteroids!"')
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height", SCREEN_HEIGHT)
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)

    #Sets screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    relog = pygame.time.Clock()
    dt = 0
    score = 0

    #Sets groups for the Classes in order to be drawable/updatable in the screen
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Adds in the containers in order to run the interactions
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    #Makes the loop that the runs the game
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
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit(f"Sua pontuação foi de {score}, Game over!")
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    score += 1
                    asteroid.split()
                    shot.kill()

        #draws the score
        draw_score(screen, score)
        #flips display
        pygame.display.flip()


if __name__ == "__main__":
    main()