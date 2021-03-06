from items import *
from skills import *
from user import *
from inventory import *
from mob import *
from action import *
import time
import random


# Blank (for making empty lines between lines)
def Blank():
    print()
    print()
    print()
    print()
    print()


# Short Loading (2.1 seconds)
def Loading():
    print()
    print("Loading", end='')
    for i in range(3):
        time.sleep(0.7)
        print(".", end='')
    print()
    print()


# For Printing elements in a list
def PrintList(list):
    for i in range(len(list)):
        print(list[i])
    print()


# Long Loading (5 seconds)
def Long_loading():
    print()
    print("Loading", end='')
    for i in range(10):
        time.sleep(0.5)
        print(".", end='')
    print()
    print()


# If/When the player is dead or has died
def Dead(user):  # Natsuki Osada
    if user.hp == 0:
        Loading()
        print("You have woken up in a church in town")
        print("Oh... How unfortunate! You shall be given another chance!")
        user.hp = user.MAX_HP
        user.mp = user.MAX_HP
        Town(user)


# Battle
def StartBattle(self, opponent):
    print("Prepare for battle!\n")
    while (self.hp > 0) and (opponent.hp > 0):
        print("What is {} going to do next?".format(self.nickname))
        print("1: Attack\n2: Use a potion\n3: Use a skill")
        next_move = input("Next move: ")
        print()

        # If/When the user chooses to attack
        if next_move == '1':
            self.attack(opponent)
            time.sleep(1)

        # If/When the user chooses to use a potion
        elif next_move == '2':
            print("{}'s inventory: ".format(self.nickname))
            for i in range(len(self.inventory)):
                print(self.inventory[i], end=' | ')
            print()
            index = int(input("Which item do you want to use? (Select the index number): "))

            try:  # This is to prevent index errors
                if isinstance(self.inventory[index - 1], HP_Potion) == True:
                    self.use_hp_potion(self.inventory[index - 1])
                elif isinstance(self.inventory[index - 1], MP_Potion) == True:
                    self.use_mp_potion(self.inventory[index - 1])
                else:
                    print("The selected item is not a potion.")

            except IndexError:  # This is to prevent index errors
                print("There is no item in that index.")

            print()
            time.sleep(1)

        # If/When the user chooses to use a skill
        elif next_move == '3':
            print("{} skills: ".format(self.nickname))
            for i in range(len(self.skills)):
                print(self.skills[i], end=' | ')

            print()
            index = int(input("Which skill do you want to use? (Select the index number): "))

            try:  # This is to prevent index errors
                self.use_skill(self.skills[index - 1], opponent)
                print()
                time.sleep(1)

            except IndexError:  # This is to prevent index errors
                print("There is no skill in that index.")

        # opponent's attack
        if self.hp > 0:
            Loading()
            opponent.attack(self)
            print()
            # If/When the player's hp is lower than 0
            if self.hp <= 0:
                Dead(self)

    if self.hp > 0:
        self.show_hp


# Town (This function is called when the player enters "shinjuku villege")
def Town(user: User):
    leave_town = False
    print("{} is in the town".format(user))
    print()

    while leave_town == False:
        Blank()
        print("What is {} going to do next?: ".format(user.nickname))
        print()
        print("1. Go shopping\n2. Play Pachinko\n3. Go to the church\n4. Leave the town and head to Keio castle")
        user_choice = input("")
        Loading()

        # If/When the user chooses to go shopping
        if user_choice == '1':
            Shop(user)

        # If/When the user chooses to go to pachinko
        if user_choice == '2':
            Pachinko(user)

        # If/When the user chooses to go to the church
        if user_choice == '3':
            print("{} has visited the church.\nOne can take rest in the church.".format(user.nickname))
            Loading()
            print("{}'s hp/mp was fully recovered!".format(user.nickname))
            user.hp = user.MAX_HP
            user.mp = user.MAX_MP

        # If/When the user chooses to leave the town
        if user_choice == '4':
            print("{} has left the town.\n".format(user.nickname))
            leave_town = True


