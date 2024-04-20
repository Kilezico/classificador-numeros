import pygame as pg
from src.utility import *

class Button:
    def __init__(self, x, y, width, height, color, font, label, label_color=(0, 0, 0)):
        self.hitbox = pg.rect.Rect(x, y, width, height)
        self.border_radius = int(self.hitbox.height/4)

        self.color = color
        self.pressed_color = tuple(map(lambda x: int(x*0.7), color)) # Cor mais escura

        self.pressing = False
        self.pressed = False

        self.font = font
        self.label = label
        self.label_color = label_color

    
    def draw(self, win):
        if not self.pressing:
            pg.draw.rect(win, self.color, self.hitbox, border_radius=self.border_radius)
        else:
            pg.draw.rect(win, self.pressed_color, self.hitbox, border_radius=self.border_radius)
        
        pg.draw.rect(win, (0, 0, 0), self.hitbox, width=1, border_radius=self.border_radius)
        
        # Desenha texto no centro do botao
        text_surface = self.font.render(self.label, True, (0, 0, 0))
        win.blit(text_surface, (self.get_center()[0] - text_surface.get_width()/2,
                                self.get_center()[1] - text_surface.get_height()/2))
    
    def update(self):
        # Detecta colisão com o mouse
        mouse_pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if mouse_pressed[0] and collision_point_rect(mouse_pos, self.hitbox):
            self.pressing = True
        elif not mouse_pressed[0] and self.pressing:
            self.pressing = False
            self.pressed = True
        
    def get_pressed(self):
        # O status de pressed fica no butao até essa funcao ser chamada
        # para a função do botão ser executada. Quando isso acontecer
        # o status pressed vai ficar False
        if self.pressed:
            self.pressed = False
            return True
        return False

    def get_center(self):
        return (self.hitbox.x + self.hitbox.width/2, self.hitbox.y + self.hitbox.height/2)
