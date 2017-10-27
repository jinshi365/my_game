import sys

import pygame


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_bottom = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_bottom = False


def check_events(ship):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    #
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
