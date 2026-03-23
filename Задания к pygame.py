# Это прыгающий квадрат
'''
import random
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (213, 30, 80)

FPS = 60
W = 700
H = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (213, 30, 80)

RIGHT = 'to the right'
LEFT = ' to the left'
STOP = 'stop'
UP = 'to the up'
DOWN = 'to the down'

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50
rect_size = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
           if i.key == pygame.K_SPACE:
               x = random.randint(0, 650)
               y = random.randint(0, 250)

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, rect_size, rect_size))
    pygame.display.update()

    clock.tick(FPS)
'''

# Разноцветные фигуры
'''
import random
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 102)

FPS = 60
W = 700
H = 300

RIGHT = 'to the right'
LEFT = ' to the left'
STOP = 'stop'
UP = 'to the up'
DOWN = 'to the down'

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50
rect_size = 50
color = BLACK
colorfon = WHITE

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
           if i.key == pygame.K_r:
               color = RED
           if i.key == pygame.K_g:
               color = GREEN
           if i.key == pygame.K_b:
               color = BLUE
           if i.key == pygame.K_y:
               colorfon = YELLOW
           if i.key == pygame.K_w:
               colorfon = WHITE
           if i.key == pygame.K_l:
               colorfon = BLACK

    sc.fill(colorfon)
    pygame.draw.rect(sc, color, (x, y, rect_size, rect_size))
    pygame.display.update()

    clock.tick(FPS)
'''

'''
import random
import pygame
import sys

FPS = 60
W = 700
H = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 70, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > r:
        x -= 3
    if keys[pygame.K_RIGHT] and x < W - r:
        x += 3
    if keys[pygame.K_UP] and y > r:
        y -= 3
    if keys[pygame.K_DOWN] and y < H - r:
        y += 3

    clock.tick(FPS)
'''

'''
import random
import pygame
import sys

FPS = 60
W = 700
H = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 70, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 3
    if keys[pygame.K_RIGHT]:
        x += 3
    if keys[pygame.K_UP]:
        y -= 3
    if keys[pygame.K_DOWN]:
        y += 3
    if x < -70:
        x = 760
    if x > 770:
        x = -60
    if y < -70:
        y = 360
    if y > 370:
        y = -60
    clock.tick(FPS)
'''

'''
import random
import pygame
import sys

FPS = 60
W = 700
H = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 102)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50
color = BLUE
colorfon = WHITE
control = True

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_r:
                color = RED
            if i.key == pygame.K_g:
                color = GREEN
            if i.key == pygame.K_b:
                color = BLUE
            if i.key == pygame.K_y:
                colorfon = YELLOW
            if i.key == pygame.K_w:
                colorfon = WHITE
            if i.key == pygame.K_l:
                colorfon = BLACK

    sc.fill(colorfon)
    pygame.draw.circle(sc, color, (x, y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 3
        control = True
    if keys[pygame.K_RIGHT]:
        x += 3
        control = True
    if keys[pygame.K_UP]:
        y -= 3
        control = True
    if keys[pygame.K_DOWN]:
        y += 3
        control = True
    if keys[pygame.K_SPACE] and control == True:
        x = random.randint(50, 650)
        y = random.randint(50, 250)
        control = False
    if x < -70:
        x = 760
    if x > 770:
        x = -60
    if y < -70:
        y = 360
    if y > 370:
        y = -60
    clock.tick(FPS)
'''

''''''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((700, 400), 0, 32)
pygame.display.set_caption('Рисование')
clock = pygame.time.Clock()
FPS = 60
control = True

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)
BROWN = (150, 75, 0)
WIGHT_and_BROWN = (150, 100, 0)

x = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > -70:
        x -= 3
    if keys[pygame.K_RIGHT] and x < 450:
        x += 3
    if keys[pygame.K_SPACE]:
        control = False


    # Дом
    pygame.draw.rect(DISPLAYSURF, RED, (310, 100, 50, 100))
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((370, 200), (130, 200), (250, 20)))
    pygame.draw.rect(DISPLAYSURF, BROWN, (150, 200, 200, 200))
    pygame.draw.rect(DISPLAYSURF, WIGHT_and_BROWN, (220, 300, 50, 100))
    # Снеговик
    pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 380), 70)
    pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 290), 55)
    pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 210), 45)
    pygame.draw.line(DISPLAYSURF, BLACK, (40, 220), (100, 220), 4)
    if control == True:
        pygame.draw.circle(DISPLAYSURF, BLACK, (50, 190), 7)
        pygame.draw.circle(DISPLAYSURF, BLACK, (90, 190), 7)
    else:
        pygame.draw.line(DISPLAYSURF, BLACK, (40, 190), (60, 190), 2)
        pygame.draw.line(DISPLAYSURF, BLACK, (80, 190), (100, 190), 2)
    control = True
    # Машина
    pygame.draw.rect(DISPLAYSURF, RED, (x + 80, 330, 150, 50))
    pygame.draw.rect(DISPLAYSURF, RED, (x + 105, 280, 100, 50))
    pygame.draw.circle(DISPLAYSURF, BLACK, (x + 110, 380), 20)
    pygame.draw.circle(DISPLAYSURF, BLACK, (x + 200, 380), 20)
    pygame.display.update()
    clock.tick(FPS)
    DISPLAYSURF.fill(GRAY)