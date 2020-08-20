import pygame
from util import *
import map


class player:
    def __init__(self,height):
        self.height = height
        self.monvingspeed = 0
        self.dead = 0
        self.speed = 6
        self.dino = pygame.Rect(50, 100, 50, 50)

    def jump(self):
        if self.dino.y >= self.height - 62 and self.dead ==0:
            self.dino.y -= 5
            self.monvingspeed = -12

    def move(self):
        self.dino.y += int(self.monvingspeed)
        self.monvingspeed += 0.6
        if self.dino.y >= self.height - 12 - self.dino.height:
            self.monvingspeed = 0

    def handleInput(self, input):
        if input:
            self.jump()

    def drawplayer(self,screen):
        pygame.draw.rect(screen,(RGB("#424242")),self.dino)