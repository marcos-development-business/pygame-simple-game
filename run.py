import pygame
import sys

from pygame import gfxdraw

from constants import Constants
from objects.Score import Score
from objects.ball import Ball
from objects.ballsList import BallsList
from objects.particles import Particles

pygame.init()

pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)


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
        score = Score()

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
                            self.balls.remove_ball(ball.id)
                            particles.create(ball.x, ball.y)
                            score.increment()

            for ball in balls:
                if ball.check_if_y_exceed_height():
                    self.balls.remove_ball(ball.id)
                    score.decrement()
                else:
                    if ball.check_if_y_exceed_breakpoint():
                        self.create_new_ball()

                    ball.change_x_direction()
                    ball.move()
                    ball.handle_with_color_update(Constants.Colors.GREEN)
                    ball.render()

            gfxdraw.hline(self.screen, 0, int(Constants.GAME_WIDTH), int(Constants.BREAKPOINT), Constants.Colors.WHITE)

            particles.render()

            score_text = font.render(f' SCORE: {score} ', True, Constants.Colors.WHITE, Constants.Colors.SMOOTH_BLACK)

            text_width = score_text.get_width() + score_text.get_width() * 2
            rect_center = int(Constants.GAME_WIDTH / 2 - text_width / 2)
            text_center = (int(Constants.GAME_WIDTH / 2 - score_text.get_width() / 2), int(score_text.get_height() / 2) + 15 // 4)

            pygame.draw.rect(
                self.screen, Constants.Colors.SMOOTH_BLACK,
                border_bottom_left_radius=20, border_bottom_right_radius=20,
                rect=(rect_center, 0, score_text.get_width() + score_text.get_width() * 2, 30)
            )

            self.screen.blit(score_text, (text_center[0], text_center[1]))

            pygame.display.update()

            self.screen.fill(Constants.Colors.BLACK)


if __name__ == '__main__':
    game = Game()
    game.loop()
