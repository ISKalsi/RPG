import json
import os
import sys

import pygame


class Sprites(pygame.sprite.Sprite):
    mediaPath = os.getcwd() + '/media/asprite'

    def __init__(self, name, frames):
        super(Sprites, self).__init__()
        self.frames = frames
        self.list = list(
            [pygame.image.load(f'{self.mediaPath}/{name}/{name}{i + 1}.png').convert_alpha() for i in range(frames)]
        )
        self.cells = list(
            [self.list[i].get_rect() for i in range(frames)]
        )

    def drawFrame(self, surface, i, x, y):
        surface.blit(self.list[i], (x, y), self.cells[i])

    def scale(self, n=4):
        for i in range(self.frames):
            self.cells[i][2] *= n
            self.cells[i][3] *= n

        for i in range(self.frames):
            self.list[i] = pygame.transform.scale(self.list[i], (self.cells[i][2], self.cells[i][3]))

    def animate(self, screen, x, y, fps):
        for index in range(self.frames):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            pygame.time.Clock().tick(fps)
            screen.fill((255, 255, 255))
            self.drawFrame(screen, index, x, y)
            pygame.display.update(self.cells[index])


class SpriteSheet(pygame.sprite.Sprite):
    mediaPath = os.getcwd() + '/media/asprite'

    def __init__(self, name):
        super(SpriteSheet, self).__init__()
        self.sheet = pygame.image.load(f'{self.mediaPath}/{name}/{name}.png').convert_alpha()
        self.metaData = json.load(open(f'{self.mediaPath}/{name}/{name}.json'))

        size = self.metaData["meta"]["size"]
        w = self.sheetWidth = size['w']
        h = self.sheetHeight = size['h']
        self.frames = w // h

        self.cells = []
        for i in range(self.frames):
            frame = self.metaData["frames"][f'{i}.']["frame"]
            self.cells.append((frame['x'], frame['y'], frame['w'], frame['h']))

    def drawFrame(self, surface, i, x, y):
        # frame = self.metaData["frames"][f'{i}.']["frame"]
        surface.blit(self.sheet, (x, y), self.cells[i])

    def scale(self, n=2):
        self.sheetWidth *= n
        self.sheetHeight *= n
        self.sheet = pygame.transform.scale(self.sheet, (self.sheetWidth, self.sheetHeight))

        for i in range(self.frames):
            self.cells[i] = tuple([k * n for k in self.cells[i]])

    def animate(self, screen, x, y, fps):
        for index in range(self.frames):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            pygame.time.Clock().tick(fps)
            screen.fill((255, 255, 255))
            self.drawFrame(screen, index, x, y)
            pygame.display.update()
