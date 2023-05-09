import pygame as pg
import sys
import math as m
pg.init()
pg.font.init()

win_x, win_y = 1500, 700
screen = pg.display.set_mode((win_x, win_y))
origin = (450, 500)

def toRadian(degree):
    return m.radians(degree)




class  projectile:
    def __init__(self,degree,k,load) :
        self.degree = degree
        # degree = m.radians(degree)
        self.k = k
        self.load  = load
       

    def getvelocity(self):
        u = (2.415/m.cos(m.radians(self.degree)))*((9.81/(2*2.415*m.tan(m.radians(self.degree))))**(1/2))
        return round(u,2)
    
    def getMaxHeight(self,u):
        h = ((u**2) * (m.sin(m.radians(self.degree))) ** 2) / (2 * 9.81)
        return round(h,2)

class text:
    def __init__(self,text,font2,react,text_color) :
          self.font2 = font2
          self.text =text
          self.text = self.font2.render(self.text, True, text_color)
          self.react = self.text.get_rect(bottomleft= react)
    
    def print(self,screen):
          screen.blit(self.text,self.react)


font2 = pg.font.SysFont("Koulen",25)
pro = projectile(60 ,200,200)
run=True
while run:
    out_vel = text(f"{pro.getvelocity()}",font2,(100,500),(255,255,255))
            # out_springpress = text(f"{sim.getMaxHeight}",font2,(60,150),(255,255,255))
    out_maxH = text(f"{pro.getMaxHeight(pro.getvelocity())}",font2,(100,580),(255,255,255))
    out_vel.print(screen)
            # out_springpress.print(screen)
    out_maxH.print(screen)
  
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.flip()
    pg.display.update()