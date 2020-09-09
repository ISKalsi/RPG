from files.library.Elements import *

# initialization
pygame.init()
pygame.display.set_caption("RPG")
screen = pygame.display.set_mode((K.width, K.height))
clock = pygame.time.Clock()

bg = Sprites('background', 1)
bg.scale(6)

# CHINTU SPRITES
stickmanSprites = {
    "attack": Sprites('Stickman_Sword_Attaack', 39),
    "still": Sprites('stickman_still')
}

chintuSprites = {
    "coins": Sprites('coin', 12),
    "health": SnekHealthBar('snek_healthbar_frame', 'pixel art samples', (120, 0)),
    "stickman": stickmanSprites
}

# SPRITE GROUPS
background = pygame.sprite.Group()
ui = pygame.sprite.Group()
players = pygame.sprite.Group()
triggerOnce = pygame.sprite.Group()

# BACKGROUND ELEMENTS
background.add(bg)
for i in range(10):
    background.add(Cloud('cloud samples', 3, 'pixel art samples', i))


# UPDATE BACKGROUND
def updateBG():
    background.update()
    background.draw(screen)
