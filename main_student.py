import pygame
from object import Background, Pipe, Bird, Base

def initial():
    
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return

    pygame.init()
    WIDTH,HEIGHT = 800,500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    background = # 初始化Background物件
    
    base = # 初始化Base物件

    pipes_list = pygame.sprite.Group()
    pygame.time.set_timer(pygame.USEREVENT + 1, 2000)

    bird_animation = [] # 填入Bird的所有圖片路徑
    bird = # 初始化Bird物件

    score = 0
    score_font = pygame.font.SysFont(None, 36)

def start():
    
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
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
        start_rect = start_surface.get_rect(center = (WIDTH*0.5, HEIGHT * 0.83))
        screen.blit(start_surface, start_rect)
        pygame.display.update()



def run():
    
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    
    bird.gravity = 0.03
    running = True
    while running:
        for event in pygame.event.get():
            # 按鍵指令的條件判斷
            
            if event.type == pygame.USEREVENT + 1:
                # 固定時間產生Pipe
                pipes_list.add(new_pipe)
        #更新background
        #更新bird
        #更新base

        for pipe in pipes_list:
            # 判斷bird是否撞到pipe
            # 判斷bird是否超過pipe並加分
            # 更新pipe
        #顯示score
        #更新畫面

def game_over():
    
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    
    running = True
    while running:
        for event in pygame.event.get():
            # 按鍵指令的條件判斷
        
        #更新background
        #更新pipe
        #更新bird
        #更新base

        #顯示GameOver
        #顯示Final Score

        #更新畫面



if __name__ == '__main__':
    try:
        system_running = True
        while system_running :
            initial()
            start()
            run()
            game_over()
        pygame.quit()
    except Exception as e:
        # print(e)
        pass