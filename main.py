import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    while True:
        for event in pygame.event.get():
            pygame.Surface.fill(screen, BLACK)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                return

if __name__ == '__main__':
    main()
