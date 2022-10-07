import random
from .obstacle import Obstacle

class SmallCactus(Obstacle):
    def __init__(self,images):
        type = random.randint(0,2)
        super().__init__(images, type)
        self.rect.y = 325
        
class LargeCactus(Obstacle):
       def __init__(self,images):
        type = random.randint(0,2)
        super().__init__(images, type)
        self.rect.y = 300
        
class BirdUp(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 260
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)
        self.index += 1
        
class BirdDown(Obstacle):
       def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 310
        self.index = 0
        
       def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)
        self.index += 1
    