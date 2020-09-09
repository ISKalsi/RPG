from files.library.Players import Weapon


class K:
    # screen
    width = 1200
    height = 600
    fps = 30

    # colors
    black = (0, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    transparent = (0, 0, 0, 0)

    # health bar positions


# WEAPONS
class WeaponList:
    SWORD = Weapon('SWORD', 10, 15)
    HAMMER = Weapon('HAMMER', 20, 5)
    KATTARS = Weapon('KATTARS', 5, 20)
    SPEAR = Weapon('SPEAR', 15, 10)
