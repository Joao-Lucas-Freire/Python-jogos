# importando a biblioteca pygame
import pygame as pg
import sys
from game import Game
from menu import Menu
# Criando nossa classe main
class Main():
    def __init__ (self, x, y, title):
        self.window = pg.display.set_mode((x, y))
        self.title = pg.display.set_caption(title)
        self.loop = True
        self.game =  Game()
        self.menu = Menu()
        self.clock = pg.time.Clock()
    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(str(self.game.max_score))

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        else:
            self.loop = False
            
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.save_score()  # salva o recorde mesmo fechando no meio da partida
                pg.quit()
                sys.exit()
            if not self.menu.change_scene:
                self.menu.events(event)
            


    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pg.display.update()
            self.clock.tick(180)  # limita o FPS: o jogo fica um pouco mais lento e igual em qualquer PC

# Criando o jogo
loop =  True
while loop:
    jogo = Main(360, 640, "Flappy Bird")
    jogo.update() 