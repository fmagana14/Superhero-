from random import randint
from abilities import ablility
class Weapon (ablility):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        random_value = randint((self.max_damage//2), self.max_damage)
        return random_value

      
      
        # half_max_damage = self.max_damage // (2) 
        # return random.randint(half_max_damage, self.max_damage)
