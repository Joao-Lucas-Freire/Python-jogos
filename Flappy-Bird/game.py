from obj import Obj, Pipe
import pygame as pg
pg.init()

class Game:
    def __init__(self):
        self.all_sprites = pg.sprite.Group()
        self.bg = Obj("assests/sky.png", 0, 0, self.all_sprites)  
        self.chao = Obj("assests/ground.png", 0, 480,self.all_sprites)

        self.bg2 = Obj("assests/sky.png", 360, 0, self.all_sprites)
        self.chao2 = Obj("assests/ground.png", 360, 480,self.all_sprites)
        
        self.ticks = 0

        
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

         if self.ticks >= 120:
              self.ticks = 0
              pipe = Pipe("assests/pipe1.png", 360, 400, self.all_sprites)
              pipe2 = Pipe("assests/pipe2.png",360, - 30, self.all_sprites)
              