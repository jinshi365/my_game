import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed
            # self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center1 -= self.ai_settings.ship_speed
        if self.moving_top and self.rect.top:
            self.center2 -= self.ai_settings.ship_speed
            # self.rect.centerx += 1
        if self.moving_bottom and self.rect.bottom:
            # self.rect.centerx -= 1
            self.center2 += self.ai_settings.ship_speed
        # if self.moving_up:
        #     self.rect.centery -= 1
        # if self.moving_down:
        #     self.rect.centery += 1

        self.rect.centerx = self.center1
        self.rect.centery = self.center2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
