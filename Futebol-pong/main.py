#Importando a biblioteca pygame
import pygame as pg # apelidando a biblioteca de pg

# Criando a janela ou a temla do jogo
window = pg.display.set_mode([1280, 720])  #  A TELA DO NOSSO SISTEMA sera de 1280 por 720
title = pg.display.set_caption("Fotball pong")  # Definindo o titulo do jogo

# Definindo uma variavel para manter a tela aberta

loop = True
while loop:
    # Criando  um for para eventos
    for events in pg.event.get():    # Criando um for para cada evento em eventos no pygame faça
        if events.type == pg.QUIT:    # se o tipo de evento for do tipo quit ou seja clicar no x por exemplo
            loop = False   # o loop que determina o while fica false e fecha a tela
    pg.display.update()   # Usado para não fechar a janela do jogo enquanto o loop for true um evento