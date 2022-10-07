import random
import pygame

from dino_runner.components.obstacles.obstaclesSLB import BirdDown, BirdUp, LargeCactus, SmallCactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(BirdUp(BIRD))
            else:
                self.obstacles.append(BirdDown(BIRD))
                
            #bird_type = "UP" if random.randint(0,1) == 0 else "DOWN"
            #self.obstacles.append(Bird(bird_type))
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                if on_death():
                    self.obstacles.remove(obstacle)
                else:
                    break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []