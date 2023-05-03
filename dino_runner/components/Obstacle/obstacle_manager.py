import pygame
import random
from dino_runner.components.Obstacle.cactus import Cactus
from dino_runner.components.Obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
    
    def update (self, game_speed, game):

        if len(self.obstacles) == 0:
            type = random.randint(0,2)

    
            if type == 0:
             self.obstacles.append(Bird(BIRD))

            elif type == 1:
             self.obstacles.append(Cactus(SMALL_CACTUS))

            elif type == 2:
             self.obstacles.append(Cactus(LARGE_CACTUS))
               
    

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
               pygame.time.delay(300)
               game.playing = False
               break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw (screen)


