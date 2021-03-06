from user import *
from items import Sword
from action import *

# Monster Class
class Monster(Action):
    """Monster class"""
    def __init__(self, nickname, hp, mp, weapon):
        self.nickname = nickname
        self.hp = hp
        self.mp = mp
        self.weapon = weapon
        self.MAX_HP = hp

    def __str__(self):
        return self.nickname

####################################################################################
####################################################################################

# Monster damage
satyr_weapon = Sword("Satyr", 5)
basilisk_weapon =Sword("Basilisk", 15)
hydra_weapon = Sword("Hydra", 25)
werewolf_weapon = Sword("Werewolf", 10)
troll_weapon= Sword("Troll",8)
goblin_weapon = Sword("Goblin", 5)

damage5 = Sword('5', 5)
damage10 = Sword("10", 10)
damage15 = Sword('15', 15)
damage20 = Sword('20', 20)
damage25 = Sword('25', 25)
damage30 = Sword('30', 30)