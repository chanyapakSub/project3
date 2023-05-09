import pygame as pg
import math
pg.init()
win_x, win_y = 800, 450 
screen = pg.display.set_mode((win_x, win_y))
c1,c2,c3 = 200,0,200 #สี
r = 20
t = 0
a = 1
sx,sy = (win_x/2)+r,win_y
u = 20
axis = 60
rad = axis*(3.14)/180
while(1) :
    # temx = sx
    # temy = sy
    screen.fill((255,255,255))
    pg.draw.circle(screen, (c1,c2,c3), (sx,sy), r)
    t += 0.05
    sx = u*(math.cos(rad))*t
    sy = 450 - (u*(math.sin(rad))*t - 0.5*a*(t**2))
    pg.display.update()
    pg.time.delay(0)
    print(sx,sy)
    # if sy > win_y : 
    #     sx = temx
    #     sy = temy
    #     t = 0

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit()
            exit()   
        
pg.time.delay(200)