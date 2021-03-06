from abc import ABC, abstractmethod
from items import *
from skills import *

## Character's Action Class
class Action:
    @abstractmethod
    def __init__(self, inventory, weapon, money):
        """This class takes the user's inventory, weapon, and money"""
        pass

    def change_weapon(self, new_weapon: IWeapon):
        """Change the equipped weapon"""
        if new_weapon in self.inventory:
            self.weapon = new_weapon
            print("{} has equipped a(an) {}.".format(self.nickname, new_weapon))
            print("{}'s attack point: {}\n".format(self.nickname, new_weapon.damage))
        else:
            print("{} is not in your inventory.\n".format(new_weapon))

    def attack(self, object):
        """Attacking other object"""
        if self.hp > 0:
            print("{} attacked {}!".format(self.nickname, object.nickname))
            self.weapon.use_on(object)
        else:
            print("{} is dead.\n".format(self.nickname))

    def get_damage(self, damage):
        """method for deducting HP when attacked"""
        if self.hp <= damage:
            self.hp = 0
            print(self.nickname + " has died.\n")
        else:
            print("{} gets {} damage".format(self.nickname, damage))
            self.hp -= damage
            print("{}'s remaining hp: {} / {}".format(self.nickname, self.hp, self.MAX_HP))

    def show_hp(self):
        print("You have {} hp left.\n".format(self.hp))

    def use_hp_potion(self, potion: HP_Potion):
        """method for using HP potion"""
        if (self.hp + potion.point) >= self.MAX_HP:
            self.hp = self.MAX_HP
        else:
            self.hp += potion.point
        self.inventory.remove(potion)
        print("{} used one {}".format(self.nickname, potion.name))

    def use_mp_potion(self, potion: MP_Potion):
        """method for using MP potion"""
        if (self.mp + potion.point) >= self.MAX_MP:
            self.Mp = self.MAX_MP
        else:
            self.mp += potion.point
        self.inventory.remove(potion)
        print("{} used one {}!".format(self.nickname, potion.name))
        print("{}'s remaining hp: {}".format(self.nickname, self.hp))

    def get_skill(self, skill: Skill):
        self.skills.append(skill)

    def use_skill(self, skill: Skill, object):
        """method for using skill"""
        if (self.mp - skill.cost_mp) < 0:
            print("Not enough mp.")
        else:
            print("{} have used '{}'! ".format(self.nickname, skill.name))
            self.mp -= skill.cost_mp
            object.get_damage(skill.damage)
            print("{}'s remaing mp: {}".format(self.nickname, self.mp))