from weapons_spells import *
from enemies import *

class Hero:
    """docstring for ClassName"""


    def __init__(self, name="Bron", title="Dragonslayer", health=100,
                 mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.count_hero_moves = 0
        self.weapon_used = None
        self.spell_used = None


    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def is_alive(self):
        return True if self.health > 0 else False

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return True if self.mana > 0 else False  # check to comply with cast minumum values

    def take_damage(self, damage_points):
        if self.health > damage_points:
            self.health -= damage_points
        else:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive():
            if healing_points + self.health > 100: # 100 is the initial health
                self.health = 100
            else:
                self.health += healing_points
        else:
            return False

    def take_mana(self, mana_points):
        if my_hero.is_alive():
            self.mana_regeneration_rate += mana_points
            if my_hero.mana_regeneration_rate > 100:
                my_hero.mana_regeneration_rate = 100

    def equip(self, weapon):
        self.weapon_used = weapon

    def learn(self, spell):
        self.spell_used = spell
    # attack method has not been tested
    
    def attack(self, by="weapon"):
        no_weapon = "Weapon not found"
        no_spell = "Spell not found"
        if by == "weapon":
            if self.weapon_used is None:
                print(no_weapon)
                return 0
                
            return self.weapon_used.get_damage()
        if by == "spell":
            if self.spell_used is None:
                print(no_spell)
                return 0
            if self.can_cast():
                self.mana -= self.spell_used.get_mana_cost()
                return self.spell_used.get_damage()
            return 0


my_hero = Hero()
# # print(my_hero.known_as())
# # print(my_hero.is_alive())
# my_hero.take_damage(99)
# print(my_hero.is_alive())
# # my_hero.take_damage(99)
# print(my_hero.is_alive())
# print(my_hero.health)
# my_hero.take_healing(40)
# print(my_hero.health)
# my_hero.take_healing(400)
# print(my_hero.health)

# print(my_hero.count_hero_moves)

print(my_hero.weapon_used)
my_hero.equip(my_weapon)
print(my_hero.weapon_used.name)

# print(my_hero.spell_used)
# my_hero.learn(my_spell)
# print(my_hero.spell_used.name)
#///////////////////////////////
# my_hero.attack(by="weapon")
