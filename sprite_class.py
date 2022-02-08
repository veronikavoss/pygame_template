from setting import *

class SurfaceSprite(pygame.sprite.Sprite):
    def __init__(self,center):
        super().__init__()
        self.image=pygame.image.load(os.path.join(IMAGE_PATH,'General Sprites.png')).convert_alpha()
        self.image=pygame.transform.scale(self.image,(32*4,32*4))
        self.image.set_colorkey((147,187,236))
        self.rect=self.image.get_rect(center=center)
        self.direction=pygame.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=1
        self.angle=0
    
    def set_rect(self,topleft):
        self.rect=self.image.get_rect(topleft=topleft)
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.angle-=self.speed
        elif key_input[pygame.K_RIGHT]:
            self.angle+=self.speed
        else:
            self.speed=0
    
    def move(self):
        # self.rect.x+=self.dx
        self.angle+=self.speed
        self.image=pygame.transform.rotate(self.image,self.angle)
    
    def update(self):
        self.set_key_input()
        self.move()
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)