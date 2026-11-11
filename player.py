import pygame
from settings import WIDTH, HEIGHT, ROAD_LEFT, ROAD_RIGHT, PLAYER_COLOR


class PlayerCar:
    def __init__(self):
        self.width = 48
        self.height = 82
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_speed = 360

    def update(self, keys, dt):
        direction = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction += 1

        self.rect.x += int(direction * self.move_speed * dt)

        # El auto permanece dentro de la ruta
        self.rect.left = max(self.rect.left, ROAD_LEFT + 14)
        self.rect.right = min(self.rect.right, ROAD_RIGHT - 14)

    def draw(self, screen):
        # Carrocería
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect, border_radius=9)
        # Parabrisas y luneta
        pygame.draw.rect(screen, (150, 215, 245),
                         (self.rect.x + 8, self.rect.y + 12, self.width - 16, 19),
                         border_radius=5)
        pygame.draw.rect(screen, (100, 175, 215),
                         (self.rect.x + 8, self.rect.y + 52, self.width - 16, 15),
                         border_radius=4)
        # Ruedas
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.x - 4, self.rect.y + 13, 6, 18), border_radius=2)
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.right - 2, self.rect.y + 13, 6, 18), border_radius=2)
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.x - 4, self.rect.y + 52, 6, 18), border_radius=2)
        pygame.draw.rect(screen, (15, 15, 15),
                         (self.rect.right - 2, self.rect.y + 52, 6, 18), border_radius=2)
