
import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        self.lowest_attack = self.attack_strength // 2
        self.attack_value = random.randint(self.lowest_attack, self.attack_strength)
        return self.attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_value.attack()

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.ability = ability
        self.abilities.append(ability)

    def attack(self):
        for ability in self.abilities:
            ability.attack()
            

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
