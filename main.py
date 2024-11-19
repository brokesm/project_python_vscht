from dungeon import Dungeon
import subprocess
import pickle

def load_game(import_saved):
    with open(f"{import_saved}",mode="rb") as file:
        file = pickle.load(file)
        for index,item in enumerate(file["current_map"]):
            file["current_map"][index] = list(map(lambda x: x.replace("@","."),item))
    return file


if __name__ == "__main__":
    dungeon: object
    hero_name = ""
    import_saved = input("Load game: ")
    
    
    if import_saved:
        imported_game = load_game(import_saved)
        hero_name = import_saved.split("_")[0]
        dungeon = Dungeon(imported_game=imported_game,load_import=True)
    else:
        hero_name = input("What is your name hero? ")
        dungeon = Dungeon(size=(10, 10), tunnel_number=40, hero_name=hero_name)


    while True:
        subprocess.Popen("cls", shell=True).communicate()
        print(dungeon)
        print(dungeon.message)
        action = input(f"Select an action {hero_name}: (L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, (S)AVE, (Q)UIT")
        if action == "Q":
            print("You coward!")
            exit(0)
        else:
            dungeon.hero_action(action)
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)
        if action == "S":
            dungeon.save_game()