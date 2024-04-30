#you need pygame to run this code
#sudo apt install pygame
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes Demo")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WINDOW.fill(WHITE)

    pygame.draw.rect(WINDOW, RED, (50, 50, 100, 50)) 
    pygame.draw.circle(WINDOW, GREEN, (200, 100), 30) 
    pygame.draw.line(WINDOW, BLUE, (300, 200), (400, 300), 5) 

    pygame.display.flip()

pygame.quit()
sys.exit()
