# importando a biblioteca pygame
import pygame as pg
# Criando a classe obj cada imagem do jogo será um objeto dessa classe
class Obj():
    def __init__(self, imagem, x,y): # Aqui recebemos o caminho da imagem a posição eixo x e eixo y
        self.image = pg.image.load(imagem) # aqui pegamos o parametro imagem transformamos numa imagem no pg e colocamos no atributo imgae
        self.rect  = self.image.get_rect() # get_rect cria um retangulo de acordo com a altura e largura do objeto ficando mais facil para o pg usar ele
        # porém o retangulo se inicia na posição 0,0 nos 2 eixo
        self.rect.x = x # aqui pegamos o parametro passando na criação do objeto e colocamos no rentagulo criado para o obj então essa é a posição dele no eixo x
        self.rect.y = y # mesma coisa aqui agora o obj sai do 0,0 e fica de acordo com sua posição quando foi criado 

    # criando a função para mostrar na tela
    def mostrar(self, window): # window é a janela ou a tela onde o objeto vai ser mostrado
        window.blit(self.image, self.rect) # o blit serve para dizer para mostrar a imagem dentro da window ou da tela é um parametro nescessario toda vez que formos usar essa função