class ConsoleInput:
    def __init__(my, i):
        my.name = input('enter the name of player' + str(i) + ' => ')

        my.health = int(input('enter the health of player' + str(i) + ' => '))
        while my.health > 100:
            print("aukat me value daaliye")
            my.health = int(input('enter the health of player' + str(i) + ' => '))

        my.agility = int(input('enter the agility of player' + str(i) + ' => '))
        while my.agility > 20:
            print("aukat me value daaliye")
            my.agility = int(input('enter the agility of player' + str(i) + ' => '))

        while my.health + my.agility > 100:
            print('sum of health and agility cannot exceed 100 !')

            my.health = int(input('enter the health of player' + str(i) + ' => '))
            while my.health > 100:
                print("aukat me value daaliye")
                my.health = int(input('enter the health of player' + str(i) + ' => '))

            my.agility = int(input('enter the agility of player' + str(i) + ' => '))
            while my.agility > 20:
                print("aukat me value daaliye")
                my.agility = int(input('enter the agility of player' + str(i) + ' => '))

        print('Choose your weapon', my.name, '(Name - Damage, Dexterity)')
        j = 1
        for weapon in weapons:
            print(str(j) + ". " + weapon.name + " - " + str(weapon.damage) + ", " + str(weapon.dexterity))
            j += 1

        choice = int(input(' => ')) - 1
        while choice < 1 and choice > len(weapons):
            print('choose from the option given')
            choice = int(input(' => ')) - 1

        my.weapon = weapons[choice]
