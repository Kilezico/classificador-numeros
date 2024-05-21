import pygame as pg
from src.utility import pos_add, squared_dist

class DrawSurface:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Cria a superfície branca
        self.surface = pg.Surface((self.width, self.height))
        pg.draw.rect(self.surface, (255, 255, 255), (0, 0, self.width, self.height))
        
        self.last_pos = [0, 0]
        self.pressed = True
        self.max_circle_distance = 81
        self.circle_radius = 15
        self.line_width = 2 * self.circle_radius + 3
    
    def draw(self, window, pos):
        window.blit(self.surface, pos)
    
    def update(self, mouse_offset):
        mouse_pressed = pg.mouse.get_pressed()
        if mouse_pressed[0]:
            pos_atual = pos_add(pg.mouse.get_pos(), mouse_offset) # mouse + offset
            # Se for o primeiro clique, last_pos = pos_atual
            if not self.pressed:
                self.last_pos = pos_atual

            # Desenha uma bola no mouse, mas se duas bolas forem desenhadas muito longe,
            # desenha uma linha entre elas
            pg.draw.circle(self.surface, (0, 0, 0), pos_atual, self.circle_radius)
            if squared_dist(pos_atual, self.last_pos) > self.max_circle_distance:
                pg.draw.line(self.surface, (0, 0, 0), pos_atual, self.last_pos, self.line_width)
            
            # Atualiza as variáveis para a próxima iteração
            self.pressed = True
            self.last_pos = pos_atual
        else:
            self.pressed = False
    
    def reset(self):
        self.surface.fill((255, 255, 255))
    
    def get_image(self):
        return pg.surfarray.array3d(self.surface)
