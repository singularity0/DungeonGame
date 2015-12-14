class Hero():
    """docstring for ClassName"""
    def __init__(self, name="Bron", title="Dragonslayer", health=100,
                 mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

my_hero = Hero()
print(my_hero.known_as())
 