import random
import pygame

from dino_runner.utils.constants import BIRD
from .bird import Bird
from .cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game_speed, player, on_death):
        
        if len(self.obstacles) == 0:
            cactus_type = "SMALL" if random.randint(0,1) == 0 else "LARGE"
            self.obstacles.append(Cactus(cactus_type))
            if random.randint(0,1) == 1:
               self.obstacles.append(Bird(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                on_death()
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []