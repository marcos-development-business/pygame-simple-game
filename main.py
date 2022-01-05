import uuid

import pygame
from pygame import gfxdraw
import sys
from random import random, randint

pygame.init()

dimensions = pygame.display.Info()

w_W = dimensions.current_w
w_H = dimensions.current_h
H_09 = w_H * 0.9
W_SIZE = (min(w_W * 0.9, 600), H_09 - (H_09 % 10))
BREAKPOINT = int(W_SIZE[1] / 2) - int(W_SIZE[1] * 0.1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 0, 255)
COLORS = [RED, GREEN, WHITE, YELLOW]
MAX_DISTANCE_TO_PARTICLES = 300

list_of_elements = []
list_of_particles = []

screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption("Game")


def create_cube():
    w = max(int(w_W * 0.02), 10)
    s = randint(10, w - (w % 10))
    element = {
        'g': max(random() / 1.5, 0.4),
        's': s,
        'id': str(uuid.uuid4()),
        'y': -s,
        'x': randint(s * 2, int(W_SIZE[0]) - (s * 2)),
        'c': True,
        'color': WHITE,
    }

    list_of_elements.append(element)


def create_particles(_x: int, _y: int):
    for _ in range(25):
        _g = (-random() if randint(0, 1) else random())
        _g2 = (-random() if randint(0, 1) else random()) / 1.1
        list_of_particles.append([_x, _y, COLORS[randint(0, len(COLORS) - 1)], _g, _g2, str(uuid.uuid4()), _x, _y])


def game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for element in list_of_elements:
                if (element['x'] - element['s'] * 2 <= mouse[0] <= element['x'] + element['s'] * 2 and
                        element['y'] + element['s'] * 2 >= mouse[1] >= element['y'] - element['s'] * 2 >= BREAKPOINT):
                    create_particles(mouse[0], mouse[1])
                    list_of_elements.remove(element)

    for element in list_of_elements:
        element['y'] = element['y'] + element['g']
        color = WHITE

        if element['y'] - (element['s'] * 2) > BREAKPOINT:
            color = GREEN
        gfxdraw.aacircle(screen, int(element['x']), int(element['y']), element['s'] * 2, color)
        gfxdraw.filled_circle(screen, int(element['x']), int(element['y']), element['s'] * 2, color)

        b_1 = element['y'] + element['s']

        if element['y'] >= W_SIZE[1] + element['s'] * 2:
            list_of_elements.remove(element)
        elif b_1 - (b_1 % 10) == BREAKPOINT - (BREAKPOINT % 10) and element['c']:
            element['c'] = False
            create_cube()

    for particle in list_of_particles:
        particle[1] = particle[1] + particle[4]
        particle[0] = particle[0] + particle[3]
        gfxdraw.aacircle(screen, int(particle[0]), int(particle[1]), 5, particle[2])
        gfxdraw.filled_circle(screen, int(particle[0]), int(particle[1]), 5, particle[2])

        if (particle[0] >= particle[6] + MAX_DISTANCE_TO_PARTICLES or
                particle[0] <= particle[6] - MAX_DISTANCE_TO_PARTICLES or
                particle[1] >= particle[7] + MAX_DISTANCE_TO_PARTICLES or
                particle[1] <= particle[7] - MAX_DISTANCE_TO_PARTICLES or
                particle[0] >= W_SIZE[0] or particle[1] >= W_SIZE[1] or
                particle[0] <= 0 or particle[1] <= 0):
            list_of_particles.remove(particle)

    gfxdraw.hline(screen, 0, int(W_SIZE[0]), BREAKPOINT, RED)

    pygame.display.update()
    screen.fill(BLACK)


if __name__ == '__main__':
    create_cube()

    while 1:
        try:
            game()
        except Exception as e:
            print(e)
            sys.exit()
