import sys

import pygame
from alien_bullet import Bullet
from aliens import Aliens
from time import sleep


def check_events(ai_settings, screen, g_status, sb, 
    play_button, ship, aliens, bullets):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_game_button(ai_settings, screen, g_status, sb, ship, aliens, 
                bullets, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            


def check_game_button(ai_settings, screen, g_status, sb, ship, aliens, 
    bullets, play_button, mouse_x, mouse_y):
    """ 在玩家点击play按钮时，开始新游戏 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and not g_status.game_active:
        #删除现有的子弹，加快游戏的节奏，并创建一群新的外星人
        ai_settings.init_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)

        #重置游戏统计信息
        g_status.reset_status()
        g_status.game_active = True

        #重置记分牌图案
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空外星人和子弹
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        #飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #飞船向左移动
        ship.moving_left  = True
    elif event.key == pygame.K_SPACE:
        #如果子弹发射数未达到上限，就发射一颗子弹
        fire_bullets(ai_settings, screen, ship, bullets)
        


def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            #飞船停止向右移动
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #飞船停止向左移动
            ship.moving_left  = False



def fire_bullets(ai_settings, screen, ship, bullets):
    #创建一颗子弹，并将其加入到bullets子弹容器中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def check_high_score(g_status, sb):
    #检测是否诞生了新的最高得分
    if g_status.score > g_status.high_score:
        g_status.high_score = g_status.score
        sb.prep_high_score()



def check_bullet_alien_collisions(ai_settings, screen, g_status, sb, 
    ship, bullets, aliens):
    """
    1.检查是否有子弹击中了外星人
    2.如果是击中了，就删除相应的子弹和外星人
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            g_status.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(g_status, sb)


    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        #提高等级
        g_status.level += 1
        sb.prep_level()

        creat_fleet(ai_settings, screen, ship, aliens)



def update_bullets(ai_settings, screen, g_status, sb, ship, bullets, aliens):
    #更新子弹的位置，并删除已经消失的子弹
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, g_status, sb, 
        ship, bullets, aliens)



def get_number_rows(ai_settings, ship_height, alien_height):
    #计算整个屏幕可容纳多少行外星人
    avail_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(avail_space_y / (2*alien_height))
    return number_rows



def get_number_alien_x(ai_settings, alien_width):
    #计算每行可容纳多少个外星人
    avail_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(avail_space_x / (2 * alien_width))
    return number_aliens_x


def creat_alien(ai_settings, screen, aliens, alien_number, rows_number):
    #创建一个外星人并将其放在当前行
    alien = Aliens(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*rows_number

    aliens.add(alien)



def creat_fleet(ai_settings, screen, ship, aliens):
    """ 创建一群外星人 """
    alien = Aliens(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ai_settings, aliens):
    #将整群外星人下移，并改变它们的方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    if ai_settings.fleet_direction == 1:
        ai_settings.fleet_direction = -1
    elif ai_settings.fleet_direction == -1:
        ai_settings.fleet_direction = 1



def check_fleet_sdges(ai_settings, aliens):
    #有外星人到达屏幕边缘是采取相应的措施
    for alien in aliens.sprites():
        if alien.check_sdges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, screen, g_status, sb, ship, bullets, aliens):
    """ 检查是否有外星人到达屏幕低端 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, g_status, sb, ship, bullets, aliens)
            break


def ship_hit(ai_settings, screen, g_status, sb, ship, bullets, aliens):
    """ 响应被外星人撞到的飞船 """
    if g_status.ships_left > 0:
        #将飞船ship_limit 减 1
        g_status.ships_left -= 1

        #更新当前飞船剩余数
        sb.prep_ships()

        #清空外星人流标和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕最低端居中
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)

    else:
        g_status.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, g_status, sb, ship, bullets, aliens):
    check_fleet_sdges(ai_settings, aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("ship hit !!!")
        ship_hit(ai_settings, screen, g_status, sb, ship, bullets, aliens)

    check_aliens_bottom(ai_settings, screen, g_status, sb, ship, bullets, aliens)



def update_screen(ai_settings, screen, g_status, sb, 
    ship, aliens, bullets, play_button):
    """ 更新屏幕上的图像，并切换到新屏幕 """

    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)


    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)


    #显示得分
    sb.show_score()


    #如果游戏处于非活动状态，就绘制play按钮
    if not g_status.game_active:
        play_button.draw_button()

    #刷新最近绘制的屏幕
    pygame.display.flip()
