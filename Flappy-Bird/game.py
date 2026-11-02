from obj import Obj, Pipe, Coin, Bird, Text
import pygame as pg
pg.init()
import random


class Game:
    def __init__(self):
        self.all_sprites = pg.sprite.Group()
        self.coin_group = pg.sprite.Group()
        self.pipe_group = pg.sprite.Group()

        self.bg = Obj("assests/sky.png", 0, 0, self.all_sprites)  
        self.chao = Obj("assests/ground.png", 0, 480,self.all_sprites)

        self.bg2 = Obj("assests/sky.png", 360, 0, self.all_sprites)
        self.chao2 = Obj("assests/ground.png", 360, 480,self.all_sprites)
        
        self.ticks = 0
        self.bird = Bird("assests/bird1.png", 50, 320, self.all_sprites)

        self.change_scene = False

        self.score = Text(100, "0")

        self.max_score = 0
        self.check_score()
        self.timer = 0
    def draw(self, window):
            self.all_sprites.draw(window)
            self.score.draw(window, 150, 50)


    def update(self):
         self.all_sprites.update()
         self.move_bg()
         self.move_chao()
         if self.bird.play:
            self.spaw_pipes()
            self.bird.colision_coin(self.coin_group)
            self.bird.colision_pipe(self.pipe_group)
            self.score.text_update(str(self.bird.pts))
            self.all_sprites.update()
         else:
              self.save_score
              self.game_over()
    def move_bg(self):
         self.bg.rect.x -=0.6
         self.bg2.rect.x -= 0.6

         if self.bg.rect.x <= -360:
              self.bg.rect.x = 0 

         if self.bg2.rect.x <= 0:
              self.bg2.rect.x = 360

    def move_chao(self):
         self.chao.rect.x -= 0.6
         self.chao2.rect.x -= 0.6

         if self.chao.rect.x <= -360:
              self.chao.rect.x = 0

         if self.chao2.rect.x <= 0:
              self.chao2.rect.x = 360

    def spaw_pipes(self):
         self.ticks += 1
         
         if self.ticks >= random.randrange(150, 180):
              self.ticks = 0
              pipe = Pipe("assests/pipe1.png", 360, random.randrange(340,400), self.all_sprites, self.pipe_group)
              pipe2 = Pipe("assests/pipe2.png",360, random.randrange(-200, -160), self.all_sprites, self.pipe_group) 

              coiny = (pipe.rect.bottom + pipe2.rect.top) / 2
              coin = Coin("assests/0.png", 388, coiny - 24, self.all_sprites, self.coin_group)

    def game_over(self):
         self.timer += 1
         if self.timer >= 45:
              self.change_scene = True


    def save_score(self):
         if self.bird.pts > self.max_score:
              self.max_score = self.bird.pts
              file = open("save.txt", "w")   # usando w podemos escrever dentro do arquivo

              file.write(str(self.max_score))
              file.close()

    def check_score(self):
         file = open("save.txt", "r")  # usando o r podemos ler o que está no arquivo
         self.max_score = int(file.read())
         file.close()