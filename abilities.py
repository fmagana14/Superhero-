import random
class ablility:
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value
if __name__ == "__main__":
    ablility = ablility("debugging abilities", 20)
    print(ablility.name)
    print(ablility.attack())

