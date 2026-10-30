# importando o pygame 
import pygame as pg
# imporatndo a classe Obj
from obj import Obj


# Criando a class Jogo
class Jogo():
    def __init__(self, sizex, sizey, title):  # quando formos criar o objeto dessa classe será passado o tamanho da tela em x e y e o titulo do jogo
        self.window = pg.display.set_mode((sizex, sizey))
        self.titulo = pg.display.set_caption((title))  # criando o titulo na janela de acordo com o que o usuario digitar
        self.loop = True  # criando um loop inicia no true

# criando a função tela para mostrar os itens na tela
    def tela(self):
        pass

    # Criando a função eventos para gerir os eventos durante o jogo
    def eventos(self):
        for i in pg.event.get():
            if i.type == pg.QUIT:
                self.loop = False

    def update(self): # Criando a função para rodar o jogo
        while self.loop:  # enquanto a variavel loop for verdadeira faça
            self.tela()   # chama a variavel tela a variavel eventos e o display.update
            self.eventos()
            pg.display.update()

