#File for creating our functions for the check in
import data
import random


#Liam's helper function
def boss_access_attempt():
    """
    Helper Function for the player_move function, used if the player attempts to
    enter the boss room.
    
    Returns:
        Bool: True if password is correct, otherwise False
    """
    
    code = "ABCD"
    
    guess = input("guess password: ")
    
    if guess == code:
        print("As you speak these words, "
        f"the mighty door swings open. You are in {data.rooms[0,0]}")
        return True
    else:
        print("Nothing happened... "
        "It seems you must figure out what to say first.")
        return False
    
#Liam's algo
def player_move(row_pos, col_pos):
    """
    Function that allows player to move about the 4x4 map.
    
    Args:
        row_pos (int) the current row the player is on
        col_pos (int) the current col the player is on
    Returns:
        tuple (int,int) the players coordinates
    
    """

    move_accepted = False
    
    while (not move_accepted):
        
        move_direction = input("Chose direction to move in (w,a,s,d): ")
        #move validation
        if move_direction.lower() not in ["w", "a", "s", "d"]:
            print("Invalid direction!")
            
            
        #Forward move logic
        if move_direction == "w":
            
            if (row_pos == 0):
                 #can't go forward if on the top row
                print("you slam your face into a wall... "
                      "it seems this is as far forward as you can go.")
                
            elif (row_pos == 1 and col_pos == 0):
                #attempting to enter the boss room (0,0) from below.
                answer = boss_access_attempt()
                #if password is correct this method will return true
                
                if answer == True:
                    row_pos -= 1
                    move_accepted = True
                else:
                    #password incorrect, choose differnet move.
                    continue
                
            else:
                #valid move into room other than boss room.
                row_pos -= 1
                print(f"You walk forwards through a door and find "
                      f"yourself in the {data.rooms[(row_pos, col_pos)]}")
                move_accepted = True
                
                
        #Left move logic
        if move_direction == "a":
            
            if (col_pos == 0):
                #cant go any more left if at far left column
                print("you slam your face into a wall... "
                    "it seems this is as far left as you can go.")
                
            elif (row_pos == 0 and col_pos == 1):
                #attemting to enter boss room from the left
                answer = boss_access_attempt()
                #if password is correct this method will return true
        
                if answer == True:
                    #allow entry to boss room
                    col_pos -= 1
                    move_accepted = True
                else:
                    #password incorrect, choose differnet move.
                    continue
            else:
                #valid move to room other than boss room.
                col_pos -= 1
                print(f"You walk to your left through a door and find "
                    f"yourself in the {data.rooms[(row_pos, col_pos)]}")
                move_accepted = True
                
                
            #Down move logic
        if move_direction == "s":
        
            if (row_pos == 3):
                #Cant move down if on the bottom row
                print("you slam your face into a wall... "
                    "it seems this is as far backwards as you can go.")
                
            else:
                #Valid move
                row_pos += 1
                print(f"You walk backwards through a door and find "
                      f"yourself in the {data.rooms[(row_pos, col_pos)]}")
                move_accepted = True
            
            
        #Right move logic
        if move_direction == "d":
        
            if (col_pos == 3):
                #Cant move down if on the right column
                print("you slam your face into a wall... "
                    "it seems this is as far right as you can go.")
                
            else:
                #Valid move
                col_pos += 1
                print(f"You walk to your right through a door and find "
                    f"yourself in the {data.rooms[(row_pos, col_pos)]}")
                move_accepted = True
    
    #A valid move has been made, and the coordinates have changed.
    #Return the coordinates as a tuple
    return (row_pos, col_pos)

