class Weapon:
    def __init__(self, name='The Axe of Destiny',
                 damage=20):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage


class Spell:
    def __init__(self, name='Fireball', damage=30,
                 mana_cost=50, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cost_range(self):
        return self.cast_range




my_weapon = Weapon("Deadly axe", 30)
# print(my_weapon.name)
my_spell = Spell("Iceball")
# print(my_spell.mana_cost)
# print(my_spell.get_damage())