# Shop    (This function is called when the player chooses to go shopping in the town)
def Shop(user: User):
    leave_shop = False

    while leave_shop == False:

        Blank()
        print(" << 77-eleven >> ")
        print("Welcome to 77-eleven.\nWe have all of the things that you need for your journey.\nTake a look around!\n")

        user_choice = input("Which one are you interested in? (weapon/potion/skill/exit)")
        print()

        # If/When the player wants to buy a weapon
        if user_choice == "weapon":

            shop_weapon_list = (
            hunter_sword, wooden_axe, dragon_slayer, gun, pirate_gun, captain_pistol, grand_magnum_25)
            shop_weapon_names = list(weapon_dict.keys())
            shop_weapon_price = (500, 1500, 9999, 1000, 1800, 4500, 12000)

            print(" << 77-eleven's weapon section >> ")
            PrintList(shop_weapon_names)
            user_choice = int(input("Which one do you need? (Select the index number)"))
            try:  # This is to prevent type errors
                if type(user_choice) == type(1):
                    chosen_weapon_name = shop_weapon_names[user_choice - 1]
                    chosen_weapon_price = shop_weapon_price[user_choice - 1]
                    print("You want {}? That'll be {}yen!".format(chosen_weapon_name, chosen_weapon_price))
                    print()
                    buy = input("Do you want to buy? (Y/N)")
                    print()
                    if buy == "Y":
                        if user.money - chosen_weapon_price > 0:
                            print("Thank you very much. Here you go.\n")
                            user.money -= chosen_weapon_price
                            print("{} has bought {}!".format(user.nickname, chosen_weapon_name))
                            user.check_money()
                            user.get_weapon(shop_weapon_list[user_choice - 1])
                            print()
                        else:
                            print("Not enough money.\n")

            except IndexError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player wants to buy a potion
        elif user_choice == "potion":

            shop_potion_list = (red_potion, hunter_whiskey, elixir, blue_potion, fairy_juice)
            shop_potion_names = list(potion_dict.keys())
            shop_potion_price = (300, 500, 2000, 400, 800)

            print(" << 77-eleven's potion section >> ")
            PrintList(shop_potion_names)
            user_choice = int(input("Which one do you need? (Select the index number)"))
            try:  # This is to prevent type errors
                num_potion = int(input("How many do you need?: "))
                chosen_potion_name = shop_potion_names[user_choice - 1]
                chosen_potion_price = shop_potion_price[user_choice - 1] * num_potion

                print("You want {} {}? That'll be {}yen!".format(num_potion, chosen_potion_name, chosen_potion_price))
                print()
                buy = input("Do you want to buy? (Y/N)")
                print()
                if buy == "Y":
                    if user.money - chosen_potion_price > 0:
                        user.money -= chosen_potion_price
                        print("Thank you very much. Here you go.\n")
                        print("{} has bought {}!".format(user.nickname, chosen_potion_name))
                        user.check_money()
                        user.get_potion(shop_potion_list[user_choice - 1])
                        print()
                    else:
                        print("Not enough money.\n")

            except IndexError or ValueError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player wants to buy some skills
        elif user_choice == "skill":
            shop_skill_list = (triple_slash, quadruple_slash, firebolt, icestrike, meteor, iceage)
            shop_skill_names = list(skill_dict.keys())
            shop_skill_price = (4000, 6000, 8000, 8000, 14000, 14000)

            print(" << 77-eleven's skill section >> ")
            PrintList(shop_skill_names)
            user_choice = int(input("Which skill do you want to learn? (Select the index number)"))
            try:  # This is to prevent type errors
                chosen_skill_name = shop_skill_names[user_choice - 1]
                chosen_skill_price = shop_skill_price[user_choice - 1]

                print("You want to learn {}? That'll be {}yen!".format(chosen_skill_name, chosen_skill_price))
                print()
                buy = input("Do you want to buy? (Y/N)")
                print()
                if buy == "Y":
                    if user.money - chosen_skill_price > 0:
                        user.money -= chosen_skill_price
                        print("Thank you very much. Focus!\n")
                        print("{} has learned {}!".format(user.nickname, chosen_skill_name))
                        user.check_money()
                        user.get_skill(shop_skill_list[user_choice - 1])
                        print()
                    else:
                        print("Not enough money.\n")

            except IndexError or ValueError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player decides to quit shopping
        elif user_choice == "exit":
            leave_shop = True

        # If/When the player didn't choose among the four options
        else:
            print("An error has occured. Please select again.")
            print()

    # If/When the player leaves the shop
    print("{} has left the shop".format(user.nickname))


