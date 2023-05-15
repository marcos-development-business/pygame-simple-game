from os import path
from uuid import uuid4
from random import random, randint

import pygame
from pygame import gfxdraw, Surface

from constants import Constants


class Ball:
    def __init__(self, screen: Surface, color: tuple[int, int, int] = Constants.Colors.WHITE):
        __w = max(int(Constants.GAME_WIDTH * 0.05), 20)
        self.color = color
        self.break_point_exceeded = False
        self.screen = screen
        self.gravityY = min(random() / 3, 0.3)
        self.gravityX = min(random() / 3, 0.3) if randint(0, 1) == 1 else -max(random() / 3, 0.3)
        self.ray = randint(20, int(__w - (__w % 10)))
        self.id = str(uuid4())
        self.x = randint(int(self.ray * 2), int(Constants.GAME_WIDTH - (self.ray * 2)))
        self.y = -self.ray

    def render(self):
        gfxdraw.aacircle(self.screen, int(self.x), int(self.y), self.ray, self.color)
        gfxdraw.filled_circle(self.screen, int(self.x), int(self.y), self.ray, self.color)

    def move(self):
        if self.gravityX > 0:
            self.x = (self.x + Constants.GAME_VELOCITY) + self.gravityX
        else:
            self.x = (self.x - Constants.GAME_VELOCITY) + self.gravityX

        self.y = (self.y + Constants.GAME_VELOCITY) + self.gravityY

    def change_x_direction(self):
        if self.x + self.ray >= Constants.GAME_WIDTH or self.x - self.ray <= 0:
            ball_change_direction_sound = pygame.mixer.Sound(path.join('assets/sounds/ball_change_direction.wav'))
            ball_change_direction_sound.play(0)
            self.gravityX = -self.gravityX

    def handle_with_color_update(self, new_color: tuple[int, int, int]):
        if self.y + self.ray > Constants.BREAKPOINT > self.y - self.ray:
            self.color = Constants.Colors.YELLOW
        elif self.y - self.ray > Constants.BREAKPOINT:
            self.color = new_color

    def check_if_y_exceed_breakpoint(self):
        check = self.y + self.ray >= Constants.BREAKPOINT and not self.break_point_exceeded

        if check:
            self.break_point_exceeded = True

        return check

    def check_if_y_exceed_height(self):
        return self.y >= Constants.GAME_HEIGHT + (self.ray * 2)

    def check_if_click_is_inside(self, click_x: int, click_y: int):
        equation = (click_x - self.x) ** 2 + (click_y - self.y) ** 2

        return equation <= self.ray ** 2 and self.y + self.ray
