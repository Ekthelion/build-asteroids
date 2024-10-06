import pygame
from constants import SHOT_RADIUS, SHOT_WIDTH, WHITE
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, SHOT_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
