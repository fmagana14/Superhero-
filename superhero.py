import random
class hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self,opponent):   
     heroes = [self, opponent]

     winner_display = random.randint (0,1)
     winner = heroes[winner_display]
     loser = heroes[1 - winner_display]
     print(f"{winner.name} defeated {loser.name}! {winner.name} Wins!")

if __name__ == "__main__":
        hero1 = hero("Luminaflare", 250)
        hero2 = hero("Bolt", 200)

        print(hero1.name)
        print(hero1.current_health)
        print(hero2.name)
        print(hero2.current_health)

        hero1.fight(hero2)