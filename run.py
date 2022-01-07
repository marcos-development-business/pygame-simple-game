import time

import pygame
import sys

from pygame import gfxdraw

from constants import Constants
from objects.Score import Score
from objects.ball import Ball
from objects.ballsList import BallsList
from objects.particles import Particles


pygame.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(Constants.SIZE)
        self.balls = BallsList()
        self.running = True
        self.score = Score(self.screen)
        self.particles = Particles(self.screen)

        start_game_sound = pygame.mixer.Sound('assets/sounds/start_game.wav')
        start_game_sound.play(0)

        self.create_new_ball()

    def quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def create_new_ball(self):
        ball = Ball(self.screen)
        self.balls.add_ball(ball)

    def loop(self):
        while self.running:
            balls = self.balls.get_balls()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click_pos = pygame.mouse.get_pos()
                    for ball in balls:
                        if ball.check_if_click_is_inside(mouse_click_pos[0], mouse_click_pos[1]) and mouse_click_pos[1] > Constants.BREAKPOINT:
                            if (self.score.get_score() + 1) % 10 == 0:
                                ten_more_point = pygame.mixer.Sound('assets/sounds/10_more_point.wav')
                                ten_more_point.play(0, 1500)
                            else:
                                get_ball_sound = pygame.mixer.Sound('assets/sounds/get_ball.wav')
                                get_ball_sound.play(0, 2000)
                            self.balls.remove_ball(ball.id)
                            self.particles.create(ball.x, ball.y)
                            self.score.increment()

            for ball in balls:
                if ball.check_if_y_exceed_height():
                    self.balls.remove_ball(ball.id)
                    self.score.decrement()
                else:
                    if ball.check_if_y_exceed_breakpoint():
                        self.create_new_ball()

                    ball.change_x_direction()
                    ball.move()
                    ball.handle_with_color_update(Constants.Colors.GREEN)
                    ball.render()

            gfxdraw.hline(self.screen, 0, int(Constants.GAME_WIDTH), int(Constants.BREAKPOINT), Constants.Colors.WHITE)

            self.particles.render()

            self.score.render()

            pygame.display.update()

            self.screen.fill(Constants.Colors.BLACK)


if __name__ == '__main__':
    game = Game()
    game.loop()
