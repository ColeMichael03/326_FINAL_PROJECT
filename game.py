"""Simulate a dungeon crawler with prodecurally generated rooms, combat, and loot collection"""
"test commit"


class Character:
    def __init__(self, health):
        self.health = health
    

class Player(Character):
    
    def __init__(self, health, character_class):
        super().__init__(health)
        self.character_class = character_class
        self.row_pos = 3
        self.col_pos = 3
        self.weapon = None
    

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
    
    #setting player symbol at the proper coordinates
    map[player.row_pos][player.col_pos] = "\u25CB\t"
    #boss room symbol
    map[0][0] = "\u2620\t"
    
    print("\n----Map Of The Dungeon----")
    for row in map:
        for item in row:
            print(item, end= " ")
        print("\n")

        
def boss_access_attempt():
    
    code = "ABCD"
    
    guess = input("You stand upon a massive door. A plaque says 'Ye who dare enter must speak the words of Ragnaric.'\nYou choose to say: ")

    if guess == code:
        return True
    else:
        return False
    
    
def player_move(player):
    
    move_accepted = False
    
    while (not move_accepted):
        
        move_direction = input("Chose direction to move in (w,a,s,d): ")
        
        if move_direction.lower() not in ["w", "a", "s", "d"]:
            print("Invalid direction!")
        
        #FORWARD
        if move_direction == "w":
            #If at top wall already, cannot move forwards
            if (player.row_pos == 0):
                
                print("you slam your face into a wall... it seems this is as far forward as you can go.")
                
            #Attempt to enter boss room    
            elif (player.row_pos == 1 and player.col_pos == 0):
                
                answer = boss_access_attempt()
                
                if answer == True:
                    print("As you speak these words, the mighty door swings open.")
                    player.row_pos -= 1
                    move_accepted = True
                    
                else:
                    print("Nothing happened... It semms you must go elsewhere first.")
                    break
            #Valid move
            else:
                player.row_pos -= 1
                print("You walk to your forwards through a door and find yourself in NEW ROOM")
                move_accepted = True
        #LEFT     
        if move_direction == "a":
            #If at the left wall already, you cannot progress
            if (player.col_pos == 0):
                
                print("you slam your face into a wall... it seems this is as far left as you can go.")
            
            #Attempt to enter boss room
            elif (player.row_pos == 0 and player.col_pos == 1):
                
                answer = boss_access_attempt()
                
                if answer == True:
                    print("As you speak these words, the mighty door swings open.")
                    player.col_pos -= 1
                    move_accepted = True
                    
                else:
                    print("Nothing happened...")
                    break
            #Valid move
            else:
                player.col_pos -= 1
                print("You walk to your left through a door and find yourself in NEW ROOM")
                move_accepted = True
        #DOWN
        if move_direction == "s":
            #Barrier of map
            if (player.row_pos == 3):
                
                print("you slam your face into a wall... it seems this is as far backwards as you can go.")
            #Valid move
            else:
                player.row_pos += 1
                print("You walk to your backwards through a door and find yourself in NEW ROOM")
                move_accepted = True
        #RIGHT
        if move_direction == "d":
            #Barrier of map
            if (player.col_pos == 3):
                
                print("you slam your face into a wall... it seems this is as far right as you can go.")
            #Valid move
            else:
                player.col_pos += 1
                print("You walk to your right through a door and find yourself in NEW ROOM")
                move_accepted = True

        
    
player = Player(100, "Warrior")

for i in range(5):
    display_dungeon_map(player)
    player_move(player)
    display_dungeon_map(player)
