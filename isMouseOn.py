import pygame as pg
import sys
import math
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
    def __init__(self, x, y, w, h , text_input , font1 , base_color,hovering_color):
        Rectangle.__init__(x, y, w, h)
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
    def update(self, screen):
	    screen.blit(self.text, self.text_rect,)
    
    def changeColor(self):
        mx,my = pg.mouse.get_pos()
        if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
            return True
        else:self.text = self.font.render(self.text_input, True, self.base_color)




# class Button(Rectangle):
# 	def __init__(self, x,y,w,h , text_input,font1, base_color, hovering_color):
# 		Rectangle.__init__(self, x, y, w, h)
# 		self.font = font
# 		self.base_color, self.hovering_color = base_color, hovering_color
# 		self.text_input = text_input
# 		self.text = self.font.render(self.text_input, True, self.base_color)
# 		self.text_rect = self.text.get_rect(center=((self.x+(self.w/2)), self.y+(self.h/2)))
   


# 	def update(self, screen):
# 		screen.blit(self.text, self.text_rect,)


# 	def changeColor(self):
# 		mx,my = pg.mouse.get_pos()
# 		if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
# 			self.text = self.font.render(self.text_input, True, self.hovering_color)
            
# 		else: self.text = self.font.render(self.text_input, True, self.base_color)
    
    
#     def isMouseOn(self):
   
#         mx,my = pg.mouse.get_pos()
#         if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
#             return True
            
#         else :
#            return False
        
#     def isMousePress(self):
#         if pg.mouse.get_pressed()[0]:
#            return True
#         else :
#            return False