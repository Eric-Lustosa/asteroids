import pygame
pygame.font.init()

font = pygame.font.SysFont(None, 36)

def draw_score(screen, score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))