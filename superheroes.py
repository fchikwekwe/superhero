# /usr/bin/env python
# -*- coding: utf-8 -*-

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
    def __init__(self, name):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = start_health
        self.health = start_health
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
            self.attack_total += int(ability.attack())
        # return the total of all attacks
        return self.attack_total

    def defend(self):
        for armor in self.armors:

    def take_damage(self, damage_amt):
        if self.health <= 0:
            self.deaths += 1
        else:
            self.health -= self.damage_amt

    def add_kill(self, num_kills):
        self.kills += num_kills

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

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defense(self):
        self.defend = random.randint(0, self.defense)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
