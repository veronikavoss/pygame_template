from setting import *

class SurfaceSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((30,40))
        self.image.fill('blue')
        self.rect=self.image.get_rect()
    
    def move(self):
        pass
    
    def update(self):
        pass