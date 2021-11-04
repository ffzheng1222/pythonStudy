class Settings:
    """ 存储《外星人入侵》的所有设置类 """

    def __init__(self):
        # 屏幕设置
        self.screen_name = "Alien Tony"
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 250)

        # 飞船的设置
        # self.ship_speed_factor = 5
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed_factor = 2
        self.bullet_width = 1500
        self.bullet_height = 10
        self.bullet_color = (0, 0, 250)
        self.bullet_allowed = 3000

        # 外星静态设置
        # ...FIXME

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """" 初始化游戏进行而变化的设置 """
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 2

        # 外星人动态设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
