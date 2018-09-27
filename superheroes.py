
import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # calculate lowest attack value as integer
        self.lowest_attack = self.attack_strength // 2
        # select random attack value
        self.attack_value = random.randint(self.lowest_attack, self.attack_strength)
        # return attack value
        return self.attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # self.ability = ability
        self.abilities.append(ability)

    def attack(self):
        # total of all attacks
        self.attack_total = 0
        # call the attack method on every ability in list
        for ability in self.abilities:
            # add up all of the attacks
            self.attack_total += Ability.attack(ability)
        # return the total of all attacks
        return self.attack_total

    def defend(self):
        total_defense = 0
        # run the defend method on each piece of armor and calculate the total defense
        for armor in self.armors:
            total_defense += armor.defend()
        return total_defense

    def take_damage(self, damage_amt):
        if self.health <= 0:
            self.deaths += 1
        elif self.health <= damage_amt:
            self.health -= self.damage_amt
            self.deaths += 1
        else:
            self.health -= self.damage_amt

    def add_kill(self, num_kills):
        self.kills += num_kills


    def add_armor(self, armor):
        self.armors.append(armor)

class Weapon(Ability):
    def attack(self):
        self.lowest_attack = 0
        self.attack_value = random.randint(self.lowest_attack, self.attack_strength)
        return self.attack_value

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                index_num = self.heroes.index(hero)
                self.heroes.pop(index_num)
            else:
                pass
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        if len(self.heroes) == 0:
            return None
        else:
            for hero in self.heroes:
                print(hero.name)

    def attack(self, other_team):
        # create a variable to track total team damage
        team_attack = 0
        # print off each hero's name
        hero_names = [hero.name for hero in self.heroes]
        print(self.name, "currently contains", hero_names)
        # go to each hero object in our list of hero objects
        for hero in self.heroes:
            # get the attack value from the hero and add it to total team attack
            team_attack += hero.attack()
            # print("team attack after each hero:", team_attack)
        # create a variable that store the total kills based on the other team's defense
        # the kill needs to only be recorded for the hero that did the damage
        # need to check each hero
        num_kills = other_team.defend(team_attack)
        print("team: {} num_kills: {}".format(self.name, num_kills))
        for hero in self.heroes:
            hero.add_kill(num_kills)

    def deal_damage(self, damage):
        team_deaths = 0
        hero_damage = damage // len(self.heroes)
        for hero in self.heroes:
            if hero.health <= 0:
                pass
            elif hero.health <= hero_damage:
                hero.health -= hero_damage
                hero.deaths += 1
                team_deaths += 1
            elif hero.health > hero_damage:
                hero.health -= hero_damage
            else:
                hero.health -= hero_damage
        return team_deaths

    def defend(self, damage_amt):
        team_defense = 0
        for hero in self.heroes:
            team_defense += hero.defend()
        excess_damage = damage_amt - team_defense
        if excess_damage <= 0:
            return 0
        else:
            return self.deal_damage(excess_damage)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0:
                print("Team: {}; Hero: {}; Kill/Death Ratio: {}; deaths: {}; kills: {}".format(self.name, hero.name, hero.kills/hero.deaths, hero.deaths, hero.kills))
            else:
                print("Team: {}; Hero: {}; deaths: 0; kills: {}".format(self.name, hero.name, hero.kills))

    def update_kills(self):
        for hero in self.heroes:
            team_kills += hero.kills
        return team_kills

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        defend = random.randint(0, self.defense)
        return defend

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        # premade teams to choose from
        justice_league = ["Batman", "Wonder Woman", "The Flash", "Superman"]
        stark_family = ["Arya", "Jon Snow", "Ned's Head", "Three Eyed Raven"]
        normandy_crew = ["Commander Shepard", "Garrus", "Liara", "Tali'Zorah vas Normandy"]
        zoo_animals = ["African Elephant", "Boa Constrictor", "Deadly Penguin", "Harmless Lion"]

        self.team_one = Team("first_team")
        # team select
        team_not_picked = True
        while team_not_picked:
            team_select = input("Please pick your team from the following options: \n Enter '0' for The Justice League \n enter '1' for The Stark Family from Game of Thrones \n enter '2' for the crew of the Normandy from Mass Effect \n enter '3' for some feisty zoo animals \n enter '4' to create your own team from scratch \n : ")
            if team_select == "0":
                self.team_one.name = "Justice League"
                for leaguer in justice_league:
                    hero = Hero(leaguer)
                    self.team_one.add_hero(hero)
                team_not_picked = False
            elif team_select == "1":
                self.team_one.name = "The Stark Family"
                for stark in stark_family:
                    hero = Hero(stark)
                    self.team_one.add_hero(hero)
                team_not_picked = False
            elif team_select == "2":
                self.team_one.name = "The Normandy Crew"
                for being in normandy_crew:
                    hero = Hero(being)
                    self.team_one.add_hero(hero)
                team_not_picked = False
            elif team_select == "3":
                self.team_one.name = "Random Zoo Animals"
                for animal in zoo_animals:
                    hero = Hero(animal)
                    self.team_one.add_hero(hero)
                team_not_picked = False
            elif team_select == "4":
                self.team_one.name = input("Name your team! \n: ")
                for one in self.team_one.heroes:
                    hero = Hero(one)
                    self.team_one.add_hero(hero)
                team_not_picked = False
            else:
                print("Please pick a valid team option. ")

    def build_team_two(self):
        avengers = ["Captain America", "Black Panther", "Iron Man", "Thor"]
        daenerys_and_dragons = ["Daenerys Targaryen", "Drogon", "Rhaegal", "Viserion"]
        late_night_comedians = ["John Oliver", "Trevor Noah", "Jimmy Kimmel", "Steven Colbert"]
        disney_princesses = ["Mulan", "Pocahontas", "Jasmine", "Moana"]

        self.team_two = Team("second_team")
        team_not_picked = True
        while team_not_picked:
            team_select = input("Please pick your team from the following options: \n Enter '0' for The Avengers \n enter '1' for Daenerys and her dragons from Game of Thrones \n enter '2' for some late night comedians \n enter '3' for Disney Princesses \n enter '4' to create your own team from scratch \n : ")
            if team_select == "0":
                self.team_two.name = "The Avengers"
                for avenger in avengers:
                    hero = Hero(avenger)
                    self.team_two.add_hero(hero)
                team_not_picked = False
            elif team_select == "1":
                self.team_two.name = "Daenerys and her Dragons"
                for dragonborn in daenerys_and_dragons:
                    hero = Hero(dragonborn)
                    self.team_two.add_hero(hero)
                team_not_picked = False
            elif team_select == "2":
                self.team_two.name = "Some Late Night Comedians"
                for comedian in late_night_comedians:
                    hero = Hero(comedian)
                    self.team_two.add_hero(hero)
                team_not_picked = False
            elif team_select == "3":
                self.team_two.name = "Disney Princesses"
                for princess in disney_princesses:
                    hero = Hero(princess)
                    self.team_two.add_hero(hero)
                team_not_picked = False
            elif team_select == "4":
                self.team_two.name = input("Name Your Team! \n: ")
                for one in self.team_two.heroes:
                    hero = Hero(one)
                    self.team_two.add_hero(Hero)
                team_not_picked = False
            else:
                print("Please pick a valid team option. ")

    def edit_team(self, team):
        # allow changes to team comp
        team_not_edited = True
        while team_not_edited:
            for x in team.heroes:
                print(x.name, "is on your team!")
            add_remove = input("Would you like to add or remove any heroes from your team? \nType 'R' to remove, 'A' to add or 'N' if you do not want to change the composition of your team \n : ")
            if add_remove.lower() == 'r':
                number = str(len(team.heroes))
                remove = input("Please select the list number of the hero you would like to remove. You can select between 1 and " + number + ", respectively. \n : ")
                if remove.isdigit():
                    try:
                        team.heroes.pop(int(remove) - 1)
                    except IndexError:
                        print("Make sure your choice is between 0 and " + remove + ".")
                elif remove.isdigit() == False:
                    print("Please try again. ")
                    # fix adding object not string
            elif add_remove.lower() == 'a':
                number = str(len(team.heroes))
                add = input("Please name the hero that you would like to add. \n : ")
                hero = Hero(add)
                team.add_hero(hero)
            elif add_remove.lower() == 'n':
                team_not_edited = False
            else:
                print("Please provide a valid choice. ")

    def add_ability(self, fighter):
        ability_list = [ability.name for ability in fighter.abilities]
        print(fighter.name, "currently has: ", ability_list, "in weapon/ability loadout.")
        adding_abilities = True
        while adding_abilities:
            add_more = input("Would you like to add another ability or weapon to " + fighter.name + " ? \n type 'Y' for yes or 'N' for no \n: ")
            if add_more.lower() == 'n' or add_more.lower() == 'no':
                adding_abilities = False
            elif add_more.lower() == 'y' or add_more.lower() == 'yes':
                ability_input = input("Name " + fighter.name + "'s new ability or weapon \n: ")
                try:
                    power = input("How much power can " + ability_input + " dish out? \n:")
                    add_power = True
                    while add_power:
                        if power.isdigit():
                            print("This power can deal up to", power , "damage.")
                            add_power = False
                        else:
                            print("Please make sure your max power level is a whole number. ")
                except ValueError:
                    print("Make sure your power level is a whole number.")
                ability = Ability(ability_input, int(power))
                fighter.add_ability(ability)
            else:
                print("Please select a valid option. ")

    def add_armor(self, fighter):
            armor_list = [armor.name for armor in fighter.armors]
            print(fighter.name, "currently has: ", armor_list, "in armor loadout.")
            adding_armor = True
            while adding_armor:
                add_more = input("Would you like to add another armor to " + fighter.name + " ? \n type 'Y' for yes or 'N' for no \n: ")
                if add_more.lower() == 'n' or add_more.lower() == 'no':
                    adding_armor = False
                elif add_more.lower() == 'y' or add_more.lower() == 'yes':
                    armor_input = input("Name " + fighter.name + "'s new armor \n: ")
                    try:
                        power = input("How much power can " + armor_input + " protect against? \n:")
                        add_power = True
                        while add_power:
                            if power.isdigit():
                                print("This armor currently defends against", power , "damage.")
                                add_power = False
                            else:
                                print("Please make sure your armor level is a whole number. ")
                    except ValueError:
                        print("Make sure your armor level is a whole number.")
                    armor = Armor(armor_input, int(power))
                    fighter.add_armor(armor)
                else:
                    print("Please select a valid option. ")

    def equip_heroes(self, team):
        for fighter in team.heroes:
            self.add_ability(fighter)
            self.add_armor(fighter)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

    def fight(self):
        game_is_running = True
        while game_is_running:
            self.build_team_one()
            self.edit_team(self.team_one)
            self.build_team_two()
            self.edit_team(self.team_two)
            self.equip_heroes(self.team_one)
            self.equip_heroes(self.team_two)

            coin_flip = random.randint(1, 2)
            print("Coin flip selects team", coin_flip)
            if coin_flip == 1:
                hero_health = 0
                for hero in self.team_one.heroes:
                    hero_health += hero.health

                print("{} goes first!".format(self.team_one.name))
                self.team_one.attack(self.team_two)

                if hero_health > 0:
                    self.team_two.attack(self.team_one)
                else:
                    pass
                print("{} have died! Stats are listed below!".format(self.team_two.name))

            else:
                hero_health = 0
                for hero in self.team_two.heroes:
                    hero_health += hero.health

                print("{} goes first!".format(self.team_two.name))
                self.team_two.attack(self.team_one)

                if hero_health > 0:
                    self.team_one.attack(self.team_two)
                else:
                    pass
                print("{} has died! Stats are listed below!".format(self.team_one.name))

            self.show_stats()
            decide_to_play = True
            while decide_to_play:
                play_again = input("Would you like to battle again? Type 'Y' for yes or 'N' for no \n : ")
                if play_again.lower() == 'n':
                    print("Thanks for playing!")
                    game_is_running = False
                    decide_to_play = False
                elif play_again.lower() == 'y':
                    self.team_one.revive_heroes()
                    self.team_two.revive_heroes()
                    decide_to_play = False
                else:
                    print("Please pick a valid option!")


if __name__ == "__main__":
    # hero = Hero("Wonder Woman")
    # ability = Ability("Divine Speed", 300)
    # hero.add_ability(ability)
    #
    # other_hero = Hero("Flash")
    # other_ability = Ability("Super Fast", 200)
    # other_hero.add_ability(other_ability)
    #
    # # print(hero.attack())
    # # print(hero.attack())
    # # new_ability = Ability("Super Human Strength", 800)
    # # hero.add_ability(new_ability)
    # # print(hero.attack())
    #
    # team = Team("Test Team")
    # team.add_hero(hero)
    #
    # other_team = Team("Other Test Team")
    # other_team.add_hero(other_hero)
    #
    # # print(other_team)
    # # print(team)
    #
    # # team.attack(other_team)


    Arena().fight()
