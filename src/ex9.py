import random


def fight(character):
    random_number = random.randint(1, 20)
    character.hit_points -= random_number
    if character.hit_points <= 0:
        character.hit_points = "You have 0 hit points left. Game over!."


class Character:
    def __init__(self, hit_points):
        self.hit_points = hit_points


class Fighter(Character):
    def __repr__(self):
        return f"Fighter: {self.hit_points} hit points."


class Dwarf(Character):
    def __repr__(self):
        return f"Dwarf: {self.hit_points} hit points."


f = Fighter(18)
d = Dwarf(15)
print(f)
print(d)
fight(d)
fight(f)
print(f)
print(d)
