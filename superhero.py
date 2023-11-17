import random
from abilities import ablility
from armor import Armor
from weapon import Weapon
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.armor = []
        self.abilities = list()
        self.weapon = [] 
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def fight(self, opponent):   
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                attack1 = self.attack()
                opponent.take_damage(attack1)

                attack2 = opponent.attack()
                self.take_damage(attack2)

                # if not self.is_alive():


                # output -> False

                if not self.is_alive():
                    opponent.kills += 1
                    # add kill to oponent
                    self.deaths += 1
                    # add death to self 
                    print(f"{opponent.name} Has won!")
                    # print who won 
                    break

                else:
                    # add kill to self
                    self.kills += 1
                    # add death to oponent
                    opponent.deaths += 1
                    #print who won
                    print(f"{self.name} Has won!")
                    break

    def attack(self):
        total_damage = 0
        for ability in self.abilities:  
            total_damage += ability.attack()
            return total_damage
    # def attack(self):
    #     total_damage = 0
    #     for ability in self.abilities:
    #         if isinstance(ability, Weapon):
    #             total_damage += ability.attack()
    #         else:
    #             total_damage += random.randint(ability.max_damage // 2, ability.max_damage)
    #     return total_damage 


#  add abilities here
    def add_ability(self, ability):
         self.abilities.append(ability)

    def defense(self):
        total_armor = 0
        for armor in self.armor:
            total_armor += armor.block()
        return total_armor

    def add_armor(self, armor):
        self.armor.append(armor)

    def take_damage(self, damage):
        defended = damage - self.defense()
        if defended >= 0:
            self.current_health -= defended

    def add_weapon(self, weapon):   
        self.abilities.append(weapon)
    # def deal_damage(self, damage):


    def is_alive(self):
        if self.current_health <= 0:
            return False 
        else:
            return True
    
    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deths):
        self.deaths += num_deths
        pass


if __name__ == "__main__":
       
    hero1 = Hero("Luminaflare", 250)
    ablility1 = ablility("blazing rush", 50)
    hero1.add_ability(ablility1)    
    armor1 = Armor("balistic shield", 40)
    hero1.add_armor(armor1)
    weapon1 = Weapon("sword strike", 65)
    hero1.add_weapon(weapon1)

    hero2 = Hero("Bolt", 200)
    ablility2 = ablility("super flash", 50)
    hero2.add_ability(ablility2)
    armor2 = Armor("body shield", 60)
    hero2.add_armor(armor2)
    weapon2 = Weapon("staff strike", 80)
    hero2.add_weapon(weapon2)
   
    hero1.fight(hero2)
    
    hero3 = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero3.add_weapon(weapon)
    print(hero3.attack())


        # hero1 = hero("Luminaflare", 250)
        # ablility1 = ablility("blazing rush", 50)
        # hero1.add_ability(ablility1)
        # armor1 = Armor("balistic shield", 40)
        # hero1.add_armor(armor1)
        # weapon1 = Weapon("sword strike", 65)
        # hero1.add_weapon(weapon1)


        # hero2 = hero("Bolt", 200)
        # ablility2 = ablility("super flash", 50)
        # hero2.add_ability(ablility2)
        # armor2 = Armor("body shield", 60)
        # hero2.add_armor(armor2)
        # weapon2 = Weapon("staff strike", 80)
        # hero2.add_weapon(weapon2)



# could not get terminal to display any number between 40-80