import pygame
class MyPlane(pygame.sprite.Sprite): # 继承Sprite()类
    def __init__(self,bg_size):
        # 调用sprite初始化
        pygame.sprite.Sprite.__init__(self)
        # super().__init__(self)
        # 加载图片
        self.image1 = pygame.image.load('images/me1.png').convert_alpha()
        self.image2 = pygame.image.load('images/me2.png').convert_alpha()
        # 加载破坏画面
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/me_destroy_1.png').convert_alpha(),
            pygame.image.load('images/me_destroy_2.png').convert_alpha(),
            pygame.image.load('images/me_destroy_3.png').convert_alpha(),
            pygame.image.load('images/me_destroy_4.png').convert_alpha()
        ])
        # 获取矩形
        self.rect = self.image1.get_rect()
        # 获取的尺寸本地化
        self.width, self.height = bg_size[0],bg_size[1]
        # 设置飞机初始位置(飞机矩形左上角顶点,背景图左上角为原点(0,0),向左为正,向下为正)
        self.rect.left, self.rect.top = (self.width - self.rect.width)//2, self.height - self.rect.height - 60
        # 设置飞机速度
        self.speed = 10
        # 飞机存活
        self.active = True
        # 无敌状态
        self.invincible = False
        # 提取图片非白色的部分mask作为本体
        self.mask = pygame.mask.from_surface(self.image1)

    # 向上移动
    def moveUp(self):
        # 判断是否跑出边框
        # 没有超过上边框
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            # 最上端极限位置
            self.rect.top = 0
    # 向下移动
    def moveDown(self):
        # 没有超过下边框
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            # 最低端极限位置
            self.rect.bottom = self.height - 60
    # 向左移动
    def moveLeft(self):
        # 没有超过左边框
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    # 想右移动
    def moveRight(self):
        # 没有超过右边框
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            # 最右端极限位置
            self.rect.right = self.width

    # 复活
    def reset(self):
        # 初始化飞机位置
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        self.active = True
        self.invincible = True