#Cole's algo
def enemy_move(php, ehp, pc):
    """
    Function to determine enemy's move
    Args:
        php(int) the players health points
        ehp(int) the enemy's health points
        pc(int) the enemy's potion count
    Returns:
        tuple: the enemy's move (str), the enemy's potion count (int)
    
    """
    
    potion_count = pc 
    player_health = php 
    enemy_health = ehp
    
    
    #later on the values will be used as weights in a randomizer 
    choices = {
        'attack': 0,
        'heal': 0,
        'defend': 0     
    }
    
    for move in choices: 
        if move == 'attack':
            #player low and enemy high 
            if 40 >= player_health and enemy_health >= 70:
                choices[move]+=90 
            #player low and enemy medium 
            elif 40 >= player_health and 40 >= enemy_health < 70:
                choices[move]+=70
            # both medium 
            elif 40 >= player_health < 70 and 40 >= enemy_health < 70:
                choices[move] += 50
            # both low 
            elif 40 > player_health and 40 > enemy_health:
                choices[move] += 45
            # player med and enemy low 
            elif 40 >= player_health < 70 and enemy_health < 40:
                choices[move] += 20
            #player high and enemy low
            elif player_health > 70 and enemy_health < 40:
                choices[move] += 10
                
        if move == "defend":
            #player low and enemy high 
            if 40 >= player_health and enemy_health >= 70:
                choices[move]+=35
            #player low and enemy medium 
            elif 40 >= player_health and 40 >= enemy_health < 70:
                choices[move]+=70
            # both medium 
            elif 40 >= player_health < 70 and 40 >= enemy_health < 70:
                choices[move] += 40
            # both low 
            elif 40 > player_health and 40 > enemy_health:
                choices[move] += 30
            # player med and enemy low 
            elif 40 >= player_health < 70 and enemy_health < 40:
                choices[move] += 10
            #player high and enemy low
            elif player_health > 70 and enemy_health < 40:
                choices[move] += 0
        
        if move == "heal":
            if potion_count > 0: 
                #player low and enemy high 
                if 40 >= player_health and enemy_health >= 70:
                    choices[move]+=10
                #player low and enemy medium 
                elif 40 >= player_health and 40 >= enemy_health < 70:
                    choices[move]+=25
                # both medium 
                elif 40 >= player_health < 70 and 40 >= enemy_health < 70:
                    choices[move] += 40
                # both low 
                elif 40 > player_health and 40 > enemy_health:
                    choices[move] += 50
                # player med and enemy low 
                elif 40 >= player_health < 70 and enemy_health < 40:
                    choices[move] += 75
                #player high and enemy low
                elif player_health > 70 and enemy_health < 40:
                    choices[move] += 90
            else: 
                choices[move] = 0 
        
            
            # sort dict 
            
            sorted_moves = sorted(choices.items(), key=lambda m: m[1], reverse=True)
            
            print(sorted_moves[0][0])
            if sorted_moves[0][0] == 'heal':
                potion_count -= 1
            
            
                
        
        
        
    return (sorted_moves[0], potion_count)

#Logan's algo
def combat(p_inv, e_inv, max_inv):
    """
    Simulates a fight between the enemy and the player
    Args:
        p_inv(dict) the player's inventory - to be used for looting
        e_inv(list) the enemy's inventory - to be used for looting
        max_inv(int) the maxinum allowed player inventory slots.
    """
    
    php = 100
    ehp = 100
    pc = 2
    while php > 0 and ehp > 0:
        attack_choice = input("Press 1 to perform a heavy attack, Press 2 to"
            " perform a light attack, 3 to heal ")
        if attack_choice == "1":
            ehp -= 65
            print(f"You performed a heavy attack! The enemy has {ehp} health.")
        elif attack_choice == "2":
            ehp -= 15
            print(f"You performed a light attack! The enemy has {ehp} health.")
        elif attack_choice == "3":
            if pc > 0:
                if php + 10 > 100:
                    php = 100
                else:
                    php += 10
                pc -=1
                print(f"You healed! You now have {php} health!")
            else:
                print("Uh Oh! You have no potions! You drink nothing!")
       
        if ehp <= 0:
            print("You defeated the enemy!")
            enemy_loot(p_inv, e_inv, max_inv)
            break    
        
        move, pc = enemy_move(php, ehp, pc)    
        enemy_action = move[0]
        
        print(f"The enemy chose to {enemy_action}!")
        
        if enemy_action == "attack":
            php -= 20
            print(f"The enemy does 20 damage! You have {php} health! ")
        elif enemy_action == "heal":
            ehp +=15
            print(f"The enemy now has {ehp} health!")
        elif enemy_action == "defend":
            print("The enemy braces for impact")            
    
    if php <= 0:
        print("The enemy has defeated you!")
    
