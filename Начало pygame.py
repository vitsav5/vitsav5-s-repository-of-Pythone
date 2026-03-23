import pygame
import random

#Создание размеров окна игры
WIDTH = 360
HEIGHT = 480
FPS = 30

# Создание цветов для игры
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Создание окна и игры
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()

#Создание цикла для игры
running = True
while running:
    #Скорость кадров(повторенмй цикла)
    clock.tick(FPS)
    for event in pygame.event.get():
        #Проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        # Рендеринг
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

pygame.quit()