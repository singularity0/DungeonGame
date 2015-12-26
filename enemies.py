class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        return True if self.health > 0 else False

    def can_cast(self):
        pass

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.is_alive():
            if healing_points + self.health > 100:
                self.health = 100
            else:
                self.health += healing_points
        else:
            return False

    def take_mana(self, mana_points):
        if self.is_alive():
            if mana_points + self.mana > 100:
                self.mana = 100
            else:
                self.mana += mana_points
        else:
            return False

    def take_damage(self, damage_points):
        if self.health > damage_points:
            self.health -= damage_points
        else:
            self.health = 0

    def attack(self):
        pass

# enemy = Enemy(health=10, mana=20)
"""print(enemy.is_alive())
print(enemy.health)
print(enemy.take_healing(30))
print(enemy.health)
print(enemy.take_healing(80))
print(enemy.take_damage(45))
print(enemy.health)
print(enemy.take_damage(55))
print(enemy.health)
print(enemy.take_mana(30))
print(enemy.mana)"""
# print(enemy.get_health())
# print(enemy.get_mana())