#Nathan's helper
def remove_item(player_inv):
    """
    Manages removing items from player inventory.
    Args:
        player_inv(dict) the players inventory
    Side_effects:
        changes the contents of the inventory to free up space.
    Returns:
        boolean. True if space freed, false otherwise
    """
    
    if len(player_inv) == 0:
        print("Inventory is empty. Nothing to remove.")
        return False
    
    print("\n Your Inventory:")
    
    items = list(player_inv.keys())
    
    # loops through index
    i = 0
    while i < len(items):
        item = items[i]
        print(str(i + 1) + ". " + item + " (x" + str(player_inv[item]) + ")")
        i += 1
        
    choice = input('Choose item to remove or press "q" to cancel: ')   
    
    if choice == 'q':
        return False
    
    try:
        index = int(choice) - 1
        item_removed = items[index]
        
        player_inv[item_removed] = player_inv[item_removed] - 1
        
        if player_inv[item_removed] == 0:
            del player_inv[item_removed]
            
        print("You dropped " + item_removed)
        return True
    
    except:
        print("What are you saying?")
        return False
    
#Nathan's algo
def enemy_loot(player_inv, enemy_inv, max_inv):
    """
    Manages choosing what items to pick up from enemies.
    Args:
        p_inv(dict) the player's inventory 
        e_inv(list) the enemy's inventory
        max_inv(int) the maxinum allowed player inventory slots.
    Side Effects:
        adds new items to player's inventory
    """
    print("\n Enemy defeated! You found...\n")
    
    # loops through the enemies inventory
    for item in enemy_inv:
        
        choice = input("Take " + item + "? (y/n): ")
        
        while choice != 'y' and choice != 'n':
            choice = input("Enter y for Yes or n for No: ")
            
        if choice == 'n':
            print("You leave the " + item)
            continue
        
        print("You grab " + item + "...")
        
        # if item already in inventory
        if item in player_inv:
            player_inv[item] = player_inv[item] + 1
            print(item + " now x" + str(player_inv[item]))
            continue
        
        # if inventory NOT full
        if len(player_inv) < max_inv:
            player_inv[item] = 1
            print("You picked up " + item)
            continue
        
        # if inventory is full
        print("Inventory full!")
        
        removed = remove_item(player_inv)
        
        if removed == True:
            player_inv[item] = 1
            print(item + " added")
        else:
            print("You leave the " + item)
        
    # Just prints the full inventory by default for now    
    print("\nFinal Inventory:")
    for item_name in player_inv:
        print(item_name + ": x" + str(player_inv[item_name]))
        
#Cole's totem of luck function. 

def totem_of_luck(player, php):
    
        choice = input(f"{player.name} do you wish to interact \
                               with the totem of luck? (y/n):")
        
        while choice != 'y' and choice != 'n':
                choice = input("Enter 'y' for Yes or 'n' for No: ").casefold()
                
        if choice == 'n':
            print("Not a gambler I see. Maybe next time.")
            return 
            
        
        if choice == 'y':
            print("Luck favors the bold.")

            luck = random.randint(1,2)
            if luck == 1: 
                
                php = php * 30 // 100
                print("You lose %30 of your health.")
                print(f"Current health: {php}")
                return php
            
            if luck == 2:
                gold = random.randint(80,200)
                player.gold += gold 
                print(f"Congrats you've earned {gold} gold!")
                return player.gold 
                
        
    
#tests for the algorithms
    
if __name__ == "__main__":
    
    player_inv = {
        "Health Potion": 2,
        "Copper Wire": 5,
        "Saber": 1
    }
    
    enemy_inv = ["Health Potion", "Copper Wire", "Longsword", "Shield"]
    max_inv = 3
    
    player_x = 1
    player_y = 0
    
    print("Welcome to the functions test phase. We will walk you through our"
        "algorithms here.")
    
    for i in range(3):
        player_x, player_y = player_move(player_x,player_y)
        print("Oh no! You have encountered an enemy!")
        combat(player_inv, enemy_inv, max_inv)
