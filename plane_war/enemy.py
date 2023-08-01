import pygame
from random import *

# 小型敌机
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        # 加载破坏图片
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),
            pygame.image.load('images/enemy1_down4.png').convert_alpha()
        ])
        # 获取矩形
        self.rect = self.image.get_rect()
        # 获取背景尺寸本地化
        self.width, self.height = bg_size[0], bg_size[1]
        # 飞机速度
        self.speed = 2
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5个屏幕的高度出现
        self.rect.left, self.rect.top = randint(0,self.width - self.rect.width), randint(-5*self.height, 0)
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机移动
    def move(self):
        # 坐标在底部以上 向下移动
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5保证随机出现的飞机不会出现在同一排
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)


# 中型敌机
class MidEnemy(pygame.sprite.Sprite):
    # 飞机血条
    energy = 8

    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        # 加载被子弹击打时的图片
        self.image_hit = pygame.image.load('images/enemy2_hit.png').convert_alpha()
        # 加载破坏图片
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),
            pygame.image.load('images/enemy2_down4.png').convert_alpha()
        ])
        # 获取矩形
        self.rect = self.image.get_rect()
        # 获取背景尺寸本地化
        self.width, self.height = bg_size[0], bg_size[1]
        # 飞机速度
        self.speed = 1
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5个屏幕的高度出现
        self.rect.left, self.rect.top = randint(0,self.width - self.rect.width), randint(-10*self.height, -self.height)
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image)
        # 飞机血条
        self.energy = MidEnemy.energy
        # 击中属性
        self.hit = False

    # 敌机移动
    def move(self):
        # 坐标在底部以上 向下移动
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        #飞机血条
        self.energy = MidEnemy.energy
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5保证随机出现的飞机不会出现在同一排
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10*self.height, -self.height)


# 大型敌机
class BigEnemy(pygame.sprite.Sprite):
    # 飞机血条
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        # 加载被子弹击打时的图片
        self.image_hit = pygame.image.load('images/enemy3_hit.png').convert_alpha()
        # 加载破坏图片
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),
            pygame.image.load('images/enemy3_down6.png').convert_alpha()
        ])
        # 获取矩形
        self.rect = self.image1.get_rect()
        # 获取背景尺寸本地化
        self.width, self.height = bg_size[0], bg_size[1]
        # 飞机速度
        self.speed = 1
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5个屏幕的高度出现
        self.rect.left, self.rect.top = randint(0,self.width - self.rect.width), randint(-15*self.height, -5*self.height)
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image1)
        #飞机血条
        self.energy = BigEnemy.energy
        # 击中属性
        self.hit = False

    # 敌机移动
    def move(self):
        # 坐标在底部以上 向下移动
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        #飞机血条
        self.energy = BigEnemy.energy
        # 飞机存活
        self.active = True
        # 设置敌方飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正) ,-5保证随机出现的飞机不会出现在同一排
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15*self.height, -5*self.height)






