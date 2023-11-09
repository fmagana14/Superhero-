import random
class armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value
    
if __name__ == "__main__":
        my_armor = armor("debugging shields", 10)
        print(my_armor.name)
        print(my_armor.block())