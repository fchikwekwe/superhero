
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
    def __init__(self, name, health = 100):
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
            # if self.health > 0:
            total_defense += armor.defend()
            # else:
            #     total_defense = 0
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
        team_attack = 0
        for hero in self.heroes:
            team_attack += hero.attack()
        num_kills = other_team.defend(team_attack)

        for hero in self.heroes:
            hero.add_kill(num_kills)

    def deal_damage(self, damage):
        team_deaths = 0
        hero_damage = damage // len(self.heroes)
        for hero in self.heroes:
            if hero.health <= 0:
                hero.deaths += 1
                team_deaths += 1
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

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            print(hero.name)
            print(hero.kills / hero.deaths)

    def update_kills(self):
        for hero in self.heroes:
            hero.kills += self.kills
        return self.kills

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
        justice_league = ["Batman", "Wonder Woman", "The Flash", "Superman"]
        stark_family = ["Arya", "Jon Snow", "Ned's Head", "Three Eyed Raven"]
        normandy_crew = ["Commander Shepard", "Garrus", "Liara", "Tali'Zorah vas Normandy"]
        zoo_animals = ["African Elephant", "Boa Constrictor", "Deadly Penguin", "Harmless Lion"]

        self.team_one = Team("first_team")
        team_not_picked = True
        while team_not_picked:
            team_select = input("Please pick a your team from the following options: \n Enter '0' for The Justice League \n enter '1' for The Stark Family from Game of Thrones \n enter '2' for the crew of the Normandy from Mass Effect \n enter '3' for some feisty zoo animals. \n enter '4' to create your own team from scratch \n : ")
            if team_select == "0":
                self.team_one.name = "Justice League"
                self.team_one.heroes = justice_league
                team_not_picked = False
            elif team_select == "1":
                self.team_one.name = "The Stark Family"
                self.team_one.heroes = stark_family
                team_not_picked = False
            elif team_select == "2":
                self.team_one.name = "The Normandy Crew"
                self.team_one.heroes = normandy_crew
                team_not_picked = False
            elif team_select == "3":
                self.team_one.name = "Random Zoo Animals"
                self.team_one.heroes = zoo_animals
                team_not_picked = False
            elif team_select == "4":
                self.team_one.name = input("Name your team! \n: ")
                self.team_one.heroes = list()
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
            team_select = input("Please pick a your team from the following options: \n Enter '0' for The Avengers \n enter '1' for Daenerys and her dragons from Game of Thrones \n enter '2' for some late night comedians \n enter '3' for Disney Princesses. \n enter '4' to create your own team from scratch \n : ")
            if team_select == "0":
                self.team_two.name = "The Avengers"
                self.team_two.heroes = avengers
                team_not_picked = False
            elif team_select == "1":
                self.team_two.name = "Daenerys and her Dragons"
                self.team_two.heroes = daenerys_and_dragons
                team_not_picked = False
            elif team_select == "2":
                self.team_two.name = "Some Late Night Comedians"
                self.team_two.heroes  = late_night_comedians
                team_not_picked = False
            elif team_select == "3":
                self.team_two.name = "Disney Princesses"
                self.team_two.heroes = disney_princesses
                team_not_picked = False
            elif team_select == "4":
                self.team_two.name = input("Name Your Team! \n: ")
                self.team_two.heroes = list()
                team_not_picked = False
            else:
                print("Please pick a valid team option. ")

    def edit_team(self, team):
        team_not_edited = True
        while team_not_edited:
            print("Your team consists of ", team)
            add_remove = input("Would you like to add or remove any heroes from your team? \nType 'R' to remove, 'A' to add or 'N' if you do not want to change the composition of your team \n : ")
            if add_remove.lower() == 'r':
                number = str(len(team))
                remove = input("Please select the list number of the hero you would like to remove. You can select between 1 and " + number + ", respectively. \n : ")
                if remove.isdigit():
                    try:
                        team.pop(int(remove) - 1)
                    except IndexError:
                        print("Make sure your choice is between 0 and " + remove + ".")
                elif remove.isdigit() == False:
                    print("Please try again. ")
            elif add_remove.lower() == 'a':
                number = str(len(team))
                add = input("Please name the hero that you would like to add. \n : ")
                team.append(add)
            elif add_remove.lower() == 'n':
                team_not_edited = False
            else:
                print("Please provide a valid choice. ")

    def equip_heroes(self, team):
        for hero in team:
            hero = Hero(team[team.index(hero)])
            adding_abilities = True
            while adding_abilities:
                print(hero.name, "currently has the following abilities and weapons: ", hero.abilities)
                add_more = input("Would you like to add another ability or weapon to " + hero.name + " ? \n type 'Y' for yes or 'N' for no \n: ")
                if add_more.lower() == 'n' or add_more.lower() == 'no':
                    adding_abilities = False
                elif add_more.lower() == 'y' or add_more.lower() == 'yes':
                    ability = input("Name " + hero.name + "'s new ability or weapon \n: ")
                    hero.add_ability(ability)
                else:
                    print("Please select a valid option. ")
            for ability in hero.abilities:
                current_ability = hero.abilities[ability.index(ability)]
                print(hero.name, "currently has the following abilities and weapons: ", hero.abilities)
                add_power = True
                while add_power:
                    try:
                        power = input("How much power can " + current_ability + " dish out? \n:")
                    except ValueError:
                        print("Make sure your power level is a whole number.")
                        continue
                    if power.isdigit():
                        ability = Ability(current_ability, power)
                        print(ability.name, "currently deals", ability.attack_strength, "damage.")
                        add_power = False
                    else:
                        print("Please make sure your power level is a whole number. ")

            adding_armor = True
            while adding_armor:
                print(hero.name, "currently has the following armor: ", hero.armors)
                add_more = input("Would you like to add another piece of armor to " + hero.name + " ? \n type 'Y' for yes or 'N' for no \n: ")
                if add_more.lower() == 'n' or add_more.lower() == 'no':
                    adding_armor = False
                elif add_more.lower() == 'y' or add_more.lower() == 'yes':
                    armor = input("Name " + hero.name + "'s new armor \n: ")
                    hero.add_armor(armor)
                else:
                    print("Please select a valid option. ")
            for armor in hero.armors:
                current_armor = hero.armors[armor.index(armor)]
                print(hero.name, "currently has the following armor pieces: ", hero.armors)
                add_power = True
                while add_power:
                    try:
                        power = input("How much power can " + current_armor + " defend against? \n:")
                    except ValueError:
                        print("Please make sure your defense level is a whole number.")
                    if power.isdigit():
                        armor = Armor(current_armor, power)
                        print(armor.name, "currently protects against", armor.defense, "damage.")
                        add_power = False
                    else:
                        print("Please make sure your power level is a whole number. ")

    def show_stats(self):
        for hero in self.team_one:
            # attack(build_team_two) is kills / defend( build_team_one ) is deaths
            kill_death_ratio = int(attack(build_team_two) / defend(build_team_one))
            print("The kill to death ratio for {} is {}").format(hero.name, kill_death_ratio)
        for hero in self.team_two:
            kill_death_ratio = int(attack(build_team_one) / defend(build_team_two))
            print("The kill to death ratio for {} is {}").format(hero.name, kill_death_ratio)

    def fight(self):
        self.build_team_one()
        self.edit_team(self.team_one.heroes)
        self.build_team_two()
        self.edit_team(self.team_two.heroes)
        self.equip_heroes(self.team_one.heroes)


if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
#     print(hero.attack())
#     ability = Ability("Divine Speed", 300)
#     hero.add_ability(ability)
#     print(hero.attack())
#     new_ability = Ability("Super Human Strength", 800)
#     hero.add_ability(new_ability)
#     print(hero.attack())
    Arena().fight()
