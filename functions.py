#File for creating our functions

import data

def boss_access_attempt():
    #Helper function for the player_move function
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
    
def player_move(row_pos, col_pos):
    #Note the map is a 4x4 grid, we will use this info to determine map barriers
    
    #loop variable to ensure funciton does not end until valid move is made
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





def enemy_move(php, ehp, pc):
    
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



move, pc = enemy_move(86, 15, 2)

print(f"enemy used {move} and has a pc of {pc}")
        