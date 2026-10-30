import pygame as pg
from obj import Obj

class Game:
    def __init__(self):
        self.bg = Obj("imagem/bg.png", 0, 0)
        self.bg2 = Obj("imagem/bg.png", 0, -640)
        self.change_scene = False

    def tela(self, window):
        self.bg.mostrar(window)
        self.bg2.mostrar(window)

    def update(self):
        self.bg.sprite.rect.y += 1
        self.bg2.sprite.rect.y += 1
        if self.bg.sprite.rect.y >=640:
            self.bg.sprite.rect.y = -640

        if self.bg.sprite.rect.y >=640:
            self.bg.sprite.rect.y = -640

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DELETE:
                self.change_scene == True