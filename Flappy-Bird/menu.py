from obj import Obj
import pygame as pg 
pg.init()

class Menu(Obj):
    def __init__(self):
        self.all_sprites = pg.sprite.Group()
        self.bg = Obj("assests/sky.png", 0, 0, self.all_sprites)  
        self.chao = Obj("assests/ground.png", 0, 480,self.all_sprites)
         
        self.bg2 = Obj("assests/sky.png", 360, 0, self.all_sprites)
        self.chao2 = Obj("assests/ground.png", 360, 480,self.all_sprites)
                    
        self.get_ready = Obj("assests/getready.png", 50, 150, self.all_sprites)
        self.table_score = Obj("assests/score.png", 21, 250, self.all_sprites)
        self.button_go = Obj("assests/go.png", 100, 500, self.all_sprites)
        self.change_scene =  False






   
    def draw(self, window):
        self.all_sprites.draw(window)
        self.move_chao()
        self.move_bg()

    def update(self):
        self.all_sprites



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

    def events(self, event):
         if event.type == pg.MOUSEBUTTONUP:
              if self.button_go.rect.collidepoint(pg.mouse.get_pos()):
                   self.change_scene = True
         if event.type == pg.KEYDOWN:
              if event.key == pg.K_SPACE:
                 self.change_scene = True