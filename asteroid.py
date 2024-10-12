from circleshape import *
from constants import ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS, WHITE
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vector_positive = self.velocity.rotate(angle)
        vector_negative = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_positive * 1.2
        asteroid_two.velocity = vector_negative * 1.2
