import pygame as pg
import sys
import math as m
pg.init()
pg.font.init()
font = pg.font.SysFont("Koulen",36)
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        
    def draw(self,screen,color,border_radius):
        pg.draw.rect(screen,(color),(self.x,self.y,self.w,self.h),0,border_radius)

class Button(Rectangle):
    def __init__(self,x, y, w, h, text_input , font1 , base_color,hovering_color):
        Rectangle.__init__(self, x, y, w, h)
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=((self.x+(self.w/2)), self.y+(self.h/2)))

    def isMouseOn(self):
   
        mx,my = pg.mouse.get_pos()
        if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
            return True
            
        else :
           return False
    def isMousePress(self):
        if pg.mouse.get_pressed()[0]:
           return True
        else :
           return False
        
    def changeColor(self):
        mx,my = pg.mouse.get_pos()
        if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
            return True
        else:self.text = self.font.render(self.text_input, True, self.base_color)
    def update(self, screen):
	    screen.blit(self.text, self.text_rect,)
    

class text:
    def __init__(self,text,font2,react,text_color) :
          self.font2 = font2
          self.text =text
          self.text = self.font2.render(self.text, True, text_color)
          self.react = self.text.get_rect(bottomleft= react)
    
    def print(self,screen):
          screen.blit(self.text,self.react)

