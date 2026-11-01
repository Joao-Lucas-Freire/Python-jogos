# importando o pygame 
import pygame as pg
# imporatndo a classe Obj
pg.init()
from obj import Obj, Heroi

from menu import Menu, GameOver

from game import Game

from obj import Text

# Criando a class Jogo
class Jogo():
    def __init__(self, sizex, sizey, title):  # quando formos criar o objeto dessa classe será passado o tamanho da tela em x e y e o titulo do jogo
        self.window = pg.display.set_mode((sizex, sizey))
        
        self.titulo = pg.display.set_caption((title))  # criando o titulo na janela de acordo com o que o usuario digitar
        self.menu = Menu()
        self.game = Game()
        self.gameover = GameOver()
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
        elif not self.gameover.change_scene:
            # o game terminou (change_scene virou True), então mostra o game over
            self.gameover.tela(self.window)
        else:
            # apertou ENTER no game over: recomeça o jogo
            self.game = Game()
            self.gameover = GameOver()

    # Criando a função eventos para gerir os eventos durante o jogo
    def eventos(self):
        for i in pg.event.get():
            if i.type == pg.QUIT:
                self.loop = False
            self.menu.events(i)
            self.game.events(i)
            self.game.heroi.move_heroi(i)
            if self.game.change_scene:  # só escuta o game over depois que o jogo acabou
                self.gameover.events(i)

    def update(self): # Criando a função para rodar o jogo
        while self.loop:  # enquanto a variavel loop for verdadeira faça
            self.tela()   # chama a variavel tela a variavel eventos e o display.update
            self.eventos()
            pg.display.update()
            self.fps.tick(30)

 #Criando a tela do jogo
jogo = Jogo(360,640, "BeeHoney")
jogo.update()