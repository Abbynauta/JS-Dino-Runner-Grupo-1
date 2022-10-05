import random
from .obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        type = random.randint(0,1)
        super().__init__(images, type)
        self.rect.y = 15
        self.index=0
        
    def draw(self, screen):
        if self.index >= 9:
            self.indexç = 0
        screen.blit(self.images[self.index//5], self.rect)
        
    