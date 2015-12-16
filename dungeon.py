# from map import *

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
        pass

    def learn(spell):
        pass

    def attack():
        pass

    def some_stupid(self):
        pass



# my_hero = Hero()
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
