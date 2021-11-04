import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """ 飞船发射的子弹管理的类 """

    def __init__(self, ai_settings, screen, ship):
        # 在飞船所处的位置创建一个子弹对象
        super().__init__()
        self.screen = screen

        # 在(0,0)坐标处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 使用小数表示子弹的位置
        self.y_position = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 子弹向上移动，表示更新子弹的位置
        self.y_position -= self.speed_factor
        self.rect.y = self.y_position

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
