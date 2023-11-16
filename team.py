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

    def add_hero(self, hero):
         
my_Team = Team("Aniheroes")

hero4 = Hero("Naruto")
hero5 = Hero("Killua")
hero6 = Hero("Toji")
my_Team.heroes.extend([hero4, hero5, hero6])

my_Team.view_all_heroes