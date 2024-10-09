import pygame as pg
import random

pg.init()
clock = pg.time.Clock()

w, h = 800, 600
screen = pg.display.set_mode((w,h))

hitbox = pg.Rect(100, 240, 70, 40)
accel = 3
spdy = 0
state = 0

tl = random.randint(130, 270)
bl = h - tl - 200
top = pg.Rect(800, -270 +tl, 100, 270)
bot = pg.Rect(800, h-bl, 100, bl)
score = 0

bird = pg.image.load('C:/Users/Angela/Downloads/PY1/bird.png')
bird = pg.transform.scale(bird, (70,50))

pipeU = pg.image.load('C:/Users/Angela/Downloads/PY1/pipe.png')
pipeU = pg.transform.scale(pipeU, (100,270))
pipeD = pg.transform.rotate(pipeU, 180)

while True:

    while state == 0:
        pg.event.pump()

        mouse = pg.mouse.get_pressed()

        if mouse[0]:
            state = 1

        screen.fill((0,0,0))
        screen.blit(bird, hitbox)
        pg.display.flip()
        clock.tick(30)

    while state == 1:

        pg.event.pump()

        hitbox[1] += spdy
        spdy += accel

        top[0] -= 10
        bot[0] -= 10

        mouse = pg.mouse.get_pressed()

        if mouse[0]:
            spdy = -20

        if hitbox[1] >= 570 or hitbox.colliderect(top) or hitbox.colliderect(bot):
            clock.tick(1)
            state = 2

        if top[0] <= - 90:
            score+=1
            top[0] = 790
            bot[0] = 790
            tl = random.randint(130, 270)
            bl = h - tl - 200
            top[1] = -270 + tl
            bot[3] = bl
            bot[1] = h-bl

        screen.fill((0,0,0))
        screen.blit(bird, hitbox)
        screen.blit(pipeU, top)
        screen.blit(pipeD, bot)
        pg.display.flip()
        clock.tick(30)

    while state == 2:
        pg.event.pump()

        mouse = pg.mouse.get_pressed()

        hitbox[1] = 240
        top[0] = 790
        bot[0] = 790

        if mouse[0]:
            state = 1
            tl = random.randint(130, 270)
            top[1] = -270 + tl
            bl = h - tl - 200
            bot[3] = bl
            bot[1] = h-bl


        screen.fill((0,0,0))
        screen.blit(bird, hitbox)
        pg.display.flip()
        clock.tick(30)
