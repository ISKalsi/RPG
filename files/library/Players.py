import random


class Weapon:
    def __init__(self, name, damage, dexterity):
        self.damage = damage
        self.dexterity = dexterity
        self.name = name
        self.level = 1

    def generate_damage(self):
        return random.randrange(self.damage - 6, self.damage + 6)

    def upgrade(self, level):
        # level upgrade
        self.level = level
        self.damage += 3 + level
        self.dexterity += level - 1


class Player:
    def __init__(self, name, health, agility, weapon, sprite):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.agility = agility
        self.weapon = weapon
        self.coins = 0
        self.upgrade_cost = 0
        self.sprite = sprite

    def player_attack(self, p):
        p.health -= self.weapon.generate_damage()
        if p.health <= 0:
            print(p, "loses")
        else:
            return p.health

    def agility_dodge(self, a):
        if (self.agility - a.weapon.dexterity) <= 0:
            self.health -= a.weapon.generate_damage()
        return self.health

    def coins_gain(self, t):
        if (self.agility - t.weapon.dexterity) > 0:
            self.coins += t.weapon.dexterity

    def upgrade_weapon(self):
        self.weapon.upgrade(self.weapon.level + 1)
        self.upgrade_cost += 10 + (self.weapon.level - 2) * 10
        self.coins -= self.upgrade_cost

    # SPRITE METHODS
    def update(self):
        self.sprite["coins"].update(5, 5, delay=2)
        self.sprite["health"].update(120, 0, self.health/self.maxHealth)
