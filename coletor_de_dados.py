import pygame as pg
from tkinter import *
from tkinter import messagebox
import pickle
import cv2

from src.classifierModel import ClassifierModel
from src.button import Button
from src.drawSurface import DrawSurface
from src.utility import *

menu_height = 80
screenWidth = 400
screenHeight = 480

def run():
    pg.init()
    pg.font.init()

    window = pg.display.set_mode((screenWidth, screenHeight))
    pg.display.set_caption("Coletor de Números")

    clok = pg.time.Clock()

    # Superfície onde serão desenhado os dígitos
    draw_surface = DrawSurface(400, 400)
    contador_de_imagens = 1

    # Modelo treinado para reconhecer dígitos
    # classifier = ClassifierModel("adivinha.pkl")

    font = pg.font.SysFont("Arial", 30)

    predict_but = Button(270, 10, 120, 60, (0, 255, 255), font, "Save")
    reset_but = Button(10, 10, 120, 60, (0, 255, 255), font, "Reset")

    run = True
    while run:
        clok.tick(60)
        # Updates
        draw_surface.update((0, -80)) # compensar pelo menu azul
        predict_but.update()
        reset_but.update()

        # Eventos
        s_was_pressed = False
        r_was_pressed = False
        for event in pg.event.get():
            if event.type == pg.WINDOWCLOSE:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                elif event.key == pg.K_s:
                    s_was_pressed = True
                elif event.key == pg.K_r:
                    r_was_pressed = True
        
        if predict_but.get_pressed() or s_was_pressed:
            path = f"data/data{contador_de_imagens:03}.jpg"
            draw_surface.save_image(path)
            contador_de_imagens += 1
            print("Image saved to", path)
        if reset_but.get_pressed() or r_was_pressed:
            draw_surface.reset()
        
        # Desenha na janela
        pg.display.update()
        window.fill((255, 255, 255))

        draw_surface.draw(window, (0, 80))
        # Área do menuzinho
        pg.draw.rect(window, (50, 70, 255),
                    (0, 0, 400, 80))
        pg.draw.line(window, (0, 0, 0), (0, 80), (400, 80), 2)
        
        predict_but.draw(window)
        reset_but.draw(window)


    pg.quit()


if __name__ == "__main__":
    run()   
