# Importando a biblioteca pygame para desenvolvimento de jogos
import pygame as pg # apelidando a biblioteca pygame de pg

# Criando a janela ou a tela do jogo
pg.init()
window = pg.display.set_mode([1280,720])  # Aqui foi definido o tamanho da tela 1280 largura 720 altura
title = pg.display.set_caption("Fotball pong")

#Criando as imagens do jogo campo - p1 - p2 - ball
campo = pg.image.load("imagem/campo.png")

player1 = pg.image.load("imagem/player1.png")   # vai criar uma imagem no pygame carregada da minha maquina
player1_y = 280
player1_moveup = False
player1_movedown = False


# Player 2
player2 = pg.image.load("imagem/player2.png")
player2_y = 280
player2_moveup = False
player2_movedown = False   # dos 2 player se inicia false pois se inicia parado


bola = pg.image.load("imagem/ball.png")

#Criando variaveis que contem a posição da bolinha
bola_x = 618
bola_y = 332   # Duas variaveis que representam a posição da bolinha
bola_dir = -0.7   # Varivel que indica a movimentação da bola
bola_dir_y = 1  # Criando a movimentação da bola no sentido vertical
# Criando uma função que vai conter os itens do jogo

# Criando as variavel de pontuação
score1 = 0
score2 = 0
score1_img = pg.image.load("imagem/pontuacao/0.png")
score2_img = pg.image.load("imagem/pontuacao/0.png")




def itens():
    window.blit(campo, (0,0))  
    window.blit(player1,(48,player1_y))
    window.blit(player2, (1154,player2_y))
    window.blit(bola,(bola_x,bola_y))
    window.blit(score1_img, (500,50))
    window.blit(score2_img, (720,50))
# Criando uma função para mover a bolinha
def move_bola():
    global bola_x
    global bola_y      # Global serve para acessar e modificar uma variavel de escopo global dentro de uma função
    global bola_dir
    global bola_dir_y
    global score1
    global score2
    global score1_img
    global score2_img


    bola_x += bola_dir
    bola_y += bola_dir_y   # Aqui adicionamos a movimentação da bola no eixo y
    if bola_x < 122.49:   # Aqui é o ponto de colisão com posição do meu boneco
       if player1_y < bola_y + 23:  # metade do tamanho da bola 23
            if player1_y + 146 > bola_y:   # tamanho da imagem do jogador 146
                bola_dir *= -1  # volta para o outro lado

    if bola_x > 1114:   # Aqui é o ponto de colisão com posição do meu boneco
           if player2_y < bola_y + 23:  # metade do tamanho da bola 23
                if player2_y + 146 > bola_y:   # tamanho da imagem do jogador 146
                    bola_dir *= -1  # volta para o outro lado
    # Criando o limite superior
    if bola_y <=2:
        bola_dir_y *= -1
    elif bola_y >= 662:     # Adicionamos os limites para o bolinha
        bola_dir_y *= -1


    # Quando a bola passa pro do limite player 1
    if bola_x <= -50:
         bola_x = 618
         bola_y = 332
         bola_dir_y *= -1
         bola_dir *= -1
         score2 += 1
         score2_img = pg.image.load("imagem/pontuacao/" + str(score2) + ".png")  # Concatenamos o score com png para ir adicionando e trocando conforme acontece a pontuação
    elif bola_x > 1320:
         bola_x = 618
         bola_y = 332
         bola_dir *= -1
         bola_dir_y *= -1
         score1 += 1
         score1_img = pg.image.load("imagem/pontuacao/" + str(score1) + ".png")

    # Criandoa s verificações para colisão com player 1


# Criando uma variavel para mover o player 1
def move_player1():
    global player1_y
    if player1_moveup:
        player1_y -= 1.2 # Se o move up que seria ir para cima do player 1 for verdadeira tira - 10 que seria movar para cim
    else:
        player1_y += 0 # se não for continua parado

    if player1_movedown:
        player1_y += 1.2 # se o move down que seria ir para baixo for verdadeiro adicione 10 
    else:
        player1_y += 0
    # Adicionando limites para o p1
    if player1_y <= 22 :
       player1_y = 22 # esse é o limite da minha tela na parte superior, dessa maneira não passa
    elif player1_y >= 542.79:
        player1_y = 542.79  # esse é o limite da parte inferior dessa maneira não passa
    
    #print(player1_y)  print usado para ver os limites

#def move_player2():
  #  global player2_y
   # global bola_y
   # player2_y = bola_y    # Criando aqui por hora para conseguir testar o jogo


# Agora criamos um loop com while para que a tela fique ligada
loop = True # declaramos uma varivel que se incia verdadeira

while loop:  # Enquanto lop for verdadeira faça

    for events in pg.event.get():   # Events uma variavel temporaria para cada evento em todos os eventos do pygame faça
        if events.type == pg.QUIT:   # Se o evento for igual a quit clicar no X por exemplo
            loop = False # Loop recebe false e acaba o loop com while
        if events.type == pg.KEYDOWN:   # verifica se o tipo de evento é do tipo keydown seria tipo teclado
            if events.key == pg.K_w:    # verifica qual key ou qual tecla foi apertado
                player1_moveup = True            # se foi a tecla w tira o jogador move para cima
            if events.key == pg.K_s:
                player1_movedown = True # se a tecla pressionada for igual S o jogador move para baixo
        if events.type == pg.KEYUP:
            if events.key == pg.K_w:  
                 player1_moveup =False         
            if events.key == pg.K_s:
                player1_movedown = False
        
        # Agora criando a movimentação do player 2



    itens()   # Chamando as imagens na tela
    move_bola()   # Adicionando o função para mover a bola
    move_player1()   # Função de movimentação para o player 1
    #move_player2()
    pg.display.update()   # Enquanto loop for verdadeira deixe a tela ligado, Cuidado pois com while corremos o riscod e ter um loop infinito







