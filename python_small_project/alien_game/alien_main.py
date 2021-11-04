#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import pygame

from pygame.sprite import Group
from alien_settings import Settings
from alien_ship import Ship
from aliens import Aliens
from game_status import GameStatus
from game_button import Button
from score_board import Scoreboard

import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕游戏
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_name)

    # 创建play按钮
    play_button = Button(ai_settings, screen, "play")

    # 创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建一群外星人
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 创建存储游戏统计信息的实例，并创建计分牌
    g_status = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, g_status)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, g_status, sb, play_button,
                        ship, aliens, bullets)

        if g_status.game_active:
            ship.move_update()

            # 表示bullets子弹容器里的每一颗子弹，都会更新位置
            bullets.update()

            gf.update_bullets(ai_settings, screen, g_status, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, screen, g_status, sb, ship, bullets, aliens)

        gf.update_screen(ai_settings, screen, g_status, sb,
                         ship, aliens, bullets, play_button)


def main():
    run_game()


#### main program ### 
if __name__ == '__main__':
    main()
