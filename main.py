import dino
import pygame
import sys
import map

clock = pygame.time.Clock()


class main:
    def __init__(self, width, height):
        self.width = width
        self.SpawnTime = 100
        self.height = height
        self.cactuslist = []
        self.aiout = 0
        self.dino = dino.player(height)
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)

    def handleInput(self):
        self.event = pygame.event.get()
        self.dino.handleInput(self.aiout)
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()
            if self.dino.dead == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.speed = 6
                        self.dino.dead = 0
                        self.cactuslist = []

    def handlecollition(self):
        for cactus in self.cactuslist:
            if self.dino.dino.colliderect(cactus.cactus):
                self.dino.speed = 0
                self.dino.dead = 1

    def spawncac(self):
        if self.dino.dead == 0:
            self.SpawnTime += 8
            if self.SpawnTime >= self.width:
                cactus = map.map (self.height, self.width)
                self.cactuslist.append(cactus)
                self.SpawnTime = 0

    def movemap(self):
        for cactus in self.cactuslist:
            cactus.move(self.dino.speed)

    def drawmap(self):
        if len(self.cactuslist) >= 1:
            for cactus in self.cactuslist:
                cactus.draw(self.screen)

    def draw(self):
        self.screen.fill((000, 000, 000))
        pygame.draw.rect(self.screen, (0, 255, 0), (0, 500 - 10, 600, 600))
        self.dino.drawplayer(self.screen)
        self.drawmap()
        pygame.display.flip()

    def ai(self):
        if len(self.cactuslist) >= 1:
            for cactus in self.cactuslist:
                if cactus.cactus.x <= 190 and cactus.cactus.x >= 50:
                    self.aiout = 1
                else:
                    self.aiout = 0

    def run(self):
        self.handleInput()
        self.dino.move()
        self.spawncac()
        self.ai()
        self.movemap()
        self.handlecollition()
        self.draw()


run = main(500, 500)
while True:
    clock.tick(60)
    run.run()
