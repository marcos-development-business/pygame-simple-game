import pygame
import sys

from pygame import gfxdraw

from constants import Constants
from objects.ball import Ball
from objects.ballsList import BallsList
from objects.particles import Particles

pygame.init()


class Game:
    screen = pygame.display.set_mode(Constants.SIZE)
    balls = BallsList()
    running = True

    def quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def create_new_ball(self):
        ball = Ball(self.screen)
        self.balls.add_ball(ball)

    def loop(self):
        self.create_new_ball()
        particles = Particles(self.screen)

        while self.running:
            balls = self.balls.get_balls()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click_pos = pygame.mouse.get_pos()
                    for ball in balls:
                        if ball.check_if_click_is_inside(mouse_click_pos[0], mouse_click_pos[1]) and ball.y + ball.ray > Constants.BREAKPOINT:
                            self.balls.remove_ball(ball.id)
                            particles.create(ball.x, ball.y)

            for ball in balls:
                if ball.check_if_y_exceed_height():
                    self.balls.remove_ball(ball.id)
                else:
                    if ball.check_if_y_exceed_breakpoint():
                        self.create_new_ball()

                    ball.change_x_direction()
                    ball.move()
                    ball.handle_with_color_update(Constants.Colors.GREEN)
                    ball.render()

            gfxdraw.hline(self.screen, 0, int(Constants.GAME_WIDTH), int(Constants.BREAKPOINT), Constants.Colors.WHITE)

            particles.render()

            pygame.display.update()

            self.screen.fill(Constants.Colors.BLACK)


if __name__ == '__main__':
    game = Game()
    game.loop()
