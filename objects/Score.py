import pygame
from pygame import Surface
from constants import Constants


pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)


class Score:
    __score = 0
    
    def __init__(self, screen: Surface):
        self.screen = screen

    def __str__(self):
        return str(self.__score).rjust(3, '0')

    def increment(self, to=1):
        self.__score += to

    def decrement(self, by=1):
        if self.__score > 0:
            self.__score -= by

    def reset(self):
        self.__score = 0

    def lose(self, total=10):
        if self.__score > total:
            self.decrement(total)
        else:
            self.reset()

    def get_score(self):
        return self.__score

    def render(self):
        score_text = font.render(f' SCORE: {self} ', True, Constants.Colors.WHITE, Constants.Colors.SMOOTH_BLACK)

        text_width = score_text.get_width() + score_text.get_width() * 2
        rect_center = int(Constants.GAME_WIDTH / 2 - text_width / 2)
        text_center = (int(Constants.GAME_WIDTH / 2 - score_text.get_width() / 2), int(score_text.get_height() / 2) + 15 // 4)

        pygame.draw.rect(
            self.screen,
            Constants.Colors.SMOOTH_BLACK,
            border_bottom_left_radius=20,
            border_bottom_right_radius=20,
            rect=(rect_center, 0, score_text.get_width() + score_text.get_width() * 2, 30)
        )

        self.screen.blit(score_text, (text_center[0], text_center[1]))

