import random
from files.ConsoleInput import ConsoleInput


class Weapon:
    def __init__(weapon, name, damage, dexterity):
        weapon.damage = damage
        weapon.dexterity = dexterity
        weapon.name = name
        weapon.level = 1

    def generate_damage(self):
        return random.randrange(self.damage - 6, self.damage + 6)

    def upgrade(self, level):
        # level upgrade
        self.level = level
        self.damage += 3 + level
        self.dexterity += level - 1


class Player(ConsoleInput):
    def __init__(self, name, health, agility, weapon):
        self.name = name
        self.health = health
        self.agility = agility
        self.weapon = weapon
        self.coins = 0
        self.upgrade_cost = 0

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


# WEAPONS
weapon_list = [Weapon('SWORD', 10, 15), Weapon('HAMMER', 20, 5), Weapon('KATTARS', 5, 20), Weapon('SPEAR', 15, 10)]
