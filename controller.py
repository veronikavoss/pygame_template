from setting import *
from sprite_class import *

class Controller:
    def __init__(self,screen):
        self.screen=screen
        
        self.surface_sprite1=SurfaceSprite((0,0))
        self.surface_sprite2=SurfaceSprite((SCREEN_WIDTH-30,0))
        self.surface_sprite_group=pygame.sprite.Group(self.surface_sprite1,self.surface_sprite2)
    
    def collision(self):
        self.collide_sprite=pygame.sprite.spritecollideany(self.surface_sprite1,self.surface_sprite_group)
        print(self.collide_sprite)
    
    def update(self):
        self.surface_sprite_group.update()
        self.collision()
    
    def draw(self):
        self.screen.fill('white')
        self.surface_sprite_group.draw(self.screen)