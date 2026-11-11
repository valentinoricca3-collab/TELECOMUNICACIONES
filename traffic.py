import pygame
import random
from settings import WIDTH, ROAD_LEFT, ROAD_RIGHT, TRAFFIC_COLORS


class TrafficCar:
    def __init__(self):
        self.width = 48
        self.height = 82
        lanes = [ROAD_LEFT + 55, WIDTH // 2 - self.width // 2, ROAD_RIGHT - 55 - self.width]
        self.rect = pygame.Rect(random.choice(lanes), -self.height, self.width, self.height)
        self.color = random.choice(TRAFFIC_COLORS)

    def update(self, road_speed, dt):
        self.rect.y += int((road_speed * 105 + 90) * dt)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=9)
        pygame.draw.rect(screen, (175, 215, 235),
                         (self.rect.x + 8, self.rect.y + 12, self.width - 16, 19),
                         border_radius=5)
        pygame.draw.rect(screen, (125, 175, 200),
                         (self.rect.x + 8, self.rect.y + 52, self.width - 16, 15),
                         border_radius=4)
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.x - 4, self.rect.y + 13, 6, 18), border_radius=2)
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.right - 2, self.rect.y + 13, 6, 18), border_radius=2)