# Omiyage Mart
def Shop1(user: User):  # Martin
    leave_shop = False

    while leave_shop == False:

        Blank()
        print(" <<Omiyage Mart>> ")
        print(
            "Welcome to Omiyage Mart,your one-stop shop for any last-minute purchases.\nOur prices are steeper,but so is the cost of venturing into Keio Castle unprepared. Please feel free to look around!\n")

        user_choice = input("Which one are you interested in? (weapon/potion/skill/exit)")
        print()

        # If/When the player wants to buy a weapon
        if user_choice == "weapon":

            shop_weapon_list = (
            hunter_sword, wooden_axe, dragon_slayer, gun, pirate_gun, captain_pistol, grand_magnum_25)
            shop_weapon_names = list(weapon_dict.keys())
            shop_weapon_price = (650, 2000, 11000, 1500, 2500, 5000, 12100)

            print(" << Omiyage Mart's weapon section >> ")
            PrintList(shop_weapon_names)
            user_choice = int(input("Which one do you need? (Select the index number)"))
            try:  # This is to prevent type errors
                if type(user_choice) == type(1):
                    chosen_weapon_name = shop_weapon_names[user_choice - 1]
                    chosen_weapon_price = shop_weapon_price[user_choice - 1]
                    print("You want {}? That'll be {}yen!".format(chosen_weapon_name, chosen_weapon_price))
                    print()
                    buy = input("Do you want to buy? (Y/N)")
                    print()
                    if buy == "Y":
                        if user.money - chosen_weapon_price > 0:
                            print("Thank you very much. Here you go.\n")
                            user.money -= chosen_weapon_price
                            print("{} has bought {}!".format(user.nickname, chosen_weapon_name))
                            user.check_money()
                            user.get_weapon(shop_weapon_list[user_choice - 1])
                            print()
                        else:
                            print("Not enough money.\n")

            except IndexError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player wants to buy potion
        elif user_choice == "potion":

            shop_potion_list = (red_potion, hunter_whiskey, elixir, blue_potion, fairy_juice)
            shop_potion_names = list(potion_dict.keys())
            shop_potion_price = (400, 600, 3000, 500, 900)

            print(" << Omiyage Mart's potion section >> ")
            PrintList(shop_potion_names)
            user_choice = int(input("Which one do you need? (Select the index number)"))
            try:  # This is to prevent type errors
                num_potion = int(input("How many do you need?: "))
                chosen_potion_name = shop_potion_names[user_choice - 1]
                chosen_potion_price = shop_potion_price[user_choice - 1] * num_potion

                print("You want {} {}? That'll be {}yen!".format(num_potion, chosen_potion_name, chosen_potion_price))
                print()
                buy = input("Do you want to buy? (Y/N)")
                print()
                if buy == "Y":
                    if user.money - chosen_potion_price > 0:
                        user.money -= chosen_potion_price
                        print("Thank you very much. Here you go.\n")
                        print("{} has bought {}!".format(user.nickname, chosen_potion_name))
                        user.check_money()
                        user.get_potion(shop_potion_list[user_choice - 1])
                        print()
                    else:
                        print("Not enough money.\n")

            except IndexError or ValueError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player wants to buy some skills
        elif user_choice == "skill":
            shop_skill_list = (triple_slash, quadruple_slash, firebolt, icestrike, meteor, iceage)
            shop_skill_names = list(skill_dict.keys())
            shop_skill_price = (4500, 6500, 8500, 8500, 14100, 14100)

            print(" << Omiyage Mart's skill section >> ")
            PrintList(shop_skill_names)
            user_choice = int(input("Which skill do you want to learn? (Select the index number)"))
            try:  # This is to prevent type errors
                chosen_skill_name = shop_skill_names[user_choice - 1]
                chosen_skill_price = shop_skill_price[user_choice - 1]

                print("You want to learn {}? That'll be {}yen!".format(chosen_skill_name, chosen_skill_price))
                print()
                buy = input("Do you want to buy? (Y/N)")
                print()
                if buy == "Y":
                    if user.money - chosen_skill_price > 0:
                        user.money -= chosen_skill_price
                        print("Thank you very much. Focus!\n")
                        print("{} has learned {}!".format(user.nickname, chosen_skill_name))
                        user.check_money()
                        user.get_skill(shop_skill_list[user_choice - 1])
                        print()
                    else:
                        print("Not enough money.\n")

            except IndexError or ValueError:  # This is to prevent type errors
                print("An error has occured. Please try again.\n")

        # If/When the player decides to quit shopping
        elif user_choice == "exit":
            leave_shop = True

        # If/When the player didn't choose among the four options
        else:
            print("An error has occured. Please select again.")
            print()

    # If/When the player leaves the shop
    print("{} has left the shop".format(user.nickname))


