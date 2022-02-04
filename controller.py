from setting import *
from sprite_class import *

class Controller:
    def __init__(self,screen):
        self.screen=screen
        
        self.surface_sprite1=SurfaceSprite((0,0),True)
        self.surface_sprite2=SurfaceSprite((SCREEN_WIDTH-30,0))
        self.surface_sprite_groupsingle=pygame.sprite.GroupSingle(self.surface_sprite1)
        self.surface_sprite_group=pygame.sprite.Group(self.surface_sprite2)
    
    def collision(self):
        self.collide_sprite=pygame.sprite.spritecollideany(self.surface_sprite1,self.surface_sprite_group)
        print(self.surface_sprite_group,self.surface_sprite1.rect)
        for i in self.surface_sprite_group:
            if pygame.sprite.collide_mask(i,self.surface_sprite_groupsingle.sprite):
                print('c')
                self.surface_sprite_group.add(self.surface_sprite_groupsingle.sprite)
    
    def update(self):
        self.surface_sprite_group.update()
        self.surface_sprite_groupsingle.update()
        self.collision()
    
    def draw(self):
        self.screen.fill('white')
        self.surface_sprite_group.draw(self.screen)
        self.surface_sprite_groupsingle.draw(self.screen)