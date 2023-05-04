import random
import pygame
from dino_runner.components.Power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH


class Hammer(PowerUp):
    def __init__(self, pos_x, pos_y):
        self.type = random.randint(0, 2)
        self.pos_x = pos_x
        self.pos_y = pos_y
        super().__init__(HAMMER, "type")
        self.active = False
        self.timer = 0

    def use(self, player, obstacles):
        if not self.active:
            self.active = True
            self.timer = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.timer >= 5000:
            self.active = False
            player.has_hammer = False

        for obstacle in obstacles:
            if obstacle.rect.colliderect(player.dino_rect):
                obstacles.pop(obstacles.index(obstacle))


    def create_hammer(obstacles):
        x = SCREEN_WIDTH + random.randint(800, 1000)
        y = 400 - HAMMER.get_height() - 5
        if len(obstacles) > 0 and x > obstacles[-1].rect.x + obstacles[-1].rect.width:
            hammer = Hammer(x, y)
            return hammer
        return None





