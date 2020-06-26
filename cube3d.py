import pygame, math

WIDTH = 500
HEIGHT = 700
FPS = 30

BLACK = (0, 0, 0)
step = 1

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

brick = pygame.Surface((5, 5))
brick.fill((0xbc, 0x39, 0x08))
rect1 = brick.get_rect()
rect2 = brick.get_rect()
rect3 = brick.get_rect()
rect4 = brick.get_rect()
rect5 = brick.get_rect()
rect6 = brick.get_rect()
rect7 = brick.get_rect()
rect8 = brick.get_rect()

def point(step, n):
    global WIDTH, HEIGHT
    r = 200

    angle_1 = (2 * math.pi / 360) * (step % 360)
    angle_2 = (2 * math.pi / 360) * (step // 90 % 2 * 90 - step % 90)
    x, y = r * math.cos(angle_1), r * math.sin(angle_1) * math.cos(angle_2)
    return x // 1 + WIDTH // 2, y // 1 + HEIGHT - n

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect1.x, rect1.y = point(step, 300)
    rect2.x, rect2.y = point(step + 90, 300)
    rect3.x, rect3.y = point(step + 180, 300)
    rect4.x, rect4.y = point(step + 270, 300)

    rect5.x, rect5.y = point(step, 500)
    rect6.x, rect6.y = point(step + 90, 500)
    rect7.x, rect7.y = point(step + 180, 500)
    rect8.x, rect8.y = point(step + 270, 500)

    step += 1


    screen.fill(BLACK)
    screen.blit(brick, rect1)
    screen.blit(brick, rect2)
    screen.blit(brick, rect3)
    screen.blit(brick, rect4)

    screen.blit(brick, rect5)
    screen.blit(brick, rect6)
    screen.blit(brick, rect7)
    screen.blit(brick, rect8)

    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect1.x, rect1.y], [rect2.x, rect2.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect2.x, rect2.y], [rect3.x, rect3.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect3.x, rect3.y], [rect4.x, rect4.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect4.x, rect4.y], [rect1.x, rect1.y], 5)

    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect5.x, rect5.y], [rect6.x, rect6.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect6.x, rect6.y], [rect7.x, rect7.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect7.x, rect7.y], [rect8.x, rect8.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect8.x, rect8.y], [rect5.x, rect5.y], 5)

    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect1.x, rect1.y], [rect5.x, rect5.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect2.x, rect2.y], [rect6.x, rect6.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect3.x, rect3.y], [rect7.x, rect7.y], 5)
    pygame.draw.line(screen, (0xbc, 0x39, 0x08), [rect4.x, rect4.y], [rect8.x, rect8.y], 5)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()