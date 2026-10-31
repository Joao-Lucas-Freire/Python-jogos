# importando o pygame 
import pygame as pg
# imporatndo a classe Obj
from obj import Obj

from menu import Menu

from game import Game

# Criando a class Jogo
class Jogo():
    def __init__(self, sizex, sizey, title):  # quando formos criar o objeto dessa classe será passado o tamanho da tela em x e y e o titulo do jogo
        self.window = pg.display.set_mode((sizex, sizey))
        
        self.titulo = pg.display.set_caption((title))  # criando o titulo na janela de acordo com o que o usuario digitar
        self.menu = Menu()
        self.game = Game()
        self.loop = True  # criando um loop inicia no true
        # controlando o fps
        self.fps = pg.time.Clock() 

# criando a função tela para mostrar os itens na tela
    def tela(self):
        if not self.menu.change_scene:
            self.menu.tela(self.window)
        elif not self.game.change_scene:
            self.game.tela(self.window)
            self.game.update()

    # Criando a função eventos para gerir os eventos durante o jogo
    def eventos(self):
        for i in pg.event.get():
            if i.type == pg.QUIT:
                self.loop = False
            self.menu.events(i)
            self.game.events(i)

    def update(self): # Criando a função para rodar o jogo
        while self.loop:  # enquanto a variavel loop for verdadeira faça
            self.tela()   # chama a variavel tela a variavel eventos e o display.update
            self.eventos()
            pg.display.update()
            self.fps.tick(30)

 #Criando a tela do jogo
jogo = Jogo(360,640, "BeeHoney")
jogo.update()