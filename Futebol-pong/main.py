# Importando a biblioteca pygame para desenvolvimento de jogos
import pygame as pg # apelidando a biblioteca pygame de pg

# Criando a janela ou a tela do jogo

window = pg.display.set_mode([1280,720])  # Aqui foi definido o tamanho da tela 1280 largura 720 altura
title = pg.display.set_caption("Fotball pong")

#Colocando a imagem de fundo o campo de futebol
campo = pg.image.load("imagem/campo.png")
window.blit(campo, (0,0))  #Função para pegar a imagem da variavel campo que se inicia na posição 0 em x e 0 em y


# Agora criamos um loop com while para que a tela fique ligada
loop = True # declaramos uma varivel que se incia verdadeira

while loop:  # Enquanto lop for verdadeira faça

    for events in pg.event.get():   # Events uma variavel temporaria para cada evento em todos os eventos do pygame faça
        if events.type == pg.QUIT:   # Se o evento for igual a quit clicar no X por exemplo
            loop = False # Loop recebe false e acaba o loop com while
    pg.display.update()   # Enquanto loop for verdadeira deixe a tela ligado, Cuidado pois com while corremos o riscod e ter um loop infinito