# Pachinko (This function is called when the player chooses to gamble in the town)
def Pachinko(user: User):
    print("Welcome to Waseda Pachinko.\nWhich game do you want to play?\n")
    exit_pachinko = False

    while exit_pachinko == False:
        choice = input("Rock Scissors Paper / Odd & Even / Exit      (Select index number)")
        print()

        # Player chooses to play rock scissors paper
        if choice == '1':
            print("Dealer: So you want to play rock scissors paper? A classic one eh?")
            print("If you win me, you will get double the money you have bet.")
            user.check_money()
            bet_money = int(input("How much will you bet?: ()yen"))

            # If player don't have enough money, end process
            if user.money - bet_money < 0:
                print("You don't have enough money! Get lost!\n")
                continue

            print("Your bet: {}".format(bet_money))
            print()

            # Player chooses
            player_choice = input("rock/scissor/paper:")

            # Computer chooses randomly
            rcp_list = ['rock', 'scissor', 'paper']
            random_index = random.randint(1, 3) - 1
            computer_choice = rcp_list[random_index]

            # Result
            if player_choice == "rock":
                if computer_choice == "rock":
                    print("It is a draw.")
                elif computer_choice == 'paper':
                    print("You lost.")
                    print("{} has lost {}yen.".format(user.nickname, bet_money))
                    user.money -= bet_money
                    user.check_money()
                elif computer_choice == 'scissor':
                    print("You won!")
                    user.get_money(bet_money)

            elif player_choice == 'scissor':
                if computer_choice == "scissor":
                    print("It is a draw.")
                elif computer_choice == 'rock':
                    print("You lost.")
                    user.money -= bet_money
                    user.check_money()
                elif computer_choice == 'paper':
                    print("You won!")
                    user.get_money(bet_money)

            elif player_choice == "paper":
                if computer_choice == "paper":
                    print("It is a draw.")
                elif computer_choice == 'scissor':
                    print("You lost.")
                    user.money -= bet_money
                    user.check_money()
                elif computer_choice == 'rock':
                    print("You won!")
                    user.get_money(bet_money)

            else:
                print("An error has occured. Please try again.")

            Blank()

        # Player chooses to play Odd & Even
        elif choice == '2':
            print(
                "Dealer: \nThis game is very simple. I'm going to pick a random number from 1~100, and you just simply have to guess if that number is odd or even.")
            print("If you guessed it correctly, you get double the money you have bet.")
            user.check_money()
            bet_money = int(input("How much will you bet?: ()yen"))
            # If player don't have enough money, end process
            if user.money - bet_money < 0:
                print("You don't have enough money! Get lost!\n")
                continue

            player_choice = input("odd or even?: ")
            print()

            print("The number was...")
            Loading()
            random_number = random.randint(1, 100)
            print("{}!! ".format(random_number))
            print()

            # Result
            if player_choice == 'odd':
                if random_number % 2 == 1:
                    print("Congratulations! You won!")
                    user.get_money(bet_money)
                else:
                    print("Oops, you have lost.")
                    print("{} have lost {}yen".format(user.nickname, bet_money))
                    user.money -= bet_money
                    user.check_money()

            elif player_choice == 'even':
                if random_number % 2 == 0:
                    print("Congratulations! You won!")
                    user.get_money(bet_money)
                else:
                    print("Oops, you have lost.")
                    print("{} have lost {}yen".format(user.nickname, bet_money))
                    user.money -= bet_money
                    user.check_money()

            Blank()

        elif choice == '3':
            exit_pachinko = True
            print("Thank you for visiting. We hope to see you next time!\n")
            print("{} has left pachinko".format(user.nickname))

        else:
            print("Wrong index number. Please try again.\n")


