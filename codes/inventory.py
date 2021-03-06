from abc import ABC, abstractmethod


# Inventory Class
class Inventory:
    @abstractmethod
    def __init__(self, inventory, money):
        """This class takes the user's inventory and money instance"""
        pass

    def get_weapon(self, item_name):
        """Obtain weapon items"""
        self.inventory.append(item_name)
        print("{} has gained a(an) {}! (damage: {})\n".format(self.nickname, item_name.name, item_name.damage))
        answer = input("Do you want to equip {}? (Y/N)".format(item_name.name))
        if answer == 'Y':
            self.change_weapon(item_name)

    def get_potion(self, item_name):
        """Obtain potion items"""
        self.inventory.append(item_name)
        print("{} has gained a(an) {}!".format(self.nickname, item_name.name))

    def get_money(self, amount):
        """Obtain money"""
        print("{} has gained {} yen!".format(self.nickname, amount))
        self.money += amount
        self.check_money()

    def lost_money(self, amount):  # Martin
        """losing money"""
        print("{} has lost {} yen!".format(self.nickname, amount))
        self.money -= amount
        self.check_money()

    def check_money(self):
        """Printing the remaining money"""
        print("{} has {} yen left\n".format(self.nickname, self.money))

    def throw_away_item(self, item_name):
        """Throw away the item that you have"""
        if item_name in self.inventory:
            self.inventory.remove(item_name)
        else:
            print("{} is not in the inventory.\n".format(item_name.name))