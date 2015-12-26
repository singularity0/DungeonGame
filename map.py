from dungeon import Hero

class Dungeon:


    def __init__(self, map):
        self.map = map

    @staticmethod
    def create_from_file(path):
        dungeon = []
        with open(path, "r") as f:
            contents = f.read().split("\n")
            dungeon = [list(line) for line in contents if line.strip() != ""]
        return Dungeon(dungeon)

    def print_map(self):
        for row in self.map:
            print(row)

    def spawn(self, hero):
        for line in self.map:
            for char in line:
                if char == 'S':
                    index = line.index(char)
                    # print(index)
                    line[index] = 'H'
                    return True

        return False

    def hero_location(self):
        for line in range(0, len(self.map)):
            for char in range(0, len(self.map[line])):
                if self.map[line][char] == 'H':
                    index_hero = (line, char)
                    print(index_hero)
        # print(len(self.map))
        # print(len())

    def move_hero(self, direction):
        if my_hero.is_alive():
            my_hero.mana_regeneration_rate += 2
            if my_hero.mana_regeneration_rate > 100:
                my_hero.mana_regeneration_rate = 100

        pass



map = Dungeon.create_from_file("level1.txt")
# map.print_map()
# print(map.map)
# map.spawn(1)
# map.print_map()
# map.hero_location()

my_hero = Hero()
# print(my_hero.known_as())
# print(my_hero.is_alive())
my_hero.take_damage(99)
print(my_hero.is_alive())
# my_hero.take_damage(99)
print(my_hero.is_alive())
print(my_hero.health)
my_hero.take_healing(40)
print(my_hero.health)
my_hero.take_healing(400)
print(my_hero.mana_regeneration_rate)
map.move_hero('dd')
print(my_hero.mana_regeneration_rate)