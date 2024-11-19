import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(x,y):
        super().__init__(x, y, SHOT_RADIUS)



