"""Simulate a dungeon crawler with procedurally generated rooms, combat, and loot collection"""
"test commit"
import data

class Character:
    def __init__(self, health):
        self.health = health
    

class Player(Character):
    
    def __init__(self, health, character_class, player_name, dodge_chance):
        super().__init__(health)
        self.character_class = character_class
        self.player_name = player_name
        self.row_pos = 3
        self.col_pos = 3
        self.dodge_chance = dodge_chance
        self.weapon = None

class Weapon():
    def __init__(self, weapon_name, heavy_damage, light_damage):
        self.weapon_name = weapon_name
        self.heavy_damage = heavy_damage
        self.light_damage = light_damage
        
    #Will have attack methods for both light and heavy with flavor text
    
    
def create_player():
    
    name = input("After days following the ragged map given you "
                 "by a mysterous man in a tavern, you finally find yourself at "
                 "the entrance of a decrepit dungeon. /nWhat is your name? ")
    
    player_class = "0"
    
    while player_class not in ["1", "2", "3"]:
        player_class = input(f"Very well, {name}. What is your background?.\n"
                            "1. A warrior, veteran of the Great War.\n"
                            "2. A mage, graduate of The Arcane Institute.\n"
                            "3. A thief, legend of the underworld\n")
    
    if player_class == "1":
        player = Player(150, "Warrior", name, 10)
        player.weapon = Weapon("Battleaxe", 65, 35)
        
    elif player_class == "2":
        player = Player(100, "Mage", name, 20)
        player.weapon = Weapon("Grand Staff", 50, 25)
    else:
        player = Player(75, "Thief", name, 65)
        player.weapon = Weapon("Obsidian Dagger", 35, 15)
    
    print(f"After a moment of contemplation, {player.player_name} "
          f"the {player.character_class} enters the dungeon.")
    
    return player
    
        
        
        
    

def display_dungeon_map(player):
    """
    This function displays a 5x5 dungeon room layout with the player position
    The coords must be in proper range (0-4) when they sent to the function.
    It is assumed that when the player chooses to move rooms (forwards, left
    right, backwards) they will only be able to choose valid moves. EX: when at
    the left wall bottom corner (4, 0), left and backwards will not be allowed.
    Just using this as an example for now, this could be used if the player
    decides to use a map while outside of an event.
    
    A possible change here is to have the players coords in a list [x,y] as an
    instance variable, and only pass the player object into the function. 
    """
    
    map = [
    ["\u25A0\t", "\u25A0\t", "\u25A0\t","\u25A0\t"],
    ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"],
    ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"],
    ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"]
    ]
    
     #boss room symbol
    map[0][0] = "\u2620\t"
    #setting player symbol at the proper coordinates
    map[player.row_pos][player.col_pos] = "\u25CB\t"
   
    
    print("\n----Map Of The Dungeon----")
    for row in map:
        for item in row:
            print(item, end= " ")
        print("\n")

        
def boss_access_attempt():
    
    code = "ABCD"
    
    guess = input("You stand upon a massive door. A plaque says "
                "'Ye who dare enter must speak the words of Ragnaric.' "
                "You choose to say: ")

    if guess == code:
        print("As you speak these words, the mighty door swings open. " 
              f"You are in {data.rooms[0,0]}")
        return True
    else:
        print("Nothing happened... "
        "It seems you must figure out what to say first.")
        return False
    
    
def player_move(player):
    
    move_accepted = False
    
    while (not move_accepted):
        
        move_direction = input("Choose a direction to move in (w,a,s,d): ")
        
        if move_direction.lower() not in ["w", "a", "s", "d"]:
            print("Invalid direction!")
        
        
        #FORWARD
        if move_direction == "w":
            #If at top wall already, cannot move forwards
            if (player.row_pos == 0):
    
                print("you slam your face into a wall... "
                      "it seems this is as far forward as you can go.")
                
            #Attempt to enter boss room    
            elif (player.row_pos == 1 and player.col_pos == 0):
                
                answer = boss_access_attempt()
                
                if answer == True:
                    player.row_pos -= 1
                    move_accepted = True
                    
                else: 
                    continue
                
            #Valid move
            else:
                player.row_pos -= 1
                print("You walk forwards through a door and find "
                      f"yourself in the {data.rooms[(player.row_pos, player.col_pos)]}")
                move_accepted = True
                
                
        #LEFT     
        if move_direction == "a":
            #If at the left wall already, you cannot progress
            if (player.col_pos == 0):
                
                print("you slam your face into a wall... "
                      "it seems this is as far left as you can go.")
            
            #Attempt to enter boss room
            elif (player.row_pos == 0 and player.col_pos == 1):
                
                answer = boss_access_attempt()
                
                if answer == True:
                    player.col_pos -= 1
                    move_accepted = True
                    
                else:
                    continue
                
            #Valid move
            else:
                player.col_pos -= 1
                print("You walk to your left through a door and find "
                      f"yourself in the {data.rooms[(player.row_pos, player.col_pos)]}")
                move_accepted = True
        #DOWN
        if move_direction == "s":
            #Barrier of map
            if (player.row_pos == 3):
                
                print("you slam your face into a wall... "
                      "it seems this is as far backwards as you can go.")
            #Valid move
            else:
                player.row_pos += 1
                print("You walk backwards through a door and find "
                      f"yourself in the {data.rooms[(player.row_pos, player.col_pos)]}")
                move_accepted = True
        #RIGHT
        if move_direction == "d":
            #Barrier of map
            if (player.col_pos == 3):
                
                print("you slam your face into a wall... "
                      "it seems this is as far right as you can go.")
            #Valid move
            else:
                player.col_pos += 1
                print("You walk to your right through a door and find "
                      f"yourself in the {data.rooms[(player.row_pos, player.col_pos)]}")
                move_accepted = True

        
    
player = create_player()

for i in range(9):
    display_dungeon_map(player)
    player_move(player)
