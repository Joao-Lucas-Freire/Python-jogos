# importando a biblioteca pygame
import pygame as pg
from game import Game
# Criando nossa classe main
class Main():
    def __init__ (self, x, y, title):
        self.window = pg.display.set_mode((x, y))
        self.title = pg.display.set_caption(title)
        self.loop = True
        self.game =  Game()
    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pg.display.update()

# Criando o jogo
jogo = Main(360, 640, "Flappy Bird")
jogo.update()