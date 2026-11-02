from obj import Obj, Pipe, Coin, Bird
import pygame as pg
pg.init()
import random


class Game:
    def __init__(self):
        self.all_sprites = pg.sprite.Group()
        self.bg = Obj("assests/sky.png", 0, 0, self.all_sprites)  
        self.chao = Obj("assests/ground.png", 0, 480,self.all_sprites)

        self.bg2 = Obj("assests/sky.png", 360, 0, self.all_sprites)
        self.chao2 = Obj("assests/ground.png", 360, 480,self.all_sprites)
        
        self.ticks = 0
        self.bird = Bird("assests/bird1.png", 50, 320, self.all_sprites)
        
    def draw(self, window):
            self.all_sprites.draw(window)


    def update(self):
         self.all_sprites.update()
         self.move_bg()
         self.move_chao()
         self.spaw_pipes()

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
              pipe = Pipe("assests/pipe1.png", 360, random.randrange(400,480), self.all_sprites)
              pipe2 = Pipe("assests/pipe2.png",360, random.randrange(-160, -30), self.all_sprites)
              coiny = (pipe.rect.bottom + pipe2.rect.top) / 2
              coin = Coin("assests/0.png", 388, coiny - 24, self.all_sprites)




              