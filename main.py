import sys
import time
import pygame

pygame.init()

moving_speed = 1
bullet_speed = 3
pause_time = 0.002

color1 = (70, 90, 128)
color2 = (60, 60, 60)

screen_height = 700
screen_width = 400

screen_image = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen_image.get_rect()

pygame.display.set_caption('我爱打飞机')

ship_image = pygame.image.load('images/飞机.png')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom

pig_image = pygame.image.load('images/猪头1.png')
pig_rect = pig_image.get_rect()
pig_rect.top = screen_rect.top

bullet_rect_list = []

moving_left = False
moving_right = False
moving_up = False
moving_down = False

while True:
    time.sleep(pause_time)
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
                bullet_rect = pygame.Rect(0, 0, 7, 12)
                bullet_rect.midbottom = ship_rect.midtop
                bullet_rect_list.append(bullet_rect)
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
        ship_rect.x -= moving_speed
    if moving_right and ship_rect.x + ship_rect.width < screen_width:
        ship_rect.x += moving_speed
    if moving_up and ship_rect.y > 0:
        ship_rect.y -= moving_speed
    if moving_down and ship_rect.y + ship_rect.height < screen_height:
        ship_rect.y += moving_speed

    screen_image.fill(color1)
    screen_image.blit(ship_image, ship_rect)
    screen_image.blit(pig_image, pig_rect)
    for bullet_rect in bullet_rect_list:
        pygame.draw.rect(screen_image, color2, bullet_rect)
        if bullet_rect.bottom < 0:
            bullet_rect_list.remove(bullet_rect)
        bullet_rect.y -= bullet_speed
    # print(len(bullet_rect_list))
    pygame.display.flip()
