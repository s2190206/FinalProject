import pygame
from Maze.maze import Maze
import sys


class PrincessPlayer:

    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.PrincessPos = (0, 0)
        self.PrincessSize = 20
        self.princess = pygame.transform.scale(pygame.image.load('leon.jpg').convert_alpha(), (80, 80))
        self.movex = 0
        self.movey = 0
        self.frame = 0

    def draw_princess(self, screen):
        screen.blit(self.princess, (self.PrincessPos[0], self.PrincessPos[1]))
        pass

    def Update_princess(self, screen):
        self.PrincessPos.x = self.rect.x + self.movex
        self.PrincessPos.y = self.rect.y + self.movey
        pass

    def princess_move_LEFT(self, x):
        self.movex += x

    def princess_move_RIGHT(self, x):
        self.movex += x

    def princess_move_UP(self, y):
        self.movey += y

    def princess_move_DOWN(self, y):
        self.movey += y
