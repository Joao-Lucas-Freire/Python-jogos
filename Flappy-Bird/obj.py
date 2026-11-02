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

        



