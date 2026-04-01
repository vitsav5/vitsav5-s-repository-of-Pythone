import pygame as pg
import sys
from random import randint

W = 800
H = 800
WHITE = (255, 255, 255)

'''
origin_surf = pg.image.load('240_F_66999217_7e1XF2RfOqs96cNXxkYzKiUojhtEZYRX.jpg').convert_alpha()
origin_surf.set_colorkey((255, 255, 255))
origin_rect = origin_surf.get_rect(center = (W / 2, H / 2))
sc.blit(origin_surf, origin_rect)
pg.display.update()

pg.time.wait(1000)

new_surf = pg.transform.rotozoom(origin_surf, -45, 0.9)

sc.fill(BG)
new_rect = new_surf.get_rect(center = (W / 2, H / 2))
origin_surf.set_colorkey((255, 255, 255))
sc.blit(new_surf, new_rect)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.wait(1000)
'''

'''
clock = pg.time.Clock()

origin_surf = pg.image.load('240_F_66999217_7e1XF2RfOqs96cNXxkYzKiUojhtEZYRX.jpg').convert_alpha()
origin_surf.set_colorkey((255, 255, 255))

surf_up = origin_surf
surf_up.set_colorkey((255, 255, 255))
surf_down = pg.transform.rotate(origin_surf, 180)
surf_down.set_colorkey((255, 255, 255))
surf_left = pg.transform.rotate(origin_surf, 90)
surf_left.set_colorkey((255, 255, 255))
surf_right = pg.transform.rotate(origin_surf, -90)
surf_right.set_colorkey((255, 255, 255))

current_surf = surf_up
rect = current_surf.get_rect(center = (W // 2, H // 2))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        rect.x -= 3
        current_surf = surf_left
    elif keys[pg.K_RIGHT]:
        rect.x += 3
        current_surf = surf_right
    elif keys[pg.K_UP]:
        rect.y -= 3
        current_surf = surf_up
    elif keys[pg.K_DOWN]:
        rect.y += 3
        current_surf = surf_down

    # Отрисовка
    sc.fill(BG)
    sc.blit(current_surf, rect)
    pg.display.update()

    clock.tick(60)
'''

'''

'''
class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center = (x, 0))

    def update(self):
        if car1.rect.y < H:
            car1.rect.y += 2
        else:
            car1.rect.y = 0

        if car2.rect.y < H:
            car2.rect.y += 2
        else:
            car2.rect.y = 0

        if car3.rect.y < H:
            car3.rect.y += 2
        else:
            car3.rect.y = 0

sc = pg.display.set_mode((W, H))
sc.fill(WHITE)

car1 = Car(randint(1, W), 'Car1.png')
car2 = Car(randint(1, W), 'Car1.png')
car3 = Car(randint(1, W), 'Car1.png')


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    sc.blit(car2.image, car2.rect)
    sc.blit(car3.image, car3.rect)
    pg.display.update()
    pg.time.delay(20)

    car1.update()
    car2.update()
    car3.update()