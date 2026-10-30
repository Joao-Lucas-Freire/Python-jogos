import pygame as pg
from obj import Obj

class Menu():
    def __init__(self):

        self.bg = Obj("Imagem/start.png",0,0)
        self.change_scene = False

    def tela(self,window):
        self.bg.group.draw(window)

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.change_scene = True