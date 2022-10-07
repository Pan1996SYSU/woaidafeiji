import sys

import pygame

pygame.init()

color1 = (0, 128, 128)
color2 = (60, 60, 60)

screen_image = pygame.display.set_mode((400, 700))
screen_rect = screen_image.get_rect()

pygame.display.set_caption('我爱打飞机')

ship_image = pygame.image.load('images/1.png')
ship_rect = ship_image.get_rect()
ship_rect.center = screen_rect.center

bullet_rect = pygame.Rect(0, 0, 5, 12)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ship_rect.x > 0:
                ship_rect.x -= 10
            elif event.key == pygame.K_RIGHT and ship_rect.x + ship_rect.width < 400:
                ship_rect.x += 10
            elif event.key == pygame.K_UP and ship_rect.y > 0:
                ship_rect.y -= 10
            elif event.key == pygame.K_DOWN and ship_rect.y + ship_rect.height < 700:
                ship_rect.y += 10
            elif event.key == pygame.K_SPACE:
                bullet_rect.midbottom = ship_rect.midtop

    bullet_rect.y -= 1
    screen_image.fill(color1)
    screen_image.blit(ship_image, ship_rect)
    pygame.draw.rect(screen_image, color2, bullet_rect)
    pygame.display.flip()
