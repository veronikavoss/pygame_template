from setting import *

class SurfaceSprite(pygame.sprite.Sprite):
    def __init__(self,topleft,load=False):
        super().__init__()
        self.image=pygame.Surface((30,40))
        self.image.fill('blue')
        self.rect=self.image.get_rect(topleft=topleft)
        self.direction=pygame.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=5
        self.load=load
    
    def set_key_input(self):
        if self.load:
            key_input=pygame.key.get_pressed()
            if key_input[pygame.K_LEFT]:
                self.dx=-self.speed
            elif key_input[pygame.K_RIGHT]:
                self.dx=self.speed
            else:
                self.dx=0
    
    def move(self):
        self.rect.x+=self.dx
    
    def update(self):
        self.set_key_input()
        self.move()
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)