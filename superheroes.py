
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
        self.team_one = list()
        self.team_two = list()

    def build_team_one(self):

    def build_team_two(self):

    def team_battle(self):

    def show_stats(self):


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