# Functions related to game play
# The prologue of the game
def Prologue(user1: User):
    Loading()
    print("<< Story >>")
    print("Once upon a time lived a boy named '{}'.".format(user1.nickname))
    print("One day, an evil king and his creatures attacked his town and stole his valuable treasure.")
    print("Therefore, he decided to begin his journey to get it back.")
    print("It is said that the evil king lives in a place called 'Keio Castle'.")
    print("Help him defeat the evil king and get his treasure back!")
    print("Let the journey begin...\n")
    Long_loading()

    # initial potion and item
    user1.get_potion(red_potion)
    user1.get_potion(red_potion)
    user1.get_skill(double_slash)


# Situation 1
def Situation1(user1: User):
    choice1 = input("{} has encountered an old man. Do you want to talk to him? (Y/N)".format(user1.nickname))
    if (choice1 == 'Y'):
        print("Old man:\nI'm old and poor.. I need 3000 yen for my dinner..\n")
        time.sleep(1)
        choice2 = input("Give him money?: (Y/N)")
        if (choice2 == 'Y'):
            print("{} gave him 3000 yen.".format(user1.nickname))
            user1.money -= 3000
            user1.check_money()
            time.sleep(1)
            print("Old man:\nHow kind of you! Now I can have some Sushi.\nPlease take this as my gift to you.\n")
            time.sleep(1)
            user1.get_weapon(old_sword)  # The player gets an item
            time.sleep(1)
    else:
        print("{} has ignored the man".format(user1.nickname))
    Blank()
    print("{} continued the journey...".format(user1.nickname))
    Loading()


# Situation 2
def Situation2(user1: User):
    print("There is a forest! But it is very late.")
    print("Going into the forest at night could be dangerous.")
    print("You can camp out here and wait until the sun rises to pass through.")
    print()
    time.sleep(1)
    answer = input("Do you want to go into forest now?: (Y/N)")
    print()

    # If/When the player chooses to go into the forest
    if answer == "Y":
        print("{} has entered forest.".format(user1.nickname))
        Blank()
        Loading()
        print("A goblin appeared!")
        # Create a goblin monster
        goblin = Monster('goblin', 7, 0, goblin_weapon)
        time.sleep(1)
        # The player conducts battle with goblin
        StartBattle(user1, goblin)
        time.sleep(1)
        # The player gets money for defeating the goblin
        user1.get_money(50)
        Blank()

        Loading()
        # Quest
        print("Fairy: \nWow, you are strong! Please wanderer, a tribe of goblins has kidnapped my friends.")
        print("They were taken to a cave just near here. Can you help me?")
        user_choice = input("Will you help the fairy?: Y/N")
        print()

        # If/When the player accepts the quest
        if user_choice == 'Y':
            print("{} has decided to help the fairy. \n{} headed to the cave.\n".format(user1.nickname, user1.nickname))
            Blank()
            Loading()
            print("{} has entered the cave.".format(user1.nickname))
            Blank()
            Loading()
            # Create a bulk-up goblin
            monster = Monster('bulk-up goblin', 18, 0, damage10)
            print("Bulk-up goblin: ")
            print("Hmm..? A human...?\nHumans are sold at high prices!\nHaha, what a lucky day!!\n\n")
            time.sleep(2)
            print("'Bulk-up goblin' has attacked {}!".format(user1.nickname))
            # The player conducts battle
            StartBattle(user1, monster)
            time.sleep(1)
            user1.get_money(1500)

            Loading()

            # Event
            print("{} has found a treasure box!\n".format(user1.nickname))
            user_choice = input('Do you want to open it?: Y/N')
            print()
            if user_choice == 'Y':
                print("Oops! It was a trap!!".format(user1.nickname))
                user1.get_damage(6)

            Loading()
            Blank()
            # When the quest is complete
            print("{} has found the captured fairies. They were safely sent back home.\n".format(user1.nickname))
            time.sleep(1)
            print("Fairy: \nThank you so much wanderer!\nThis is a small gift from all of us!\n")
            user1.get_money(3000)
            time.sleep(1)
            print("<< {} has learned a skill 'Firebolt'! >>\n".format(user1.nickname))
            user1.get_skill(firebolt)
            Blank()
            Loading()
            print(
                "Fairy: \nThe way out of the forest is over by that side.\nMay the ancient spirit protect your journey...\n")
            Blank()
            Loading()

        # If/When the player refuses the quest
        else:
            print("{} has ignored the fairy.".format(user1.nickname))
            Blank()
            Loading()

        print("{} got out of the forest safely.".format(user1.nickname))

    # If/When the player doesn't choose to go into the forest in the first place
    else:
        print("{} decided to wait until morning.".format(user1.nickname))
        print("Sleeping", end='')
        for i in range(10):
            print(".", end='')
            time.sleep(1)
        print()
        print("{} has woken up!\n".format(user1.nickname))


