from abstract_classes import AbstractDungeon
from copy import deepcopy
from map_entities import Hero, Goblin
import random
from brokesm_create_dungeon import MyDungeon
from datetime import datetime
import pickle

class Dungeon(AbstractDungeon):


    def __init__(self, imported_game={}, load_import=False, size=(), tunnel_number=1, hero_name=""):
        super().__init__(size,)
        self.imported_game = imported_game
        self.hero = Hero(name=hero_name) if not load_import else imported_game["hero"]
        self.tunnel_number = tunnel_number
        self.starting_entities = ["goblin", "goblin", "goblin", "goblin","goblin"] if not load_import else imported_game["starting_entities"]
        self.entities = [] if not load_import else imported_game["remaining_entities"]
        self.empty_space = []
        self.message = ""
        self.create_dungeon() if not imported_game else self.import_dungeon()



    def __str__(self):
        printable_map = ""
        for row in self.current_map:
            for column in row:
                printable_map += column
            printable_map += "\n"
        return printable_map
    


    def import_dungeon(self):
        self.dungeon_map = self.imported_game["current_map"]
        self.import_entities()
        self.current_map = deepcopy(self.dungeon_map)
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier



    def create_dungeon(self):
        new_dungeon = MyDungeon(self.size[0],self.size[1])
        self.dungeon_map = new_dungeon.generateDungeon(self.tunnel_number)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.dungeon_map[x][y] != "▓" and (x,y) != (1,1):
                    self.empty_space.append(tuple([x, y]))
        self.place_entities(self.starting_entities)
        self.current_map = deepcopy(self.dungeon_map)
        self.empty_space = list(map(list,set(self.empty_space)))
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier



    def hero_action(self, action):
        if action == "R":
            # if self.hero.position[1] + 1 < self.size[1] - 1:
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] + 1] != "▓":
                self.hero.position[1] += 1
        elif action == "L":
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] - 1] != "▓":
                self.hero.position[1] += -1
        elif action == "U":
            if self.dungeon_map[self.hero.position[0] - 1][self.hero.position[1]] != "▓":
                self.hero.position[0] += -1
        elif action == "D":
            if self.dungeon_map[self.hero.position[0] + 1][self.hero.position[1]] != "▓":
                self.hero.position[0] += 1
        elif action == "A":
            fighting = False
            for entity in self.entities:
                if tuple(self.hero.position) == entity.position:
                    if hasattr(entity, "attack"):
                        self.fight(entity)
                        fighting = True
            if not fighting:
                self.message ="Your big sword is hitting air really hard!"

        self.update_map(self.entities)

        if self.hero.hp < 1:
            self.message += "\nTHIS IS THE END"



    def import_entities(self):
        for entity in self.entities:
            self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier



    def place_entities(self, entities: list):
        position = random.sample(self.empty_space, len(entities))
        for idx, entity in enumerate(self.starting_entities):
            if entity == "goblin":
                self.entities.append(Goblin(identifier="\033[38;5;1mg\033[0;0m",
                                            position=position[idx], base_attack=-1,
                                            base_ac=0, damage=1))
        for entity in self.entities:
            self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier



    def update_map(self, entities: list):
        # TODO implement entities
        self.current_map = deepcopy(self.dungeon_map)
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier



    def fight(self, monster):
        hero_roll = self.hero.attack()
        monster_roll = monster.attack()
        if hero_roll["attack_roll"] > monster.base_ac:
            monster.hp -= hero_roll["inflicted_damage"]
            if monster.hp > 0:
                self.message = f"{self.hero.name} inflicted {hero_roll['inflicted_damage']} damage"
            else:
                self.message = f"{self.hero.name} inflicted {hero_roll['inflicted_damage']} damage and slain {monster}"
                self.hero.gold += monster.gold
                self.hero.xp += 1
                self.dungeon_map[monster.position[0]][monster.position[1]] = "."
                self.entities.remove(monster)
                self.starting_entities.remove("goblin")
        if monster_roll["attack_roll"] > self.hero.base_ac:
            self.message += f"\nMonster inflicted {monster_roll['inflicted_damage']} damage"
            self.hero.hp -= monster_roll['inflicted_damage']
            if self.hero.hp < 1:
                self.message += f"{self.hero.name} have been slained by {monster}"
        self.message += f"\n{self.hero.name} HP: {self.hero.hp}  Monster HP: {monster.hp}"


    def save_game(self):
        saved_progress = {
                "hero": self.hero,
                "remaining_entities":self.entities,
                "starting_entities":self.starting_entities,
                "current_map":self.current_map
            }
        with open(f"{self.hero.name}_{datetime.now().timestamp()}.dng",mode="wb") as saved_game:
            pickle.dump(saved_progress,saved_game)
            self.message += "\nGame saved!"

        
        