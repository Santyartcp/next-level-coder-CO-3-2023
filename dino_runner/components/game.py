import pygame

from dino_runner.utils.constants import (BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_ARIAL)

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.Obstacle.obstacle_manager import  ObstacleManager

from dino_runner.components.Power_ups.power_up_manager import PowerUpManager

from dino_runner.components.player_hearts.heart_manager import HeartManager

from dino_runner.components.Power_ups.hammer import Hammer

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = HeartManager()
        self.points = 0
        self.hammer = Hammer()
        self.obstacle_manager = ObstacleManager(self.hammer)
        self.hammer_mode = False
        self.hammer_key_pressed = False
        self.background_color = (255, 255, 255)
        self.game_over_font = pygame.font.Font(FONT_ARIAL, 60)
        self.game_over_surface = self.game_over_font.render('Game Over', True, (255, 0, 255))
        self.game_over_rect = self.game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        
        


    def increase_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        if self.points >= 200 and self.points < 500:
            self.background_color = (255, 255, 0)
        elif self.points >= 500:
            self.background_color = (0, 0, 0)  

        self.player.check_invincibility()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.hammer_key_pressed = True

                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.hammer_key_pressed = False

            if self.hammer_key_pressed:
                self.hammer_mode = True
                self.obstacle_manager.check_hammer_collision()

            user_input = pygame.key.get_pressed()
            self.update(user_input)
            self.draw()

            if not self.game_over:
                user_input = pygame.key.get_pressed()
                self.update(user_input)
                self.draw()
                self.check_game_over()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hammer_key_pressed = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.hammer_key_pressed = False

    def update(self, user_input): 
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self, user_input)
        self.power_up_manager.update(self.points, self.game_speed, self.player,
                                    self.obstacle_manager.obstacles)
        self.increase_score()

        if self.heart_manager.heart_count == 0:
            self.game_over()

        
    

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(self.background_color)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        surface = font.render(str(self.points), True, (0,0,0))
        rect = surface.get_rect()
        rect.x = 1000
        rect.y = 10
        self.screen.blit(surface, rect)

    
    def game_over(self):
        self.playing = False
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.game_over_surface, self.game_over_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()


    