# Situation 3
def Situation3(user1: User):
    Blank()
    Loading()
    print("{} has arrived at Shinjuku villege.\nThe village is full of different people.".format(user1.nickname))
    print("In the village, you can do many different things.")
    Town(user1)  # The player enters the town


# Situation 4 (Keio Castle: troll)
def Situation4(user1: User):  # Mariana
    Blank()
    print(
        "On your way to Keio Castle, you see a small cozy house in the middle of the woods with a sign that says 'Omiyage Mart: Weapons, Potions, Skills'")
    print()
    choice5 = input("Would you like to go into the store and get any last-minute purchases? Y/N".format(user1.nickname))
    if choice5 == 'Y':
        Shop1(user1)

    Blank()
    print("After walking for a few more hours, {} has arrived at Keio Castle.".format(user1.nickname))
    Loading()
    print("Prepare yourself for you still have a difficult journey ahead of you...")
    Loading()
    print("Guarding the first door of the castle is a gigantic green troll... he hasn't seen you yet.")
    troll = Monster('troll', 10, 0, troll_weapon)
    time.sleep(3)
    print("If you're quiet and fast enough, you can try and sneak past him... or, if you want, you can fight him.")
    choice3 = input("Will you try and sneak past him(S)... or will you try to fight him (F) ?")

    if choice3 == 'S':
        Blank()
        print("As the troll turns around, you start running for the next door quietly.")
        time.sleep(2)
        print("However, he has seen you from the corner of his eye and has started chasing you.")
        time.sleep(2)
        print(
            "You run as fast as you can towards the small corridor that connects the trolls room to the next door in the Castle...")
        time.sleep(2)
        print("You keep running, barely breathing and without looking back...")
        time.sleep(2)
        print("You're about to arrive to the thin corridor....!")
        Loading()
        print(
            "As you step in the corridor, you feel a strong hit on the back of your head that makes you fall to the ground.")
        user1.get_damage(8)
        print("The troll was able to hit you with his mace, but you managed to escape him.".format(user1.nickname))
        Loading()
    else:
        StartBattle(user1, troll)
        Loading()
        # The player gets some money for defeating the troll
        user1.get_money(1500)
        Blank()

        Loading()


# Situation 5 (Keio Castle: Werewolf)
def Situation5(user1: User):  # Martin
    Blank()
    print("You hear some growling and scratching through the next door, but there's no going back now...")
    time.sleep(3)
    print("You reluctantly turn the heavy, iron door handle...")
    Loading()
    werewolf = Monster('werewolf', 35, 10, werewolf_weapon)
    print(
        "The heavy, wooden door swings open, revealing a large, round, and cavernous room with a hairy, rabbid werewolf in the center of the room... A stream of saliva drips out of his mouth.")
    print()
    choice4 = input(
        "Do you want to make a run for it and try to escape him (R) or will you stand your ground and fight him (F) head-on?")
    print()
    if choice4 == 'R':
        user1.get_damage(20)
        print(
            "The werewolf is much faster than you are and so he bites you with his teeth and scratches you with his claws... ".format(
                user1.nickname))

        print()
        print(
            "You somehow manage to grab the sword hanging on the wall next to you and so you  manage to get the werewolf off of you! How very lucky of you!")
        user1.get_weapon(lucky_Sword)
        print("<< {} has found a new weapon: 'Lucky Sword'! >>\n".format(user1.nickname))

    else:
        StartBattle(user1, werewolf)
        time.sleep(1)
        print("<< {} has learned a skill: 'Triple-Slash'! >>\n".format(user1.nickname))
        user1.get_skill(triple_slash)
        user1.get_money(2000)
        Blank()
        Loading()


