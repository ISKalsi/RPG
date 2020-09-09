import sys
from files.library.Elements import *
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
coin = Sprites('coin', 12)
healthBar = SnekHealthBar('snek_healthbar_frame', 'pixel art samples')

attack.scale(5)
still.scale(5)
coin.scale(2)
healthBar.scale(2.3)

background = pygame.sprite.Group(bg)
allSprites = pygame.sprite.Group(coin, healthBar)
player = pygame.sprite.Group(still)
triggerOnce = pygame.sprite.Group()

for i in range(10):
    background.add(Cloud('cloud samples', 3, 'pixel art samples', i))
# game loop
while True:
    clock.tick(K.fps)

    # bg
    background.update()
    background.draw(screen)

    healthBar.update(0.99, screen)
    coin.update(5, 5, delay=2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LALT] and keys[pygame.K_F4] or keys[pygame.K_LSUPER] and keys[pygame.K_q]:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_SPACE:
                triggerOnce.add(attack)

            elif event.key == pygame.K_x:
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
        # allSprites.update(100, 225, False)
        still.update(100, 225, delay=2)
        player.draw(screen)

    allSprites.draw(screen)
    # final update
    pygame.display.update()
