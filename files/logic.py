import random


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


class Player:
    # def __init__(my, i):
    #     my.name = input('enter the name of player' + str(i)+ ' => ')

    #     my.health = int(input('enter the health of player' + str(i)+ ' => '))
    #     while my.health > 100:
    #             print("aukat me value daaliye")
    #             my.health = int(input('enter the health of player' + str(i)+ ' => '))

    #     my.agility = int(input('enter the agility of player' + str(i)+ ' => '))
    #     while my.agility > 20:
    #             print("aukat me value daaliye")
    #             my.agility = int(input('enter the agility of player' + str(i)+ ' => '))

    #     while my.health + my.agility > 100:
    #         print('sum of health and agility cannot exceed 100 !')

    #         my.health = int(input('enter the health of player' + str(i)+ ' => '))
    #         while my.health > 100:
    #             print("aukat me value daaliye")
    #             my.health = int(input('enter the health of player' + str(i)+ ' => '))

    #         my.agility = int(input('enter the agility of player' + str(i)+ ' => '))
    #         while my.agility > 20:
    #             print("aukat me value daaliye")
    #             my.agility = int(input('enter the agility of player' + str(i)+ ' => '))

    #     print('Choose your weapon',my.name,'(Name - Damage, Dexterity)')
    #     j = 1
    #     for weapon in weapons:
    #         print(str(j) + ". " + weapon.name + " - " + str(weapon.damage) + ", " + str(weapon.dexterity))
    #         j += 1

    #     choice = int(input(' => ')) - 1
    #     while choice < 1 and choice > len(weapons):
    #         print('choose from the option given')
    #         choice = int(input(' => ')) - 1

    #     my.weapon = weapons[choice]

    def __init__(my, name, health, agility, weapon):
        my.name = name
        my.health = health
        my.agility = agility
        my.weapon = weapon
        my.coins = 0
        my.upgrade_cost = 0

    def player_attack(player, p):
        p.health -= player.weapon.generate_damage()
        if p.health <= 0:
            print(p, "loses")
        else:
            return p.health

    def agility_dodge(player, a):
        if (player.agility - a.weapon.dexterity) <= 0:
            player.health -= a.weapon.generate_damage()
        return player.health

    def coins_gain(self, t):
        if (self.agility - t.weapon.dexterity) > 0:
            self.coins += t.weapon.dexterity

    def upgrade_weapon(self):
        self.weapon.upgrade(self.weapon.level + 1)
        self.upgrade_cost += 10 + (self.weapon.level - 2) * 10
        self.coins -= self.upgrade_cost


# WEAPONS
weapon_list = [Weapon('SWORD', 10, 15), Weapon('HAMMER', 20, 5), Weapon('KATTARS', 5, 20), Weapon('SPEAR', 15, 10)]
