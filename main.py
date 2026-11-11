import pygame
import random
import sys

from settings import WIDTH, HEIGHT, FPS, ROAD_LEFT, ROAD_RIGHT, WHITE, BLACK, GRAY, GREEN, YELLOW
from player import PlayerCar
from traffic import TrafficCar


def draw_road(screen, road_offset):
    screen.fill(GREEN)

    # Bordes de la ruta
    pygame.draw.rect(screen, GRAY, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))
    pygame.draw.rect(screen, WHITE, (ROAD_LEFT, 0, 8, HEIGHT))
    pygame.draw.rect(screen, WHITE, (ROAD_RIGHT - 8, 0, 8, HEIGHT))

    # Líneas divisorias animadas
    dash_height = 48
    gap = 32
    for lane_x in (WIDTH // 2 - 5,):
        y = -dash_height + (road_offset % (dash_height + gap))
        while y < HEIGHT:
            pygame.draw.rect(screen, YELLOW, (lane_x, y, 10, dash_height))
            y += dash_height + gap


def draw_text(screen, font, text, color, x, y, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(image, rect)


def reset_game():
    return PlayerCar(), [], 0, 0.0, 5.0, False


def main():
    pygame.init()
    pygame.display.set_caption("Carrera en la Ruta")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 34)
    big_font = pygame.font.Font(None, 64)

    player, traffic, score, spawn_timer, speed, game_over = reset_game()
    road_offset = 0
    running = True

    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game_over and event.key == pygame.K_RETURN:
                    player, traffic, score, spawn_timer, speed, game_over = reset_game()

        keys = pygame.key.get_pressed()

        if not game_over:
            player.update(keys, dt)

            # La velocidad aumenta gradualmente con el puntaje
            speed = min(5.0 + score * 0.025, 12.0)
            road_offset += int(speed * 120 * dt)

            spawn_timer += dt
            spawn_interval = max(0.55, 1.25 - score * 0.004)
            if spawn_timer >= spawn_interval:
                spawn_timer = 0
                traffic.append(TrafficCar())

            for car in traffic:
                car.update(speed, dt)

            traffic = [car for car in traffic if car.rect.top < HEIGHT + 30]
            for car in traffic:
                if player.rect.colliderect(car.rect):
                    game_over = True
                    break

            score += int(10 * dt)

        draw_road(screen, road_offset)

        for car in traffic:
            car.draw(screen)
        player.draw(screen)

        draw_text(screen, font, f"Puntaje: {score}", WHITE, 18, 16)
        draw_text(screen, font, f"Velocidad: {speed:.1f}", WHITE, 18, 48)
        draw_text(screen, font, "Mover: flechas o A/D", WHITE, 18, HEIGHT - 36)

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 165))
            screen.blit(overlay, (0, 0))
            draw_text(screen, big_font, "¡CHOCASTE!", WHITE, WIDTH // 2, HEIGHT // 2 - 55, True)
            draw_text(screen, font, f"Puntaje final: {score}", WHITE, WIDTH // 2, HEIGHT // 2, True)
            draw_text(screen, font, "Presioná ENTER para volver a jugar", WHITE,
                      WIDTH // 2, HEIGHT // 2 + 48, True)
            draw_text(screen, font, "ESC para salir", WHITE, WIDTH // 2, HEIGHT // 2 + 88, True)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
