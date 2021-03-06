from abc import ABC, abstractmethod


## Potion Class
class HP_Potion:
    """HP Potion class"""

    def __init__(self, name, point):
        self.name = name
        self.point = point

    def __str__(self):
        return "< {} >: recovers {} hp".format(self.name, self.point)

class MP_Potion:
    """MP Potion class"""

    def __init__(self, name, point):
        self.name = name
        self.point = point

    def __str__(self):
        return "< {} >: recovers {} mp".format(self.name, self.point)


# Weapon Class
class IWeapon(ABC):
    @abstractmethod
    def use_on(self, other_character):
        """Method for attacking other character"""
        pass

class Sword(IWeapon):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use_on(self, other_character):
        """Using sword method"""
        other_character.get_damage(self.damage)

    def __str__(self):
        return "< {} >: damage({})".format(self.name, self.damage)

class Gun(IWeapon):
    def __init__(self, name, damage, num_bullets):
        self.name = name
        self.damage = damage
        self.num_bullets = num_bullets  # the number of bullets

    def use_on(self, other_character):
        if self.num_bullets > 0:
            other_character.get_damage(self.damage)
            self.num_bullets -= 1
        else:
            print("There are not enough bullets. You cannot attack.\n")

    def __str__(self):
        return "< {} >: damage({}), bullets({})".format(self.name, self.damage, self.num_bullets)


####################################################################################
####################################################################################

# Potions
# HP
red_potion = HP_Potion('red potion', 30)
hunter_whiskey = HP_Potion("hunter's whiskey", 50)
elixir = HP_Potion("elixir", 100)

# MP
blue_potion = MP_Potion('blue potion', 10)
fairy_juice = MP_Potion("fairy juice", 20)

# Weapons
# Sword
hand = Sword("Hand", 1)
old_sword = Sword("Old Man's Sword", 5)
hunter_sword = Sword("Hunter's Sword", 7)
wooden_axe = Sword("Wooden Axe", 10)
dragon_slayer = Sword("Dragon Slayer", 30)

#Other weapons
lucky_Sword= Sword ("Wall Sword",8)

# Guns
gun = Gun("Gun", 5, 10)
pirate_gun = Gun("Pirate Gun", 8, 10)
captain_pistol = Gun("Captain's pistol", 20, 20)
grand_magnum_25 = Gun("Grand Magnum 25mm", 35, 30)


## Items Dictionary
potion_dict = {
    "Red Potion": str(red_potion),
    "Hunter's Whiskey": str(hunter_whiskey),
    "Elixir": str(elixir),

    "Blue Potion": str(blue_potion),
    "Fairy Juice": str(fairy_juice)
}

weapon_dict = {
    "Hunter Sword": str(hunter_sword),
    "Wooden Axe": str(wooden_axe),
    "Dragon Slayer": str(dragon_slayer),

    "Gun": str(gun),
    "Pirate Gun": str(pirate_gun),
    "Captain's Pistol": str(captain_pistol),
    "Grand Magnum 25mm": str(grand_magnum_25)
}