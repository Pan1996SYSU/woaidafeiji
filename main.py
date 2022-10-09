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

pygame.display.set_caption('Ilovehitplane')
title_img = pygame.image.load('images/1.png')
pygame.display.set_icon(title_img)

# buttons = pygame.sprite.Group()
# star_button = pygame.sprite.Sprite()
# end_button = pygame.sprite.Sprite()
# star_button.rect = pygame.Rect(0, 0, 70, 40)
# end_button.rect = pygame.Rect(0, 0, 70, 40)
# star_button.rect.center = screen_rect.center
# end_button.rect.center = screen_rect.center
# buttons.add(star_button)
# buttons.add(end_button)
button_rect = pygame.Rect(0, 0, 200, 50)
button_rect.center = screen_rect.center
play_font = pygame.font.SysFont(None, 48)
play_img = play_font.render('Play', True, color2, color1)
play_rect = play_img.get_rect()
play_rect.center = button_rect.center

ship = pygame.sprite.Group()
space_ship = pygame.sprite.Sprite()
space_ship.image = pygame.image.load('images/飞机.png')
space_ship.rect = space_ship.image.get_rect()
space_ship.rect.midbottom = screen_rect.midbottom
ship.add(space_ship)

pigs = pygame.sprite.Group()
pig = pygame.sprite.Sprite()
pig.image = pygame.image.load('images/猪头.png')
pig.rect = pig.image.get_rect()
pig.rect.midtop = screen_rect.midtop
pigs.add(pig)

bullets = pygame.sprite.Group()

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
                new_bullet = pygame.sprite.Sprite()
                new_bullet.rect = pygame.Rect(0, 0, 7, 12)
                new_bullet.rect.midbottom = space_ship.rect.midtop
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = False
    if moving_left and space_ship.rect.x > 0:
        space_ship.rect.x -= moving_speed
    if moving_right and space_ship.rect.x + space_ship.rect.width < screen_width:
        space_ship.rect.x += moving_speed
    if moving_up and space_ship.rect.y > 0:
        space_ship.rect.y -= moving_speed
    if moving_down and space_ship.rect.y + space_ship.rect.height < screen_height:
        space_ship.rect.y += moving_speed

    screen_image.fill(color1)
    ship.draw(screen_image)
    pigs.draw(screen_image)
    for bullet in bullets:
        pygame.draw.rect(screen_image, color2, bullet.rect)
        bullet.rect.y -= bullet_speed

    pygame.sprite.groupcollide(bullets, pigs, True, True)
    pygame.sprite.groupcollide(ship, pigs, True, False)

    pygame.draw.rect(screen_image, color2, button_rect)
    screen_image.blit(play_img, play_rect)

    pygame.display.flip()
