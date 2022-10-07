from dino_runner.utils.constants import HEART

class Heart:
    def __init__(self, widht, heigth):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = widht
        self.rect.y = heigth
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    