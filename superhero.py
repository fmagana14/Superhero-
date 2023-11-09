import random
from abilities import ablility
from armor import Armor
class hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.armor = []
        self.abilities = list()
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_ability(self, ability):
        #  add abilities here
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

    
    def fight(self,opponent):   
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while opponent.current_health > 0 and self.current_health > 0:
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

                else:
                    # add kill to self
                    self.kills += 1
                    # add death to oponent
                    opponent.deaths += 1
                    #print who won
                    print(f"{self.name} Has won!")
                    

                    
    #  heroes = [self, opponent]

    # #  if ablility == 0:
    # #     print("Draw")
    # #  else: 

    #  winner_display = random.randint (0,1)
    #  winner = heroes[winner_display]
    #  loser = heroes[1 - winner_display]
    #  print(f"{winner.name} defeated {loser.name}! {winner.name} Wins!")

    def is_alive(self):
        if self.current_health <= 0:
            return False 
        else:
            return True


if __name__ == "__main__":
        hero1 = hero("Luminaflare", 250)
        ablility1 = ablility("blazing rush", 50)
        hero1.add_ability(ablility1)
        armor1 = Armor("balistic shield", 40)
        hero1.add_armor(armor1)


        hero2 = hero("Bolt", 200)
        ablility2 = ablility("super flash", 50)
        hero2.add_ability(ablility2)
        armor2 = Armor("body shield", 60)
        hero2.add_armor(armor2)


        # print(hero1.name)
        # print(hero1.current_health)
        # print(hero2.name)
        # print(hero2.current_health)
        # print(hero1.abilities)
        # print(hero1.attack())
        # print(hero1.is_alive())
        # print(hero2.is_alive())


        hero1.fight(hero2)