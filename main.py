import pygame
from object import Background, Pipe, Bird, Base


def initial():
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
    if system_running == False: return
    pygame.init()
    WIDTH,HEIGHT = 800,500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    background = Background(img_path='assets/background.png', location=(0, 0), screen_size=(WIDTH, HEIGHT))
    
    base = Base(img_path='assets/base.png', screen_size=(WIDTH, HEIGHT))

    pipes_list = pygame.sprite.Group()
    pygame.time.set_timer(pygame.USEREVENT + 1, 2000)

    bird_animation = ['assets/bird1.png', 'assets/bird2.png', 'assets/bird3.png']
    bird = Bird(img_path=bird_animation, screen_size=(WIDTH, HEIGHT))

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
            if event.type == pygame.QUIT:
                running = False
                system_running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
            if event.type == pygame.USEREVENT + 1:
                new_pipe = Pipe(img_path='assets/pipe.png', screen_size=(WIDTH, HEIGHT))
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
    global WIDTH, HEIGHT, screen, background, pipes_list, bird, score, score_font, base, system_running
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
        game_over_rect = game_over_surface.get_rect(center=(WIDTH * 0.5, HEIGHT * 0.5))
        screen.blit(game_over_surface, game_over_rect)

        score_surface = score_font.render(f'Final Score: {score}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(WIDTH * 0.5, HEIGHT * 0.6))
        screen.blit(score_surface, score_rect)

        pygame.display.update()



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