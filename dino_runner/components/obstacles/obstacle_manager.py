from random import random
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from .cactus import SmallCactus, LargeCactus
from .bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(SmallCactus(SMALL_CACTUS))
            if len(self.obstacles)== 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
                if len(self.obstacles) == 2:
                    self.obstacles.append(Bird(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)