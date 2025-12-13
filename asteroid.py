import random
import pygame

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x ,y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(random_angle)
        second_velocity = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_one = Asteroid(self.position[0], self.position[1], new_radius)
        child_one.velocity = first_velocity * 1.2

        child_two = Asteroid(self.position[0], self.position[1], new_radius)
        child_two.velocity = second_velocity * 1.2
