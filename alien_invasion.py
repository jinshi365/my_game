

import pygame

from settings import Settings
from ship import Ship
# from alien import Alien
from pygame.sprite import Group
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # alien = Alien(ai_settings, screen)
    pygame.display.set_caption("alien")

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        # gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
