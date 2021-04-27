import random


class Weapon:
    def __init__(self, name, inv_type, dmg_min, dmg_max, range_min, range_max, durability):
        self.name = name
        self.inv_type = inv_type
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.range_min = range_min
        self.range_max = range_max
        self.current_durability = ""
        self.durability = durability

    def __str__(self):
        return f'{self.name}'


class SlateSpells:    # WIP
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Armor:

    def __init__(self, name, inv_type, dmg_reduction, durability):
        self.name = name
        self.inv_type = inv_type
        self.dmg_reduction = dmg_reduction
        self.durability = durability

    def __str__(self):
        return f'{self.name}'


class HyruleWarrior:
    def __init__(self):
        self.name = 'Link'
        self.health = 1000
        self.weapon_inv = []
        self.slate_inv = []
        self.armor_inv = []
        self.current_weapon = ""
        self.current_armor = ""

    def __iter__(self):
        yield from self.weapon_inv
        yield from self.slate_inv
        yield from self.armor_inv

    def add_item(self, item):
        # Can this be condensed to comparing by class opposed to having a class type.
        if item.inv_type == "weapon":
            self.weapon_inv.append(item)
        elif item.inv_type == "spell":
            self.slate_inv.append(item)
        elif item.inv_type == "armor":
            self.armor_inv.append(item)
        print(f'{item} has been added to your inventory!')

    def display_inventory(self):
        print(f'\nCurrent Inventory:'
              f'\n\nCurrent Weapon: {self.current_weapon} - Durability: [{self.current_weapon.durability}]\n'
              f'Current Armor: {self.current_armor} - Durability: [{self.current_armor.durability}]\n'
              )
        self.list_weapons()
        print("\n")
        self.list_armor()
        print("\n")

    def list_armor(self):
        print(f'You currently have {len(self.armor_inv)} protective gear(s):')
        for index, armor in enumerate(self.armor_inv, 1):
            print(f'{index}. {armor} | Defense {armor.dmg_reduction} - Current Durability: {armor.durability}')

    def list_weapons(self):
        print(f'You currently have {len(self.weapon_inv)} weapon(s):')
        for index, weapon in enumerate(self.weapon_inv, 1):
            print(f'{index}. {weapon} | Range: {weapon.range_min}~{weapon.range_max} '
                  f'- Damage: {weapon.dmg_min}~{weapon.dmg_max} - Current Durability: {weapon.durability}')

    def action_check(self):
        if self.current_weapon not in self.weapon_inv:
            print("\nYou need a weapon!\n")
            self.change_weapon()
        elif self.current_weapon in self.weapon_inv:
            pass

    def change_weapon(self):
        is_valid = False
        self.list_weapons()
        while not is_valid:
            if not self.weapon_inv:
                print('You are out of weapons! You Lose :(')
                exit()
            else:

                wep_name = input("Choose your weapon... ")
                if wep_name.lower() in [i.name.lower() for i in self.weapon_inv]:
                    is_valid = True
                    self.equip_item(wep_name)
                else:
                    print(f'\n{wep_name} is not a valid weapon!\n')

    def equip_item(self, item):  # WIP
        if not self.current_weapon:
            self.current_weapon = self.weapon_inv[0]
        if not self.current_armor:
            self.current_armor = self.armor_inv[0]
        else:

            for weapon in self.weapon_inv:
                if weapon.name.lower() == item.lower():
                    self.current_weapon = weapon
                    print(f'\n{weapon} has been equipped!')

            for armor in self.armor_inv:
                if armor.name.lower() == item.lower():
                    self.current_armor = armor
                    print(f'\n{armor} has been equipped!')

    def attack(self):
        damage = random.randint(self.current_weapon.dmg_min, self.current_weapon.dmg_max)
        print(f'\n{self.name} attacks with {self.current_weapon} and hits Ganondorf for {damage} damage! ')
        self.gear_durability(self.current_weapon)
        return damage

    def range_check(self, boss_range):  # WIP
        if boss_range in range(self.current_weapon.range_min, self.current_weapon.range_max):
            able_to_hit = True
            return able_to_hit
        else:
            able_to_hit = False
            print('You missed!')
            return able_to_hit

    def gear_durability(self, item):
        gear_damage = random.randint(4, 8)
        item.durability = item.durability - gear_damage
        if item.durability <= 0:
            if item.inv_type == "weapon":  # Can I make this where it is not repeating?
                for weapon in self.weapon_inv:
                    if weapon == self.current_weapon:
                        print(f'\n{self.current_weapon} broke!\n')
                        self.weapon_inv.remove(weapon)
                        self.current_weapon = "none"
                        self.change_weapon()
                        return

            if item.inv_type == "armor":
                for armor in self.armor_inv:
                    if armor == self.current_armor:
                        print(f'{self.current_armor} broke!')
                        self.armor_inv.remove(armor)
                        self.current_armor = "none"
                        self.change_armor()
                        return


game_running = True
ganondorf_health = 1000
actions_list = ['h', 'equip', 'inventory', 'attack']

print("\n\nIt's dangerous to go alone! Take these!!\n")
player = HyruleWarrior()
master_sword = Weapon('Master Sword', "weapon", 35, 55, 0, 5, 1)
player.add_item(master_sword)
bow_of_light = Weapon('Bow of Light', "weapon", 40, 65, 15, 500, 100)
player.add_item(bow_of_light)
flame_sword = Weapon('Flame Sword', "weapon", 25, 30, 0, 5, 100)
player.add_item(flame_sword)
ice_sword = Weapon('Ice Sword', "weapon", 25, 30, 0, 5, 100)
player.add_item(ice_sword)
champions_tunic = Armor('Champion\'s Tunic', "armor", 45, 100)
player.add_item(champions_tunic)
hyrule_armor = Armor('Hyrule Armor', "armor", 35, 100)
player.add_item(hyrule_armor)
player.equip_item("")


while game_running:
    try:
        action = input("\nWhat would you like to do next? Type H for Help\n")
        if action.lower() not in actions_list:
            raise ValueError(f'{action} ')
    except ValueError as err:
        print(f'\nSorry {err} was not an action able to be performed.')
    else:
        pass

    if action.lower() == 'h':
        print('\n\n Help Options'
              '\n "Inventory" to view inventory'
              '\n "Equip" to change gear'
              '\n "Attack" to attack Ganondorf\n')

    elif action.lower() == 'attack':
        player.action_check()
        damage = player.attack()
        ganondorf_health -= damage
        if ganondorf_health <= 0:
            print("You win!")
            exit()
        else:
            print(f"\nGanondorf's health is currently [{ganondorf_health}]")
            print(f"Link's health is currently [{player.health}]")

    elif action.lower() == 'inventory':
        player.display_inventory()

    elif action.lower() == 'equip':
        player.display_inventory()
        item_to_equip = input("What item would you like to equip? ")
        try:
            if item_to_equip.lower() not in [i.name.lower() for i in player.weapon_inv]:
                raise ValueError(f'{item_to_equip} was not found in inventory')
        except ValueError as err:
            print(f'Sorry action was unable to be performed. {err}')
        else:
            player.equip_item(item_to_equip)






# how I want to create and attack
# action check - done
# range check - WIP
# probability check - WIP
# attack/dmg - armor dmg reduction - WIP
# health loss - WIP
# durability check - done


#things to work on
#ganondorf
#applying damage reduction
#working on probability
