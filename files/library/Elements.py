from files.library.Sprites import Sprites
from random import randrange
import pygame
from files.constants import Constants as K


class SnekHealthBar(Sprites):
    def __init__(self, name, path=''):
        super(SnekHealthBar, self).__init__(name, 1, path)
        self.health = 1
        b = self.bar = pygame.Surface((int(self.rect.w * 0.627), int(self.rect.h * 0.35)))
        b.fill(K.green)
        self.barRect = b.get_rect()
        self.rect.x = 120
        self.rect.y = 0
        self.xOffset = self.rect.w // 5.3
        self.yOffset = self.rect.h // 2.9

    def scale(self, n=4, fromOriginal=False):
        super(SnekHealthBar, self).scale(n, fromOriginal)
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


class Cloud(Sprites):
    flag = False

    def __init__(self, name, frames=0, path='', offset=-1):
        super(Cloud, self).__init__(name, frames, path)
        self.velocity = 3
        self.newCloud(frames, offset)

    def newCloud(self, frames, offset=-1):
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
            self.newCloud(self.frames)

        self.rect.x += self.velocity
