# importando a biblioteca pygame
import pygame as pg
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
    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update()

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        else:
            self.loop = False
            
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.loop = False 
            if not self.menu.change_scene:
                self.menu.events(event)
            


    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pg.display.update() 

# Criando o jogo
loop =  True
while loop:
    jogo = Main(360, 640, "Flappy Bird")
    jogo.update() 