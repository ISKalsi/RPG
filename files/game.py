import pygame
import sys
from files.Sprites import Sprites, SpriteSheet
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

allSprites = pygame.sprite.Group(still)


# game loop
index = 0
while True:
    clock.tick(K.fps)

    # bg
    bg.update()
    screen.blit(bg.image, (0, 0), bg.rect)

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
                # attack.animate(screen, 10, 10, K.fps)
                pass

            elif event.key == pygame.K_x:
                # anotherTest.animate(screen, 10, 10, K.fps)
                # test.animate(screen, 30, 30, K.fps)
                pass

    # still animation
    allSprites.update(100, 100)
    allSprites.draw(screen)

    # final update
    pygame.display.update()

