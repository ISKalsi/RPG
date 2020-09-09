import os
from files.library.Sprites import Sprites
from random import randrange
import pygame
from files.constants import Constants as K


class SnekHealthBar(pygame.sprite.Sprite):
    def __init__(self, name, path='', placeAt=(0, 0)):
        super().__init__()
        self.mediaPath = os.getcwd() + '/files/media/' + path

        self.frame = pygame.image.load(f'{self.mediaPath}/{name}/{name}.png').convert_alpha()
        self.frameRect = self.frame.get_rect()
        w = self.originalWidth = self.frameRect.w
        h = self.originalHeight = self.frameRect.h

        self.xOffset = self.frameRect.w // 5.3
        self.yOffset = self.frameRect.h // 2.9

        self.health = 1

        b = self.bar = pygame.Surface((int(w * 0.627), int(h * 0.35)))
        b.fill(K.green)
        self.barRect = b.get_rect()

        r = self.image = pygame.surface.Surface(self.frameRect.size, pygame.SRCALPHA).convert_alpha()
        r.blit(self.bar, (self.xOffset, self.yOffset), self.barRect)
        r.blit(self.frame, (0, 0), self.frameRect)

        self.rect = r.get_rect(topleft=placeAt)

    def scale(self, n=4):
        f = self.frameRect.size = ([int(i*n) for i in self.frameRect.size])
        self.frame = pygame.transform.scale(self.frame, f)

        r = self.rect.size = ([int(i*n) for i in self.rect.size])
        self.image = pygame.transform.scale(self.image, r)

        b = self.barRect.size = ([int(i*n) for i in self.barRect.size])
        self.bar = pygame.transform.scale(self.bar, b)

        self.xOffset = f[0] // 5.3
        self.yOffset = f[1] // 2.9

    def update(self, x, y, health):
        if self.health != health:
            self.health = health
            ratio = health / 1.0
            self.barRect.w = int(self.barRect.w * ratio)

            r = self.image
            r.fill(K.transparent)
            r.blit(self.bar, (self.xOffset, self.yOffset), self.barRect)
            r.blit(self.frame, (0, 0), self.frameRect)
            self.rect = r.get_rect(topleft=(x, y))


class Cloud(Sprites):
    flag = False

    def __init__(self, name, frames=0, path='', offset=-1):
        super(Cloud, self).__init__(name, frames, path)
        self.velocity = 3
        self.newCloud(offset)

    def newCloud(self, offset=-1):
        f = self.currentFrame = randrange(1)
        self.scale(randrange(2, 4), True)
        self.image = self.images[f]
        self.rect = self.cells[f]

        # self.velocity = uniform(2, 5)
        self.rect.y = randrange(130, 190) if Cloud.flag else randrange(220, 290)
        self.rect.x = -self.rect.w if offset == -1 else offset * 120
        Cloud.flag = not Cloud.flag

    def update(self):
        if self.rect.x >= K.width:
            self.newCloud()

        self.rect.x += self.velocity