###Situation 6 (Keio Castle: Witch)
def Situation6(user1: User):  # Mariana
    print("The next door is slightly ajar and you hear a spine-chilling cackle pouring out from the open door...")
    Loading()
    print(
        "As you go inside you see a tiny, very green, very fat witch... She grabs her broom, her wand, and struggles to fly over to you. She smiles wider than you've ever seen someone smile...")
    print()
    time.sleep(3)
    print("Witch:\nSo you're the boy who's treasure we've hidden in one of our doors")
    time.sleep(1)
    print("To move on in your quest, you will first have to play a quick guessing game with me.")
    time.sleep(1)
    print()
    print(
        "You will have to guess 5 numbers from 1-60 and the only clues I will give you are whether the number you have guessed is too high or too low from my secret chosen numbers...")
    print()
    print("Try to guess quickly or you could end up staying here for a very, very, long time... HA-HA-HA-HA-HA")
    print()
    print("Are you ready to begin?")
    print()
    time.sleep(3)
    import random

    secretNum = [random.randint(1, 60) for i in range(5)]
    while (sum(secretNum) != -5):
        print("Guess a number:")
        userGuess = int(input())
        for i in range(5):
            if (userGuess == secretNum[i]):
                print("Element " + str(i + 1) + " guessed right!")
                secretNum[i] = -1
        print("[ ", end="")
        for i in range(5):
            if (secretNum[i] == -1):
                print("- ", end="")
            elif (userGuess < secretNum[i]):
                print("too low, ", end="")
            elif (userGuess > secretNum[i]):
                print("too high, ", end="")
        print("]")
    else:
        print("Oh come on... I was just starting to have some fun! But yeah, yeah, you won...")
    print()
    print("Carry on and good luck...")
    print()
    print()
    print("You exit the witch's room and start walking down to the next hall...")
    print()
    print()
    decision1 = input("Would you like to go back to Shinjuku village before you continue? Y/N ")
    if decision1 == 'Y':
        Situation3(user1)
        Situation7(user1)
    else:
        print()
        print("You continued your journey...")

    Blank()


# Situation 7 (Keio Castle: Satyr)
def Situation7(user1: User):  # Martin

    Loading()
    print("You hear some giggling and an infectious laughter echoing and bouncing off of the castle walls...")
    time.sleep(2)
    satyr = Monster('satyr', 10, 6, satyr_weapon)
    print("Hey, you there! What do you think you're doing running around in my halls...?")
    print()
    print("A small Satyr (Half goat, half-man) walks towards you angrily...")
    print()
    print("Even though he doesn't seem to have a weapon, he looks ready to attack you at any minute.")
    print()
    choice6 = input("You can try to fight the Satyr (F), bribe him (BR), or befriend him (BF).")

    # Player chooses to fight satyr
    if choice6 == 'F':
        StartBattle(user1, satyr)
        time.sleep(1)
        print()
        print("You killed him easily, but you missed out on a lot of valuable advice... After all, he had no weapon...")

    # Player chooses to bribe satyr
    elif choice6 == 'BR':
        print()
        print("I'm just trying to get through... How about we make a deal. I'll give you ¥200 and I'll be on my way.")
        print()
        print(
            "Satyr:\nYou insult me with your offer! I'd rather fight you than take such an insignificant sum from your grubby little hands! \nPay me more or prepare to fight me!")
        choice7 = input("Will you pay him more (P) or will you fight him (F)?")
        # Player additionally chooses to pay satyr more
        if choice7 == 'P':
            print()
            print("Fine, I'll give you ¥900 and no more! That's my limit!")
            # once you've given the satyr what he wants:
            print("Satyr:\nNow that's more like it!")
            print()
            print(
                "Excuse me, but there's just one more thing... Do you have any advice that you could give me before I continue on my quest...?")
            print()
            # If/When you ask the satyr for his advice:
            print("Satyr:\nNo. You didn't pay me for my advice... only for your safe passage. Keep it moving, kid!")
            user1.lost_money(900)
        # Player chooses to fight satyr without giving him extra money
        elif choice7 == "F":
            StartBattle(user1, satyr)
            time.sleep(3)
            print()
            print(
                "You killed him easily, but you missed out on a lot of valuable advice... After all, he had no weapon...")

    # Player chooses to become friend with satyr
    elif choice6 == "BF":
        print()
        print(
            "Listen, we're both human... sorta... why don't we help each other out... as friends. \nHelp me out on my quest and I'll give you something you want.")
        print()
        print("(Satyr is hesitating for {}'s unexpected proposal...".format(user1.nickname))
        print()
        Loading()
        time.sleep(3)
        print(
            "Satyr:\nI suppose that I could escort you for a little while, but you'll have to give me a 5% cut of all of your winnings from here on out for my company and for my guidance.\nDoes that sound good to you...?\n")
        print("(You nodded.)\n")
        print("Great! I promise you that you won't regret it!")

    # when typing error is occured
    else:
        print("An error has occured. Please try again.")
        Situation7(user1)
    Blank()


