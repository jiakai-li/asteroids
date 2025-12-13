import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x ,y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        center = (self.x, self.y)
        pygame.draw.circle(screen, "white", center, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= (self.velocity * dt)
        if keys[pygame.K_d]:
            self.x += (self.velocity * dt)
        if keys[pygame.K_w]:
            self.y += (self.velocity * dt)
        if keys[pygame.K_s]:
            self.y -= (self.velocity * dt)
