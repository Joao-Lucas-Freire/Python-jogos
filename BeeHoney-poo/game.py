import pygame as pg
from obj import Obj
import random


class Game:
    def __init__(self):
        self.bg = Obj("imagem/bg.png", 0, 0)
        self.bg2 = Obj("imagem/bg.png", 0, -640)
        self.change_scene = False
        self.spider = Obj("imagem/spider1.png", random.randrange(0,360), 200)
        self.flower = Obj("imagem/florwer1.png", random.randrange(0, 360), 200)


    def tela(self, window):
        self.bg.mostrar(window)
        self.bg2.mostrar(window)
        self.spider.mostrar(window)
        self.flower.mostrar(window)

    def update(self):
        self.moverbg()
        self.spider.anim("spider", 8, 5)
        self.flower.anim("florwer", 4, 3)
        self.move_spider()
        self.move_flower()

    def moverbg(self):
        self.bg.sprite.rect.y += 20
        self.bg2.sprite.rect.y += 20
        if self.bg.sprite.rect.y >= 640:
            self.bg.sprite.rect.y = 0
        elif self.bg2.sprite.rect.y >=0:
            self.bg2.sprite.rect.y = - 640


    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DELETE:
                self.change_scene = True


    def move_spider(self):
        self.spider.sprite.rect.y += 10
        if self.spider.sprite.rect.y >= 700:
            self.spider.sprite.kill() # dessa forma ao arannha sair da tela ela é eliminada
            self.spider = Obj("imagem/spider1.png", random.randrange(10,350), -50)

    def move_flower(self):
            self.flower.sprite.rect.y += 10
            if self.flower.sprite.rect.y >= 700:
                self.flower.sprite.kill()
                self.flower = Obj("imagem/florwer1.png", random.randrange(10, 350), - 50 )
                