import pygame
import random

class Background():
    def __init__(self,img_path,location,screen_size):
        self.image = # 載入background圖片
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = # 取得background的rect
        self.rect.x, self.rect.y = # 設定background位置
    def draw(self, screen):
        # 繪製background

class Base():
    def __init__(self, img_path, screen_size):
        self.image =  # 載入base圖片
        self.width, self.height = # 取得screen_size
        self.image = pygame.transform.scale(self.image,(self.width, self.height/10))
        self.base_width = # 取得base圖片寬度
        self.x1 = 0 # 設定base圖片的x1位置
        self.x2 = self.base_width # 設定base圖片的x2位置
        self.y = # 設定base圖片的y位置
        self.movement_speed = 0.8

    def update(self):
        # 更新x1位置
        # 更新x2位置
        # 如果x1位置超出螢幕，則將x1設定為x2+base寬度
        # 如果x2位置超出螢幕，則將x2設定為x1+base寬度

    def draw(self, screen):
        # 繪製base 在(x1,y)與(x2,y)位置

class Pipe(pygame.sprite.Sprite):
    def __init__(self, img_path, screen_size):
        super(Pipe, self).__init__()
        self.image = # 載入pipe圖片
        self.screen_width, self.screen_height = # 取得screen_size
        self.screen_height*=0.9
        self.gap_size = self.screen_height*0.3
        self.score_counted = # 設定是否已計算分數

    def generate_pipe(self):

        self.top_pipe = pygame.transform.flip(self.image, False, True)
        self.bottom_pipe = self.image
        
        self.top_pipe_scale = random.randint(int(self.screen_height*0.05), int(self.screen_height*0.75 - self.gap_size))
        self.bottom_pipe_scale = self.screen_height*0.9 - self.top_pipe_scale - self.gap_size
        
        self.top_pipe = pygame.transform.scale(self.top_pipe, (self.top_pipe.get_width(), self.top_pipe_scale))
        self.bottom_pipe = pygame.transform.scale(self.bottom_pipe, (self.bottom_pipe.get_width(), self.bottom_pipe_scale))        
        
        self.top_pipe_rect = # 取得top_pipe的rect
        self.bottom_pipe_rect = # 取得bottom_pipe的rect
        
        self.top_pipe_rect.topleft = # top_pipe位置
        self.bottom_pipe_rect.bottomleft = # bottom_pipe位置
        
    def update(self):
        # 更新top_pipe_rect的x位置
        # 更新bottom_pipe_rect的x位置
        # 如果top_pipe_rect超出螢幕，則刪除此物件
        # 如果bottom_pipe_rect超出螢幕，則刪除此物件
        
    def draw(self, screen):
        # 繪製top_pipe
        # 繪製bottom_pipe

class Bird(pygame.sprite.Sprite):
    def __init__(self, img_path, screen_size):
        super(Bird, self).__init__()
        self.images = # 載入bird所有圖片
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.screen_width, self.screen_height = screen_size
        self.velocity = 0
        self.gravity = 0
        self.jump_height = -2.5

        self.rect.x = self.screen_width / 6
        self.rect.y = self.screen_height / 2

    def update(self):
        
        
        self.current_image = # 更新bird的圖片編號
        self.image = # 更新bird的圖片

        # 更新bird的速度
        # 更新bird的位置

        # 如果bird的位置超出螢幕上緣，則將bird的位置設定為螢幕邊界
        # 如果bird的位置超出螢幕下緣，則將bird的位置設定為螢幕邊界

    def jump(self):
        # 跳躍動作

    def draw(self, screen):
        # 繪製bird