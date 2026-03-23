import pygame
import random

COLOR_WIGHT = (255, 255, 255)
COLOR_YELLOW = (255, 255, 102)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (213, 50, 80)
COLOR_GREEN = (255, 255, 102)
COLOR_BLUE = (0, 100, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Параметры игры
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('vitsav.INK')

clock = pygame.time.Clock()

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render(f'Ваш счёт: {score}', True, COLOR_YELLOW)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, COLOR_RED, [x[0], x[1], block_size, block_size])

def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
    screen.blit(mesg, text_rect)

def generate_food():
    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    return foodx, foody



def game_loop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    foodx, foody = generate_food()

    while not game_over:

        while game_close:
            screen.fill(COLOR_BLUE)
            show_message('Ну лох, Q - Выход, C - перезапуск', COLOR_RED)
            display_score(lenght_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Перезапуск
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_WIDTH or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(COLOR_BLUE)

        # Рисуем еду
        pygame.draw.rect(screen, COLOR_GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Логика роста змейки
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(lenght_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            lenght_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()
game_loop()