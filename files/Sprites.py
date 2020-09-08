import json
import os
from files.constants import Constants as K
import pygame
from random import randrange, uniform


class SpriteSheet:
    def __init__(self, name, path=""):
        self.mediaPath = os.getcwd() + '/media/' + path

        self._sheet = pygame.image.load(f'{self.mediaPath}/{name}/{name}.png').convert_alpha()
        self._metaData = json.load(open(f'{self.mediaPath}/{name}/{name}.json'))

        size = self._metaData["meta"]["size"]
        w = self._sheetWidth = size['w']
        h = self._sheetHeight = size['h']
        self.frames = w // h

        self.cells = []
        for i in range(self.frames):
            frame = self._metaData["frames"][f'{i}.']["frame"]
            self.cells.append(pygame.rect.Rect((frame['x'], frame['y']), (frame['w'], frame['h'])))

        self.images = []
        for i in range(self.frames):
            self.images.append(self._getImage(self.cells[i]))

        self.once = False
        f = self.currentFrame = 0
        self.image = self.images[f]
        self.rect = self.cells[f]

    def _getImage(self, rect):
        image = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA, 32)
        image = image.convert_alpha()
        image.blit(self._sheet, (0, 0), rect)
        return image


class Sprites(pygame.sprite.Sprite, SpriteSheet):
    def __init__(self, name, frames=0, path=""):
        pygame.sprite.Sprite.__init__(self)
        if frames == 0:
            SpriteSheet.__init__(self, name, path)
        else:
            self.mediaPath = os.getcwd() + '/media/' + path

            self.frames = frames
            if frames != 1:
                self.images = list(
                    [pygame.image.load(f'{self.mediaPath}/{name}/{name}{i + 1}.png').convert_alpha() for i in
                     range(frames)]
                )
            else:
                self.images = [pygame.image.load(f'{self.mediaPath}/{name}/{name}.png').convert_alpha()]

            self.cells = list(
                [self.images[i].get_rect() for i in range(frames)]
            )

            self.once = False
            f = self.currentFrame = 0
            self.image = self.images[f]
            self.rect: pygame.Rect = self.cells[f]
            self.originalWidth = self.rect.w
            self.originalHeight = self.rect.h
        self.delay = 0

    def scale(self, n=4, fromOriginal=False):
        if fromOriginal:
            for i in range(self.frames):
                self.cells[i].w = self.originalWidth * n
                self.cells[i].h = self.originalHeight * n
        else:
            for i in range(self.frames):
                self.cells[i].w *= n
                self.cells[i].h *= n

        for i in range(self.frames):
            self.images[i] = pygame.transform.scale(self.images[i], (self.cells[i].w, self.cells[i].h))

    def update(self, x=0, y=0, once=False, delay=0):
        if self.delay:
            self.delay -= 1
            return
        else:
            self.delay = delay

        self.once = once
        f = self.currentFrame = (self.currentFrame + 1) % self.frames

        if once and f == 0:
            self.once = False
            return

        self.image = self.images[f]
        self.rect = self.cells[f]
        self.rect.x = x
        self.rect.y = y


class Cloud(Sprites):
    def __init__(self, name, frames=0, path=''):
        super(Cloud, self).__init__(name, frames, path)
        self.velocity = 0
        self.newCloud(frames)

    def newCloud(self, frames):
        f = self.currentFrame = randrange(frames)
        self.scale(randrange(5, 7), True)
        self.image = self.images[f]
        self.rect = self.cells[f]

        self.velocity = uniform(2, 5)
        self.rect.y = randrange(50, 200)
        self.rect.x = -self.rect.w

    def update(self):
        if self.rect.x >= K.width:
            self.newCloud(self.frames)

        self.rect.x += self.velocity


class HealthBar(Sprites):
    def __init__(self, name, path=''):
        super(HealthBar, self).__init__(name, 1, path)
        self.health = 1
        b = self.bar = pygame.Surface((int(self.rect.w * 0.627), int(self.rect.h * 0.35)))
        b.fill(K.green)
        self.barRect = b.get_rect()
        self.rect.x = 120
        self.rect.y = 0
        self.xOffset = self.rect.w // 5.3
        self.yOffset = self.rect.h // 2.9

    def scale(self, n=4, fromOriginal=False):
        super(HealthBar, self).scale(n, fromOriginal)
        self.barRect.w *= n
        self.barRect.h *= n
        self.bar = pygame.transform.scale(self.bar, (self.barRect.w, self.barRect.h))
        self.image = self.images[0]
        self.rect = self.cells[0]
        self.xOffset = self.rect.w // 5.3
        self.yOffset = self.rect.h // 2.9

    def update(self, health, screen):
        if self.health != health:
            self.health = health
            ratio = health / 1.0
            self.barRect.w = self.barRect.w * ratio

        screen.blit(self.bar, (self.rect.x + self.xOffset, self.rect.y + self.yOffset), self.barRect)
