import pygame
from random import *

# 子弹补给
class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        # 调用Sprite初始化
        pygame.sprite.Sprite.__init__(self)
        # 加载补给图片
        self.image = pygame.image.load('images/bullet_supply.png').convert_alpha()
        # 获取矩形尺寸
        self.rect = self.image.get_rect()
        # 背景尺寸
        self.width, self.height = bg_size[0], bg_size[1]
        # 补给位置
        self.rect.left, self.rect.bottom = randint(0, self.width-self.rect.width), -100
        # 补给速度
        self.speed = 5
        # 没有补给
        self.active = False
        # 提取图片非白色部分
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width-self.rect.width), -100

# 炸弹补给
class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        # 调用Sprite初始化
        pygame.sprite.Sprite.__init__(self)
        # 加载补给图片
        self.image = pygame.image.load('images/bomb_supply.png').convert_alpha()
        # 获取矩形尺寸
        self.rect = self.image.get_rect()
        # 背景尺寸
        self.width, self.height = bg_size[0], bg_size[1]
        # 补给位置
        self.rect.left, self.rect.bottom = randint(0, self.width-self.rect.width), -100
        # 补给速度
        self.speed = 5
        # 没有补给
        self.active = False
        # 提取图片非白色部分
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width-self.rect.width), -100






