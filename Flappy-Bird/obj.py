# importando a biblioteca pygame
import pygame as pg

class Obj(pg.sprite.Sprite):
    def __init__ (self, imagem, x, y, *groups):  # Agora a classe obj herda de pg.sprite.Sprite
        super().__init__(*groups)

        self.image = pg.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Pipe(Obj):
    def __init__(self, imagem, x, y , *groups):
        super(). __init__(imagem, x, y, *groups)

    def update(self, *args):
            self.move()

    def move(self):
        self.rect.x -= 0.6
        if self.rect.x <=-100:
             self.kill()

class Coin(Obj):
    def __init__(self, imagem, x, y, *groups):
          super().__init__(imagem, x, y, *groups)

          self.ticks = 0
          self.contador = 0
    
    def update(self, *args):
     self.move()
     self.anim()

    def move(self):
        self.rect.x -= 1
        if self.rect.x <=-100:
             self.kill()

    def anim(self):
        self.contador += 1
        if self.contador >= 5:
           self.contador = 0
           self.ticks = (self.ticks + 1) % 6
           self.image = pg.image.load("assests/" + str(self.ticks) + ".png")


class Bird(Obj):
    def __init__(self, imagem, x, y, *groups):
        super().__init__(imagem, x, y, *groups)
        self.ticks = 0
        self.contador = 0

        self.vel = 0
        self.grav = 0.15

    def update(self, *args):
            self.anim()
            self.move()
        
    def anim(self):
            self.contador += 1
            if self.contador >= 8:
               self.contador = 0
               self.ticks = (self.ticks + 1) % 4
               self.image = pg.image.load("assests/bird" + str(self.ticks) + ".png")


    def move(self):
        key = pg.key.get_pressed()

        self.vel += self.grav
        self.rect.y += self.vel
        if self.vel >= 2.35:
             self.vel = 2.35
        
        if key[pg.K_SPACE]:
              self.vel -= 0.25
        if self.vel <= -2.55:
             self.vel = -2.55
        if self.rect.y >=440:
             self.rect.y = 440
        elif self.rect.y <= 0:
             self.rect.y = 0
             self.vel = 4