import pygame

from pygame.sprite import Sprite


class Aliens(Sprite):
    def __init__(self, ai_settings, screen):
        """ 初始化外星人，并设置其起始位置 """
        super(Aliens, self).__init__()
        self.settings = ai_settings
        self.screen = screen

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储卫星人的准确位置
        self.x = float(self.rect.x)

    def update(self):
        # 外星人向左或向右移动
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_sdges(self):
        # 如果外星人是否位于屏幕边缘， 就返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
