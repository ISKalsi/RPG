import sys
from files.game import *
from files.library.Players import Player


chintu = Player("chintu", 1, 80, None, chintuSprites)

attack = chintu.sprite["stickman"]["attack"]
still = chintu.sprite["stickman"]["still"]
coin = chintu.sprite["coins"]
healthBar = chintu.sprite["health"]

attack.scale(5)
still.scale(5)
coin.scale(2)
healthBar.scale(2.3)

ui.add(coin, healthBar)
players.add(still)

# game loop
while True:
    clock.tick(K.fps)

    # bg
    updateBG()

    healthBar.update(0.99, screen)
    coin.update(5, 5, delay=2)
    ui.draw(screen)

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
        players.draw(screen)

    # final update
    pygame.display.update()
