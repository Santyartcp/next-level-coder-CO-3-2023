import random

import pygame

from dino_runner.components.Power_ups.shield import Shield
from dino_runner.components.Power_ups.hammer import Hammer

class PowerUpManager:
    
    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0

    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generate power up")
                self.when_appears =random.randint(self.when_appears +200, 500 + self.when_appears)
                self.power_ups.append(Shield())
                self.power_ups.append(Hammer())
    
    def update(self, points, game_speed, player, obstacles):
        self.generate_power_ups(points)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if isinstance(power_up, Shield):
                    player.shield = True
                    player.type = power_up.type
                    start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = start_time + (time_random * 1000)
                elif isinstance(power_up, Hammer):
                    power_up.use(player, obstacles)
                self.power_ups.remove(power_up)
        

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
