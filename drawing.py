'''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Рисование')

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)

DISPLAYSURF.fill(GRAY)
pygame.draw.polygon(DISPLAYSURF, YELLOW, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120), 10)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.ellipse(DISPLAYSURF, BLUE, (300, 50, 40, 40), 5)
pygame.draw.ellipse(DISPLAYSURF, RED, (10, 300, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (380, 20, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

'''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Рисование')

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)

DISPLAYSURF.fill(WIGHT)
pygame.draw.polygon(DISPLAYSURF, YELLOW, ((350, 100), (150, 100), (250, 20)))
pygame.draw.rect(DISPLAYSURF, RED, (150, 100, 200, 200))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[474][380] = BLACK
pixObj[468][380] = BLACK
pixObj[462][380] = BLACK
pixObj[456][380] = BLACK
pixObj[456][374] = BLACK
pixObj[456][368] = BLACK
pixObj[456][362] = BLACK
pixObj[456][356] = BLACK
pixObj[462][356] = BLACK
pixObj[468][356] = BLACK
pixObj[474][356] = BLACK
pixObj[480][356] = BLACK
pixObj[468][362] = BLACK
pixObj[474][362] = BLACK
pixObj[480][362] = BLACK
pixObj[462][362] = BLACK
pixObj[468][368] = BLACK
pixObj[474][368] = BLACK
pixObj[480][368] = BLACK
pixObj[462][368] = BLACK
pixObj[462][374] = BLACK
pixObj[468][374] = BLACK
pixObj[474][374] = BLACK
pixObj[480][374] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

'''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Рисование')

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)
BROWN = (150, 75, 0)
WIGHT_and_BROWN = (150, 100, 0)

DISPLAYSURF.fill(GRAY)
# Дом
pygame.draw.polygon(DISPLAYSURF, BLACK, ((370, 200), (130, 200), (250, 20)))
pygame.draw.rect(DISPLAYSURF, BROWN, (150, 200, 200, 200))
pygame.draw.rect(DISPLAYSURF, WIGHT_and_BROWN, (220, 300, 50, 100))
# Машина
pygame.draw.rect(DISPLAYSURF, RED, (330, 330, 150, 50))
pygame.draw.rect(DISPLAYSURF, RED, (355, 280, 100, 50))
pygame.draw.circle(DISPLAYSURF, BLACK, (360, 380), 20)
pygame.draw.circle(DISPLAYSURF, BLACK, (450, 380), 20)
# Снеговик
pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 380), 70)
pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 290), 55)
pygame.draw.circle(DISPLAYSURF, WIGHT, (70, 210), 45)
pygame.draw.line(DISPLAYSURF, BLACK, (40, 220), (100, 220), 4)
pygame.draw.circle(DISPLAYSURF, BLACK, (50, 190), 7)
pygame.draw.circle(DISPLAYSURF, BLACK, (90, 190), 7)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

'''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Рисование')

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)
BROWN = (150, 75, 0)
WIGHT_and_BROWN = (150, 100, 0)

DISPLAYSURF.fill(WIGHT)

a = pygame.Surface((100, 100))
a.set_alpha(84)
a.fill((0, 255, 0))

b = pygame.Surface((100, 100))
b.set_alpha(84)
b.fill((255, 0, 0))

c = pygame.Surface((100, 100))
c.set_alpha(84)
c.fill((0, 0, 255))

d = pygame.Surface((100, 100))
d.set_alpha(128)
d.fill((34, 90, 107))

DISPLAYSURF.blit(a, (150, 100))
DISPLAYSURF.blit(b, (200, 100))
DISPLAYSURF.blit(c, (175, 125))
DISPLAYSURF.blit(d, (175, 250))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

''''''
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000, 635), 0, 32)
pygame.display.set_caption('Animation')

WIGHT = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 102)
BROWN = (150, 75, 0)
WIGHT_and_BROWN = (150, 100, 0)

pepeImg = pygame.image.load('png-clipart-memes-man-meme-thumbnail.png')
pepex = 0
pepey = 0
direction = 'right1'

while True:
    DISPLAYSURF.fill(BLACK)

    if direction == 'right1':
        pepex += 10
        if pepex == 650:
            direction = 'down1'
    elif direction == 'down1':
        pepey += 20
        if pepey == 220:
            direction = 'left1'
    elif direction == 'left1':
        pepex -= 10
        if pepex == 0:
            direction = 'down2'
    elif direction == 'down2':
        pepey += 20
        if pepey == 420:
            direction = 'right2'
    if direction == 'right2':
        pepex += 10
        if pepex == 650:
            direction = 'up1'
    elif direction == 'up1':
        pepey -= 20
        if pepey == 220:
            direction = 'left2'
    elif direction == 'left2':
        pepex -= 10
        if pepex == 0:
            direction = 'up2'
    elif direction == 'up2':
        pepey -= 20
        if pepey == 0:
            direction = 'right1'

    DISPLAYSURF.blit(pepeImg, (pepex, pepey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)