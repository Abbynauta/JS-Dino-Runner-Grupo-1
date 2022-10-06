from .obstacle import Obstacle 
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD = {
        "UP":(BIRD,260),
        "DOWN":(BIRD,310),
    }
    
    def __init__(self, bird_type):
        images, bird_pos = self.BIRD[bird_type]
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = bird_pos
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)
        self.index += 1