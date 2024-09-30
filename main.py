import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updateable = pygame.sprite.Group()
    updateable.add(player)
    drawable = pygame.sprite.Group()
    drawable.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, BLACK)

        dt = clock.tick(60) / 1000

        for upd in updateable:
            upd.update(dt)
        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
