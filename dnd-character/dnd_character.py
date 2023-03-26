import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitution_modifier = modifier(self.constitution)
        self.hitpoints = self.constitution_modifier + 10
    
    def ability(self):
        random_array = [random.randint(1,6) for int in range(4)]
        random_array.sort()
        return sum(random_array[1:4])

def modifier(score):
    return (score - 10)//2