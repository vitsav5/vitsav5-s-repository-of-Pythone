'''
import random
import pygame
import sys

FPS = 60
W = 700
H = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

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
motion = STOP

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            if i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP

    if motion == LEFT:
        x -= 3
    if motion == RIGHT:
        x += 3
    if motion == UP:
        y -= 3
    if motion == DOWN:
        y += 3

    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    clock.tick(FPS)
'''

# Редактируем
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

    clock.tick(FPS)
'''

# Тут он ещё назад будет возвращаться
''''''
import random
import pygame
import sys

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
motion = STOP

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            if i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP

    if motion == LEFT:
        x -= 3
    if motion == RIGHT:
        x += 3
    if motion == UP:
        y -= 3
    if motion == DOWN:
        y += 3
    if motion == STOP:
        if x > W // 2:
            x -= 3
        if x < W // 2:
            x += 3
        if y > H // 2:
            y -= 3
        if y < H // 2:
            y += 3

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)
    pygame.display.update()

    clock.tick(FPS)