import pygame
import random

class Background():
    def __init__(self,img_path,location,screen_size):
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = location
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Base():
    def __init__(self, img_path, screen_size):
        self.image = pygame.image.load(img_path)
        self.width, self.height = screen_size
        self.image = pygame.transform.scale(self.image,(self.width, self.height/10))
        self.base_width = self.image.get_width()
        self.x1 = 0
        self.x2 = self.base_width
        self.y = self.height - self.image.get_height()
        self.movement_speed = 0.8

    def update(self):
        self.x1 -= self.movement_speed
        self.x2 -= self.movement_speed

        if self.x1 + self.base_width < 0:
            self.x1 = self.x2 + self.base_width

        if self.x2 + self.base_width < 0:
            self.x2 = self.x1 + self.base_width

    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))

class Pipe(pygame.sprite.Sprite):
    def __init__(self, img_path, screen_size):
        super(Pipe, self).__init__()
        self.image = pygame.image.load(img_path)
        self.screen_width, self.screen_height = screen_size
        self.screen_height*=0.9
        self.gap_size = self.screen_height*0.3
        self.score_counted = False

    def generate_pipe(self):
        self.top_pipe = pygame.transform.flip(self.image, False, True)
        self.bottom_pipe = self.image
        self.top_pipe_scale = random.randint(int(self.screen_height*0.05), int(self.screen_height*0.75 - self.gap_size))
        self.bottom_pipe_scale = self.screen_height*0.9 - self.top_pipe_scale - self.gap_size
        self.top_pipe = pygame.transform.scale(self.top_pipe, (self.top_pipe.get_width(), self.top_pipe_scale))
        self.bottom_pipe = pygame.transform.scale(self.bottom_pipe, (self.bottom_pipe.get_width(), self.bottom_pipe_scale))        
        self.top_pipe_rect = self.top_pipe.get_rect()
        self.bottom_pipe_rect = self.bottom_pipe.get_rect()
        self.top_pipe_rect.topleft = (self.screen_width, 0)
        self.bottom_pipe_rect.bottomleft = (self.screen_width, self.screen_height)  # 顶部管道位置
        
    def update(self):
        self.top_pipe_rect.x -= 1
        self.bottom_pipe_rect.x -= 1
        if self.top_pipe_rect.right <= 0 and self.bottom_pipe_rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.top_pipe, self.top_pipe_rect)
        screen.blit(self.bottom_pipe, self.bottom_pipe_rect)

class Bird(pygame.sprite.Sprite):
    def __init__(self, img_path, screen_size):
        super(Bird, self).__init__()
        self.images = [pygame.image.load(img) for img in img_path]
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

        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0

        if self.rect.bottom > self.screen_height*0.9:
            self.rect.bottom = self.screen_height*0.9
            self.velocity = 0

    def jump(self):
        if self.velocity >= 0:
            self.velocity = self.jump_height

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def initial():
    global WEIGHT, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    pygame.init()
    WEIGHT,HEIGHT = 800,500
    screen = pygame.display.set_mode((WEIGHT, HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    background = Background(img_path='assets/background.png', location=(0, 0), screen_size=(WEIGHT, HEIGHT))
    
    base = Base(img_path='assets/base.png', screen_size=(WEIGHT, HEIGHT))

    pipes_list = pygame.sprite.Group()
    pygame.time.set_timer(pygame.USEREVENT + 1, 2000)

    bird_animation = ['assets/bird1.png', 'assets/bird2.png', 'assets/bird3.png']
    bird = Bird(img_path=bird_animation, screen_size=(WEIGHT, HEIGHT))

    score = 0
    score_font = pygame.font.SysFont(None, 36)

def start():
    global WEIGHT, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                system_running = False
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    break

        background.draw(screen)
        bird.update()
        bird.draw(screen)
        base.update()
        base.draw(screen)

        for pipe in pipes_list:
            pipe.update()
            pipe.draw(screen)
        score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        start_font = pygame.font.SysFont(None, 45)
        start_surface = start_font.render('Press Space to Start', True, (255, 255, 255))
        start_rect = start_surface.get_rect(center = (WEIGHT*0.5, HEIGHT * 0.83))
        screen.blit(start_surface, start_rect)
        pygame.display.update()



def run():
    global WEIGHT, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    bird.gravity = 0.03
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                system_running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
            if event.type == pygame.USEREVENT + 1:
                new_pipe = Pipe(img_path='assets/pipe.png', screen_size=(WEIGHT, HEIGHT))
                new_pipe.generate_pipe()
                pipes_list.add(new_pipe)

        background.draw(screen)
        bird.update()
        bird.draw(screen)
        base.update()
        base.draw(screen)

        for pipe in pipes_list:
            if ( bird.rect.colliderect(pipe.top_pipe_rect) or bird.rect.colliderect(pipe.bottom_pipe_rect)):
                running = False
                break
            elif not pipe.score_counted and bird.rect.left > pipe.top_pipe_rect.right and bird.rect.left > pipe.bottom_pipe_rect.right:
                score += 1
                pipe.score_counted = True
            pipe.update()
            pipe.draw(screen)
        score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        pygame.display.update()



def game_over():
    global WEIGHT, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                system_running = False
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

        background.draw(screen)
        for pipe in pipes_list:
            pipe.draw(screen)
        bird.draw(screen)
        base.draw(screen)

        game_over_font = pygame.font.SysFont(None, 45)
        game_over_surface = game_over_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center=(WEIGHT * 0.5, HEIGHT * 0.5))
        screen.blit(game_over_surface, game_over_rect)

        score_surface = score_font.render(f'Final Score: {score}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(WEIGHT * 0.5, HEIGHT * 0.6))
        screen.blit(score_surface, score_rect)

        pygame.display.update()



if __name__ == '__main__':
    system_running = True
    while system_running :
        initial()
        start()
        run()
        game_over()