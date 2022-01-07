from random import random, randint
from uuid import uuid4

from pygame import gfxdraw, Surface

from constants import Constants


class Particles:
    def __init__(self, screen: Surface, total_of_particles: int = 25):
        self.total_of_particles = total_of_particles
        self.screen = screen
        self.particles: list = []

    def create(self, x: int, y: int):
        for _ in range(self.total_of_particles):
            gx = -random() if randint(0, 1) else random()
            gy = random() if randint(0, 1) else -random()
            color = Constants.Colors.LIST[randint(0, len(Constants.Colors.LIST) - 1)]
            _id = str(uuid4())
            
            particle = [x, y, gx, gy, 5, color, x, y, _id]

            self.particles.append(particle)

    def render(self):
        for particle in self.particles:
            particle[0] = particle[0] + particle[2]
            particle[1] = particle[1] + particle[3]

            gfxdraw.aacircle(self.screen, int(particle[0]), int(particle[1]), int(particle[4]), particle[5])
            gfxdraw.filled_circle(self.screen, int(particle[0]), int(particle[1]), int(particle[4]), particle[5])

            particle[4] = particle[4] - 0.01
            
            if (particle[4] < 1 or particle[0] >= particle[6] + Constants.MAX_DISTANCE_TO_PARTICLES or
                    particle[0] <= particle[6] - Constants.MAX_DISTANCE_TO_PARTICLES or
                    particle[1] >= particle[7] + Constants.MAX_DISTANCE_TO_PARTICLES or
                    particle[1] <= particle[7] - Constants.MAX_DISTANCE_TO_PARTICLES or
                    particle[0] >= Constants.GAME_WIDTH or particle[1] >= Constants.GAME_HEIGHT or
                    particle[0] <= 0 or particle[1] <= 0):
                self.particles.remove(particle)
