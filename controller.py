from setting import *
from sprite_class import *

class Controller:
    def __init__(self,screen):
        self.screen=screen
        
        self.surface_sprite=SurfaceSprite()
        self.surface_sprite_group=pygame.sprite.GroupSingle(self.surface_sprite)
    
    def update(self):
        self.surface_sprite.update()
    
    def draw(self):
        self.screen.fill('white')
        self.surface_sprite_group.draw(self.screen)