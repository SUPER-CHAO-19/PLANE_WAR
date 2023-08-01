import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用Sprite初始化
        pygame.sprite.Sprite.__init__(self)
        # 加载子弹图片
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        # 获取图片尺寸
        self.rect = self.image.get_rect()
        # 图片位置
        self.rect.left, self.rect.top = position
        # 子弹速度
        self.speed = 12
        # 子弹显示
        self.active = False
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用Sprite初始化
        pygame.sprite.Sprite.__init__(self)
        # 加载子弹图片
        self.image = pygame.image.load('images/bullet2.png').convert_alpha()
        # 获取图片尺寸
        self.rect = self.image.get_rect()
        # 图片位置
        self.rect.left, self.rect.top = position
        # 子弹速度
        self.speed = 14
        # 子弹显示
        self.active = False
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True