class InputBox:

    def __init__(self, x, y, w, h, canAlpha, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.canalpha = canAlpha

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.canalpha:
                        self.text += event.unicode
                    elif not self.canalpha:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class  projectile:
    def __init__(self,degree,k,load) :
        self.degree = degree
        # degree = m.radians(degree)
        self.k = k
        self.load  = load
       
    def getvelocity(self):
        u = (2.403/m.cos(m.radians(self.degree)))*((9.81/(2*2.403*m.tan(m.radians(self.degree))))**(1/2))
        return round(u,2)
    
    def getMaxHeight(self,u):
        h = ((u**2) * (m.sin(m.radians(self.degree))) ** 2) / (2 * 9.81)
        return round(h,2)
    
    def getspringpress(self,u):
        x = (2*(self.load*(10**-3))*9.81*(m.sin(m.radians(self.degree))) + (4*self.k*(self.load*(10**-3))*(u**2))**0.5)/(2*self.k)
        return round(x,3)


# def pixel(self):
    


#เซ็ตค่าหน้าจอ,ฟ้อน
win_x = 1200
win_y = 700
posx ,posy = 450 ,500
screen = pg.display.set_mode((win_x, win_y))
pg.display.set_caption("Simulation Program Group 6")
background = pg.Color(141,198,191)
font = pg.font.SysFont("Koulen",36)
font2 = pg.font.SysFont("Koulen",25)
pg.mouse.set_visible( True )
COLOR_INACTIVE = pg.Color(225,225,225) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(252,188,102)     # ^^^
FONT = pg.font.SysFont("Koulen", 25)

#แถบ input
menu = Rectangle(30,30,280,370)
info_setting=Button(110,10,120,50,text_input="setting",font1=font,base_color=(88,64,83),hovering_color=None)
btn_reset = Button(60,300,80,50,text_input="reset",font1=font,base_color="white",hovering_color=(88,64,83))
btn_run = Button(200,300,80,50,text_input="run",font1=font,base_color=(88,64,83),hovering_color="white")

info_degree = text("degree",font2,(60,100),(255,255,255))
info_spring = text("spring constant",font2,(60,150),(255,255,255))
info_load = text("load",font2,(60,200),(255,255,255))
run=True

input_degree = InputBox(200, 75, 50, 30,False) # สร้าง InputBox1
input_spring = InputBox(200, 125, 50, 30,False) # สร้าง InputBox2
input_load = InputBox(200, 175, 50, 30,False)
input_boxes = [input_degree, input_spring, input_load]

#แถบ out put
menu2 = Rectangle(30,430,280,200)
info_output = Button(110,420,120,50,text_input="output",font1=font,base_color=(225,225,225),hovering_color=None)
info_vel = text("velocity :",font2,(60,500),(88,64,83))
info_springpress = text("spring press :",font2,(60,540),(88,64,83))
info_maxH = text("Maximum high : ",font2,(60,580),(88,64,83))

#simulation
bg = Rectangle(400,100,700,500)
wall = Rectangle(750,300,10,200)
origin = (450, 500)
sx = 450
sy = 500
start = False
sim = projectile(input_degree,input_spring,input_load)
# end = sim.getPosOnCircumeference(origin)
show = False
t = 0
while run:
    screen.fill(background)  
    #วาดเมนู
    menu.draw(screen,(88,64,83),border_radius=10)
    menu2.draw(screen,(252,188,102),border_radius=10)
    info_setting.draw(screen,(252,188,102),border_radius=10)
    info_setting.update(screen)
    info_output.draw(screen,(88,64,83),border_radius=10)
    info_output.update(screen)
    #วาดปุ่ม reset
    btn_reset.changeColor()
    btn_reset.draw(screen,(249,123,79),border_radius=10)
    btn_reset.update(screen)
    #วาดปุ่ม run
    btn_run.changeColor()
    btn_run.draw(screen,(249,123,79),border_radius=10)
    btn_run.update(screen)
    #รับ input
    info_degree.print(screen)
    info_spring.print(screen)
    info_load.print(screen)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen)
    #output 
    info_vel.print(screen)
    info_springpress.print(screen)
    info_maxH.print(screen)




    #simulation
    bg.draw(screen,(225,225,225),10)
    wall.draw(screen,(0,0,0),0)
    pg.draw.line(screen, (0,0,0), origin, (origin[0] + 600, origin[1]), 2)
    pg.draw.line(screen, (0,0,0), origin, (origin[0], origin[1] - 300), 2)
    # pg.draw.line(screen, (0,0,0), origin, end, 2)
  

    if btn_run.isMouseOn() and btn_run.isMousePress():
        if input_degree.text != '' and input_spring.text != '' and input_load.text != '':
            sim = projectile(float(input_degree.text),float(input_spring.text),float(input_load.text))
            out_vel = text(f"{sim.getvelocity()} m/s",font2,(200,500),(88,64,83))
            out_springpress = text(f"{sim.getspringpress(sim.getvelocity())} m ",font2,(200,540),(88,64,83))
            out_maxH = text(f"{sim.getMaxHeight(sim.getvelocity())} m ",font2,(200,580),(88,64,83))
            out_vel.print(screen)
            out_springpress.print(screen)
            out_maxH.print(screen)
            show = True
            start = True

        

    if show:
        out_vel.print(screen)
        out_springpress.print(screen)
        out_maxH.print(screen)
    
    if btn_reset.isMouseOn() and btn_reset.isMousePress():
        show = False
        input_degree.text = None
        input_spring.text = None
        input_load.text = None
    
    while start:
    # #simulation
        if sy>500:
            start = False
        
        bg.draw(screen,(225,225,225),10)
        wall.draw(screen,(0,0,0),0)
        pg.draw.line(screen, (0,0,0), origin, (origin[0] + 600, origin[1]), 2)
        pg.draw.line(screen, (0,0,0), origin, (origin[0], origin[1] - 300), 2)
        # pg.draw.line(screen, (0,0,0), origin, 100*m.cos(m.radians(int(input_degree.text))), 2)
        pg.draw.circle(screen,(100,100,100),(sx,sy),10) 
        sx = 450 + (sim.getvelocity()*m.cos(m.radians(int(input_degree.text)))*227)*(t)
        sy = 500 - (227*(sim.getvelocity()*(m.sin(m.radians(int(input_degree.text)))))*t - 0.5*9.81*227*(t**2))
        # sx= sim.getvelocity()*m.cos(m.radians(int(input_degree.text)))*(t)
        # sy= sx * m.tan(m.radians(int(input_degree.text)))- 0.5*((9.81*(sx**2))/((sim.getvelocity()**2)*((m.cos(m.radians(float(input_degree.text)))**2))))

        t += 0.001
        pg.display.update()

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    pg.display.flip()
   