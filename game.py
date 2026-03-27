
def display_dungeon_map(player_x, player_y):
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
    ["\u25A0", "\u25A0", "\u25A0", "\u25A0", "\u25A0"],
    ["\u25A0", "\u25A0", "\u25A0", "\u25A0", "\u25A0"],
    ["\u25A0", "\u25A0", "\u25A0", "\u25A0", "\u25A0"],
    ["\u25A0", "\u25A0", "\u25A0", "\u25A0", "\u25A0"],
    ["\u25A0", "\u25A0", "\u25A0", "\u25A0", "\u25A0"]
    ]
    
    map[player_x][player_y] = "\u25CB"
    print("--MAP OF THE DUNGEON--")
    for row in map:
        for item in row:
            print(item, end= " ")
        print("\n")
        
        
display_dungeon_map(4, 2)