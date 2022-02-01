from setting import *
from controller import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        self.clock=pygame.time.Clock()
        self.start_screen=True
        self.running=True
        self.start()
    
    def start(self):
        self.controller=Controller(self.screen)
        self.loop()
    
    def loop(self):
        while self.running:
            self.dt=self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.running:
                    self.running=False
                    break
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.controller.draw()

Game()
pygame.quit()