#File for creating our functions

def boss_access_attempt():
    #Helper function for the player_move function
    code = "ABCD"
    
    guess = input("guess password: ")
    
    if guess == code:
        return True
    else:
        return False
    
def player_move(row_pos, col_pos, room_names):
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
                print("you slam your face into a wall... \
                      it seems this is as far forward as you can go.")
                
            elif (row_pos == 1 and col_pos == 0):
                #attempting to enter the boss room (0,0) from below.
                answer = boss_access_attempt()
                #if password is correct this method will return true
                
                if answer == True:
                    #allow entry to boss room
                    print("As you speak these words, \
                          the mighty door swings open.")
                    row_pos -= 1
                    move_accepted = True
                else:
                    #password incorrect, choose differnet move.
                    print("Nothing happened... \
                          It semms you must go elsewhere first.")
                    continue
                
            else:
                #valid move into room other than boss room.
                row_pos -= 1
                print(f"You walk forwards through a door and find \
                      yourself in {room_names["rooms"][(row_pos, col_pos)]}")
                move_accepted = True
                
                
        #Left move logic
        if move_direction == "a":
            
            if (col_pos == 0):
                #cant go any more left if at far left column
                print("you slam your face into a wall... \
                    it seems this is as far left as you can go.")
            elif (row_pos == 0 and col_pos == 1):
                #attemting to enter boss room from the left
                answer = boss_access_attempt()
                #if password is correct this method will return true
        
                if answer == True:
                    #allow entry to boss room
                    print("As you speak these words, \
                          the mighty door swings open.")
                    row_col -= 1
                    move_accepted = True
                else:
                    #password incorrect, choose differnet move.
                    print("Nothing happened... \
                          It semms you must go elsewhere first.")
                    continue
            else:
                #valid move to room other than boss room.
                col_pos -= 1
                print(f"You walk to your left through a door and find \
                      yourself in {room_names["rooms"][(row_pos, col_pos)]}")
                move_accepted = True
                
                
            #Down move logic
            if move_direction == "s":
        
                if (row_pos == 3):
                    #Cant move down if on the bottom row
                    print("you slam your face into a wall... \
                        it seems this is as far backwards as you can go.")
                
                else:
                    #Valid move
                    row_pos += 1
                    print(f"You walk backwards through a door and find \
                        yourself in {room_names["rooms"][(row_pos, col_pos)]}")
                    move_accepted = True
            
            
            #Right move logic
            if move_direction == "d":
        
                if (col_pos == 3):
                    #Cant move down if on the right column
                    print("you slam your face into a wall... \
                        it seems this is as far right as you can go.")
                
                else:
                    #Valid move
                    col_pos += 1
                    print(f"You walk to your right through a door and find \
                        yourself in {room_names["rooms"][(row_pos, col_pos)]}")
                    move_accepted = True
    
    #A valid move has been made, and the coordinates have changed.
    #Return the coordinates as a tuple
    return (row_pos, col_pos)