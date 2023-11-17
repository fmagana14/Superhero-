from superhero import Hero
from random import choice
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

        
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                    self.heroes.remove(hero)
                    foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
         for hero in self.heroes:
              print(hero.name)

    # def add_hero(self, hero):
         
    def stats(self):
         for hero in self.heroes:
              kd = hero.kills / hero.deaths
              print(f"{hero.name} Kill/Death:{kd}")

    def revive_hero(self, health=100):
         for hero in self.heroes:
              hero.current_health = health

    def attack(self, other_team):    
        living_heroes = list()
        living_opponent = list()
        for hero in self.heroes:
             living_heroes.append(hero)

        for hero in other_team.heroes:
             living_opponent.append(hero)   
             while len(living_heroes) > 0 and len(living_opponent)>0:
         
         
         
my_Team = Team("Aniheroes")

hero4 = Hero("Naruto")
hero5 = Hero("Killua")
hero6 = Hero("Toji")
my_Team.heroes.extend([hero4, hero5, hero6])

my_Team.view_all_heroes