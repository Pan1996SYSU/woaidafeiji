import sys
import time
import pygame

pygame.init()

color1 = (0, 128, 128)
color2 = (60, 60, 60)

screen_image = pygame.display.set_mode((400, 700))
screen_rect = screen_image.get_rect()

pygame.display.set_caption('我爱打飞机')

ship_image = pygame.image.load('images/1.png')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom

bullet_rect = pygame.Rect(0, 0, 5, 12)

moving_left = False
moving_right = False
moving_up = False
moving_down = False

while True:
    time.sleep(0.002)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                bullet_rect.midbottom = ship_rect.midtop
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = False
    if moving_left and ship_rect.x > 0:
        ship_rect.x -= 1
    if moving_right and ship_rect.x + ship_rect.width < 400:
        ship_rect.x += 1
    if moving_up and ship_rect.y > 0:
        ship_rect.y -= 1
    if moving_down and ship_rect.y + ship_rect.height < 700:
        ship_rect.y += 1

    bullet_rect.y -= 1
    screen_image.fill(color1)
    screen_image.blit(ship_image, ship_rect)
    pygame.draw.rect(screen_image, color2, bullet_rect)
    pygame.display.flip()
