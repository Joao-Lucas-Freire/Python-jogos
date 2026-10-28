# Importando a biblioteca pygame para desenvolvimento de jogos
import pygame as pg # apelidando a biblioteca pygame de pg

# Criando a janela ou a tela do jogo

window = pg.display.set_mode([1280,720])  # Aqui foi definido o tamanho da tela 1280 largura 720 altura
title = pg.display.set_caption("Fotball pong")

#Criando as imagens do jogo campo - p1 - p2 - ball
campo = pg.image.load("imagem/campo.png")

player1 = pg.image.load("imagem/player1.png")   # vai criar uma imagem no pygame carregada da minha maquina

player2 = pg.image.load("imagem/player2.png")

bola = pg.image.load("imagem/ball.png")

#Criando variaveis que contem a posição da bolinha
bola_x = 618
bola_y = 332   # Duas variaveis que representam a posição da bolinha


# Criando uma função que vai conter os itens do jogo
def itens():
    window.blit(campo, (0,0))  
    window.blit(player1,(48,280))
    window.blit(player2, (1154,280))
    window.blit(bola,(bola_x,bola_y))

# Criando uma função para mover a bolinha
def move_bola():
    global bola_x
    global bola_y      # Global serve para acessar e modificar uma variavel de escopo global dentro de uma função
    bola_x += 1



# Agora criamos um loop com while para que a tela fique ligada
loop = True # declaramos uma varivel que se incia verdadeira

while loop:  # Enquanto lop for verdadeira faça

    for events in pg.event.get():   # Events uma variavel temporaria para cada evento em todos os eventos do pygame faça
        if events.type == pg.QUIT:   # Se o evento for igual a quit clicar no X por exemplo
            loop = False # Loop recebe false e acaba o loop com while
    pg.display.update()   # Enquanto loop for verdadeira deixe a tela ligado, Cuidado pois com while corremos o riscod e ter um loop infinito

    itens()   # Chamando as imagens na tela
    move_bola()   # Adicionando o função para mover a bola







