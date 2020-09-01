import pygame
import sys
from files.Sprites import Sprites, Cloud
from files.constants import Constants as K

# initialization
pygame.init()
pygame.display.set_caption("RPG")
screen = pygame.display.set_mode((K.width, K.height))
clock = pygame.time.Clock()

bg = Sprites('background', 1)
bg.scale(6)

attack = Sprites('Stickman_Sword_Attaack', 40)
still = Sprites('stickman_still')
test = Sprites('test')
anotherTest = Sprites('anotherTest', 50)

attack.scale(5)
still.scale(5)
test.scale(5)
anotherTest.scale(5)

background = pygame.sprite.Group(bg)
allSprites = pygame.sprite.Group(still)
triggerOnce = pygame.sprite.Group()

for _ in range(5):
    background.add(Cloud('cloud samples', 3, 'pixel art samples'))
# game loop
index = 0
while True:
    clock.tick(K.fps)

    # bg
    background.update()
    background.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LALT] and keys[pygame.K_F4]:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_SPACE:
                triggerOnce.add(attack)

            elif event.key == pygame.K_x:
                triggerOnce.add(test)
                pass

    if triggerOnce:
        triggerOnce.update(100, 225, True, 2)
        for sprite in triggerOnce.sprites():
            if not sprite.once:
                triggerOnce.remove(sprite)
        if triggerOnce:
            triggerOnce.draw(screen)
        else:
            continue
    else:
        # still animation
        allSprites.update(100, 225, False, 2)
        allSprites.draw(screen)

    # final update
    pygame.display.update()

