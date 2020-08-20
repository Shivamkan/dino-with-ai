import pygame
from random import randint

class map:
    def __init__(self,height,width):
        self.width = width
        self.height = height
        x = randint(420, 450)
        self.cactus = pygame.Rect(self.width,x,60, 200)

    def draw(self,screen):
        pygame.draw.rect(screen,(0,100,0),self.cactus)

    def move(self,speed):
        self.cactus.x -= speed