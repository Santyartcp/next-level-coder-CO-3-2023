import random

import pygame

from dino_runner.components.Power_ups.shield import Shield

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

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)