###Situation 8 (Keio Castle: King)
def Situation8(user1: User):  # Martin
    Long_loading()
    print(
        "You feel the ground shaking and you hear a booming, defeaning roar emanating from the deepest depths of the castle's dungeon... \nYou begin your descent down a stone staircase into the heart of darkness: the heart of the castle...")
    Loading()
    time.sleep(2)
    print("You finally reach the last step at the end of the stone staircase... It's freezing cold down here...")
    print()
    time.sleep(2)
    print("You find yourself standing in front of a giant wooden door with golden door handles...")
    print()
    time.sleep(2)
    print(
        "Inside of the room, you finally lay eyes on the tiny Evil King... by his side is a giant Hydra (like a dragon with three heads) that sits waiting for his commands.")
    print()
    time.sleep(2)
    print("Evil King:\nI'm surprised you have made it this far, boy...")
    print()
    time.sleep(1.5)
    print("{}:\nI came for my treasure and I'm not leaving without it!".format(user1.nickname))
    print()
    time.sleep(1.5)
    print("Evil King:\nWe will see about that... you will never get past my Hydra!")
    print("Hydra, attack him and make sure he doesn't survive!")
    print()
    time.sleep(1.5)
    print("The tiny King scurries away into the shadows, giggling...")
    print()
    print("The hydra stands up and starts walking towards you with its mouths open and ready to attack...!")
    hydra = Monster('hydra', 45, 20, hydra_weapon)
    time.sleep(3)
    choice8 = input(
        "Which head of the Hydra will you cut first... the left one (L), the middle one (M), or the right one (R)...?")

    while choice8 != 'R':
        print("You cut its head off and see the Hydra's body collapse to the floor.")
        time.sleep(1)
        print(
            "You think you've won until the Hydra stands up again only with two new heads that came out from the bloody stump of one of its severed necks.")
        time.sleep(1)
        print("You try to attack it, but it has too many heads and mouths for you to handle...")
        time.sleep(1)
        print(
            "The Hydra throws you up into the air and, without any chance for you to escape it, swallows you whole...")
        time.sleep(1)
        print("The tiny King giggles as he pets his Hydra on the head and leaves the room with your treasure.")
        print()
        print("Game over...")
        Long_loading()

        choice8 = input(
            "Which head of the Hydra will you cut first... the left one (L), the middle one (M), or the right one (R)...?")

    StartBattle(user1, hydra)
    print("You've beaten the Hydra...! The Evil King looks at you and then at its pet laying there, dead...")
    time.sleep(2)
    print("He screams in horror and kneels before you.")
    time.sleep(3)
    print()
    print()
    print("Evil King:\nPlease boy, don't kill me! Here, have your treasure and leave.")
    print("{} received a box with his treasure in!".format(user1.nickname))
    print()
    user_choice = input("Kill the evil king?(K) or let him run away? (R)")

    if user_choice == "K":
        print("{}:\nAfter all the bad deeds you have done, I cannot let you run away.".format(user1.nickname))
        print()
        time.sleep(2)
        print("{} has pierced him with his sword. Evil king screamed and turned into dust.".format(user1.nickname))
    else:
        print("{}:\nI'll let you run away this time. But don't you dare ever come back.".format(user1.nickname))
        print()
        print("Evil king ran away as quick as he can, looking somewhat funny.")

    Loading()
    print("{} opens his treasure box.\nNothing but a USB was inside the box.".format(user1.nickname))
    print()
    print("{}:\nMy valuable codes...\nFinally I can submit my final project to MR.Trovato!".format(user1.nickname))
    print("Phewwww... I was close to fail this class...")
    Blank()

    Long_loading()
    print("GM:\nYou've recovered your treasure and finished your quest!")
    time.sleep(2)
    print("Thank you so much! Because of you, we could submit our final project!!")
    time.sleep(2)
    print("Hope you enjoyed it. We wish you all good grades ^_^")
    Blank()
    print("                          <<< THE END >>>")