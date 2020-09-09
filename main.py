import sys
from files.game import *
from files.library.Players import Player


chintu = Player("chintu", 100, 80, WeaponList.HAMMER, chintuSprites)
mintu = Player("mintu", 100, 90, WeaponList.SPEAR, chintuSprites)

attack = chintu.sprite["stickman"]["attack"]
still = chintu.sprite["stickman"]["still"]
dead = chintu.sprite["stickman"]["dead"]
coin = chintu.sprite["coins"]
healthBar = chintu.sprite["health"]

attack.scale(5)
still.scale(5)
dead.scale(5)
coin.scale(2)
healthBar.scale(2.3)

ui.add(coin, healthBar)
players.add(still)

delay = 2
flag = False
# game loop
while True:
    clock.tick(K.fps)

    # bg
    updateBG()
    chintu.update()
    ui.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            if flag:
                print("game over")
                pygame.quit()
                sys.exit(0)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LALT] and keys[pygame.K_F4] or keys[pygame.K_LSUPER] and keys[pygame.K_q]:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_SPACE:
                triggerOnce.add(attack)

            elif event.key == pygame.K_x:
                if not mintu.player_attack(chintu):
                    triggerOnce.add(dead)
                    flag = True
                    delay = 5
                else:
                    print(chintu.health)

    if triggerOnce:
        triggerOnce.update(100, 225, True, delay)
        for sprite in triggerOnce.sprites():
            if not sprite.once:
                triggerOnce.remove(sprite)
        if triggerOnce:
            triggerOnce.draw(screen)
        else:
            if chintu.health:
                continue
            else:
                players.remove(still)
                players.add(dead)
                dead.dead = True
                players.update(100, 225, delay=delay)
                players.draw(screen)
    else:
        # still animation
        players.update(100, 225, delay=delay)
        players.draw(screen)

    # final update
    pygame.display.update()
