# importando a biblioteca pygame
import pygame as pg
pg.init()
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

class Heroi(Obj):
    def __init__(self, imagem, x, y):
        super().__init__(imagem, x, y)
        # vida e pontos ficam no __init__ para serem criados só uma vez
        self.life = 3
        self.pts = 0

    def move_heroi(self, event):
        if event.type == pg.MOUSEMOTION:
            self.sprite.rect.x = pg.mouse.get_pos()[0] - 35
            self.sprite.rect.y = pg.mouse.get_pos()[1] - 30
        
    def colisao(self, group, name):
        name = name
        colison = pg.sprite.spritecollide(self.sprite, group, True)

        if name == "florwer" and colison:
            print("colidiu com a flor")
            self.pts += 1
        elif name  == "spider" and colison:
            print("colidiu com a aranha")
            self.life -= 1


# Criando obj para criar um texto na tela
class Text():
    def __init__(self, size, text):
        self.font = pg.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, True, (0,0,0))


    def mostrar(self, window,x,y):
        window.blit(self.render, (x,y))

    def update_text (self, text):
        self.render = self.font.render(text, True, (0,0,0))