from abc import ABC, abstractmethod
from action import *
from inventory import *
import sys

# User Information Class
class User(Inventory, Action):
    """User class"""
    GAME = "Waseda RPG"
    MAX_HP = 100
    MAX_MP = 30

    def __init__(self):
        """basic information of user"""
        self.id = None
        self.password = None
        self.nickname = None
        self.hp = User.MAX_HP
        self.inventory = []
        self.weapon = hand
        self.money = 10000
        self.mp = User.MAX_MP
        self.skills = []

    def make_id(self):
        """Making a user account"""
        print("<< Making a new account... >>")
        id = input("Please type in an id: ")
        password = input("Please type in a password: ")

        self.id = id
        self.password = password

        print("Your account has successfully been created.\n")

    def login(self):
        """Log-in method"""
        login = False
        while login == False:
            print("<< Log-in to the game! >>")
            id = input("Please type in your account: ")
            password = input("Please type in your password: ")

            if (self.id == id) and (self.password == password):
                print("Log-in successful.\n")
                return True
            else:
                print("Invalid account. Please try again.\n")

    def make_character(self):
        if self.login() == True:
            print("<< Making your character... >>")
            nickname = input("Please select your character's nickname: ")
            self.nickname = nickname
            print("Welcome to {} {}! A fantasy world awaits you.\n".format(User.GAME, self.nickname))
        else:
            sys.exit()

    def __str__(self):
        return "Character Information \nName: {}\nHp: {}/{}\nMp: {}/{}\nWeapon: {} ({})".format(self.nickname, self.hp,
                                                                                                self.MAX_HP, self.mp,
                                                                                                self.MAX_MP,
                                                                                                self.weapon,
                                                                                                self.weapon.damage)
