# importando a biblioteca pygame
import pygame as pg
# Criando a classe obj cada imagem do jogo será um objeto dessa classe
class Obj():
    def __init__(self, imagem, x,y): # Aqui recebemos o caminho da imagem a posição eixo x e eixo y
        # Sprite é um objeto fornecido pelo pygame para representar os elementos do jogo
        self.group = pg.sprite.Group() # dessa maneira criamos um grupo vazio de sprits
        self.sprite = pg.sprite.Sprite(self.group)         # cada sprite será armazenado em um grupo
        self.sprite.image = pg.image.load(imagem) # aqui pegamos o parametro imagem transformamos numa imagem no pg e colocamos no atributo imgae       
        
        self.sprite.rect  = self.sprite.image.get_rect() # get_rect cria um retangulo de acordo com a altura e largura do objeto ficando mais facil para o pg usar ele    
        # porém o retangulo se inicia na posição 0,0 nos 2 eixo        
        self.sprite.rect.x = x # aqui pegamos o parametro passando na criação do objeto e colocamos no rentagulo criado para o obj então essa é a posição dele no eixo x
       
        self.sprite.rect.y = y # mesma coisa aqui agora o obj sai do 0,0 e fica de acordo com sua posição quando foi criado 
    # criando a função para mostrar na tela

        self.frame = 1

        self.tick = 0
    def mostrar(self, window): # window é a janela ou a tela onde o objeto vai ser mostrado
        self.group.draw(window)


# Toda vez que o self.frame mudar ele mostra uma aranha diferente
    def anim(self, image, tick, frame):
        self.tick +=1
        if self.tick == tick:
           self.tick = 0

           self.frame += 1
        if self.frame == frame:
            self.frame = 1
            
        self.sprite.image = pg.image.load("imagem/" + image + str(self.frame) + ".png")

        