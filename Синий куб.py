import pygame
import random

#Создание размеров окна игры
WIDTH = 360
HEIGHT = 480
FPS = 60

# Создание цветов для игры
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Параметры куба
rect_size = 50
x = WIDTH // 2 #Начальная позиция по x
y = HEIGHT // 2 #Начальная позиция по y
speed_x = 5 #Скорость куба по горизонтали
speed_y = 5 #Скорость куба по вертикали

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движущийся квадрат')
clock = pygame.time.Clock()

shape_type = 'rect'

if shape_type == pygame.KEYDOWN:
    if event.key == pygame.K_F1: shape_type = 'rect'
    if event.key == pygame.K_F2: shape_type = 'circle'

#Создание цикла для игры
running = True
while running:
    #Скорость кадров(повторенмй цикла)
    clock.tick(FPS)

    #1. Ввод (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #2. Обновление (логика движения)
    x += speed_x
    y += speed_y

    #Проверка столкновения с границей (отскок)
    if x + rect_size > WIDTH or x < 0:
        speed_x = -speed_x #Меняет направление по x
    if y + rect_size > WIDTH or y < 0:
        speed_y = -speed_y  # Меняет направление по y

    #3. Рендеринг (отрисовка)
    screen.fill(BLACK)

    #Рисуем квадрат: (где, цвет, (x, y, ширина, высота))
    if shape_type == 'rect':
        pygame.draw.rect(screen, BLUE, (x, y, rect_size, rect_size))
    if shape_type == 'circle':
        pygame.draw.circle(screen, BLUE, (x + 25, y + 25), 25)

    pygame.display.flip()

pygame.quit()