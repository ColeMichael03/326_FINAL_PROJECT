"""Simulate a dungeon crawler with procedurally generated rooms, combat, and loot collection"""
"test commit 5/1/26 4:50pm"
import data
import random
import time 

class Character:
    def __init__(self, health):
        self.health = health
    
    def choose_move(self, player):
        
        choices = {
            'Attack': 0,
            'Heal': 0,
            'Defend': 0     
        }
        
        for move in choices: 
            
            if move == 'Attack':
                #player low and enemy high 
                if 40 >= player.health and self.health >= 70:
                    choices[move]+=90 
                #player low and enemy medium 
                elif 40 >= player.health and 40 >= self.health < 70:
                    choices[move]+=70
                # both medium 
                elif 40 < player.health < 70 and 40 >= self.health < 70:
                    choices[move] += 50
                # both low 
                elif 40 > player.health and 40 > self.health:
                    choices[move] += 45
                # player med and enemy low 
                elif 40 < player.health < 70 and self.health < 40:
                    choices[move] += 20
                #player high and enemy low
                elif player.health > 70 and self.health < 40:
                    choices[move] += 10
                    
            if move == "Defend":
                #player low and enemy high 
                if 40 >= player.health and self.health >= 70:
                    choices[move]+=35
                #player low and enemy medium 
                elif 40 >= player.health and 40 >= self.health < 70:
                    choices[move]+=70
                # both medium 
                elif 40 < player.health < 70 and 40 >= self.health < 70:
                    choices[move] += 40
                # both low 
                elif 40 > player.health and 40 > self.health:
                    choices[move] += 30
                # player med and enemy low 
                elif 40 < player.health < 70 and self.health < 40:
                    choices[move] += 10
                #player high and enemy low
                elif player.health > 70 and self.health < 40:
                    choices[move] += 0
            
            if move == "Heal":
                if self.potion_count > 0: 
                    #player low and enemy high 
                    if 40 >= player.health and self.health >= 70:
                        choices[move]+=10
                    #player low and enemy medium 
                    elif 40 >= player.health and 40 >= self.health < 70:
                        choices[move]+=25
                    # both medium 
                    elif 40 < player.health < 70 and 40 >= self.health < 70:
                        choices[move] += 40
                    # both low 
                    elif 40 > player.health and 40 > self.health:
                        choices[move] += 50
                    # player med and enemy low 
                    elif 40 < player.health < 70 and self.health < 40:
                        choices[move] += 75
                    #player high and enemy low
                    elif player.health > 70 and self.health < 40:
                        choices[move] += 90
                else: 
                    choices[move] = 0
                     
        sorted_moves = sorted(choices.items(), key=lambda m: m[1], reverse=True)
        return sorted_moves[0][0]

class Player(Character):
    
    def __init__(self, health, character_class, player_name, dodge_chance):
        super().__init__(health)
        self.max_health = health
        self.character_class = character_class
        self.player_name = player_name
        self.row_pos = 0
        self.col_pos = 1
        self.dodge_chance = dodge_chance
        self.weapon = None
        self.gold = 0
        self.inventory = {"Health Potion": 2, "Mysterious Note": 1}
        self.is_hero = False
        
    def display_dungeon_map(self):
        
        map = [
        ["\u25A0\t", "\u25A0\t", "\u25A0\t","\u25A0\t"],
        ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"],
        ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"],
        ["\u25A0\t", "\u25A0\t", "\u25A0\t", "\u25A0\t"]
        ]
        
        #boss room symbol
        map[0][0] = "\u2620\t"
        #setting player symbol at the proper coordinates
        map[self.row_pos][self.col_pos] = "\u25CB\t"
    
        print("\n----Map Of The Dungeon----")
        for row in map:
            for item in row:
                print(item, end= " ")
            print("\n")
            
    def boss_access_attempt(self):
        #maybe use conditional expressopm
        print("You stand upon a massive door. A plaque says "
                "'Ye who dare enter must speak the words of Ragnaric.'")

        let_in = True if "Mysterious Note" in list(self.inventory.keys()) \
                else False
        
        if let_in:
            
            print("As you speak the words on the note, the mighty door " 
                f"swings open. You are in {data.rooms[0,0]}")
            
        else:
            print("You do not know what to do... Perhaps you can find this "
            "information somehwere.")
        return let_in
        

    def move(self):
    
        move_accepted = False
        
        while (not move_accepted):
            
            move_direction = input("Choose a direction to move in (w,a,s,d): ")
            
            if move_direction.lower() not in ["w", "a", "s", "d"]:
                print("Invalid direction!")
            
            
            #FORWARD
            if move_direction == "w":
                #If at top wall already, cannot move forwards
                if (self.row_pos == 0):
        
                    print("you slam your face into a wall... "
                        "it seems this is as far forward as you can go.")
                    
                #Attempt to enter boss room    
                elif (self.row_pos == 1 and self.col_pos == 0):
                    
                    answer = self.boss_access_attempt()
                    
                    if answer == True:
                        self.row_pos -= 1
                        move_accepted = True
                        
                    else: 
                        continue
                    
                #Valid move
                else:
                    self.row_pos -= 1
                    print("You walk forwards through a door and find "
                        f"yourself in the {data.rooms[(self.row_pos, self.col_pos)]}")
                    move_accepted = True
                    
                    
            #LEFT     
            if move_direction == "a":
                #If at the left wall already, you cannot progress
                if (self.col_pos == 0):
                    
                    print("you slam your face into a wall... "
                        "it seems this is as far left as you can go.")
                
                #Attempt to enter boss room
                elif (self.row_pos == 0 and self.col_pos == 1):
                    
                    answer = self.boss_access_attempt()
                    
                    if answer == True:
                        self.col_pos -= 1
                        move_accepted = True
                        
                    else:
                        continue
                    
                #Valid move
                else:
                    self.col_pos -= 1
                    print("You walk to your left through a door and find "
                        f"yourself in the {data.rooms[(self.row_pos, self.col_pos)]}")
                    move_accepted = True
            #DOWN
            if move_direction == "s":
                #Barrier of map
                if (self.row_pos == 3):
                    
                    print("you slam your face into a wall... "
                        "it seems this is as far backwards as you can go.")
                #Valid move
                else:
                    self.row_pos += 1
                    print("You walk backwards through a door and find "
                        f"yourself in the {data.rooms[(self.row_pos, self.col_pos)]}")
                    move_accepted = True
            #RIGHT
            if move_direction == "d":
                #Barrier of map
                if (self.col_pos == 3):
                    
                    print("you slam your face into a wall... "
                        "it seems this is as far right as you can go.")
                #Valid move
                else:
                    self.col_pos += 1
                    print("You walk to your right through a door and find "
                        f"yourself in the {data.rooms[(self.row_pos, self.col_pos)]}")
                    move_accepted = True        

    def light_attack(self, enemy):
        total_miss_chance = self.weapon.light_miss_chance + enemy.dodge_chance
        #successful hit
        if random.randint(0,100) > total_miss_chance:
            if self.character_class == "Warrior":
                print(f"You quickly jab your Battleaxe into the side of the " 
                    f"{enemy.name}, dealing {self.weapon.light_damage} damage.")
                
            if self.character_class == "Mage":
                print(f"You swiftly raise your Grand Staff, and launch a bolt "
                    "of light at the " 
                    f"{enemy.name}, dealing {self.weapon.light_damage} damage.")
            
            if self.character_class == "Thief":
                print(f"You quickly slash the {enemy.name} with your Obsidian "
                    f"Dagger, dealing {self.weapon.light_damage} damage.")
                    
            enemy.health -= self.weapon.light_damage
            print(f"The {enemy.name} has {enemy.health} health remaining.")
        else:
            print(f"The {enemy.name} dodges the attack!")
                
    def heavy_attack(self, enemy):
        total_miss_chance = self.weapon.heavy_miss_chance + enemy.dodge_chance
        #successful hit
        if random.randint(0,100) > total_miss_chance:
            if self.character_class == "Warrior":
                print(f"With a echoing roar, you slam your Battleaxe into the " 
                    f"{enemy.name}, dealing {self.weapon.heavy_damage} damage.")
                
            if self.character_class == "Mage":
                print(f"After channeling your energy into your Grand Staff, "
                    "A blue beam erupts from the orb and hurls towards the " 
                    f"{enemy.name}, dealing {self.weapon.heavy_damage} damage.")
            
            if self.character_class == "Thief":
                print(f"You lunge into the {enemy.name} with your Obsidian "
                    f"Dagger, dealing {self.weapon.heavy_damage} damage.")
                    
            enemy.health -= self.weapon.heavy_damage
            print(f"The {enemy.name} has {enemy.health} health remaining.")
        else:
            print(f"The {enemy.name} dodges the attack!")
    
    def heal(self):
        if self.inventory["Health Potion"] > 0:
            if self.health + 60 < self.max_health:
                self.health += 60
            else:
                self.health = self.max_health
            self.inventory["Health Potion"] -= 1
                
            print(f"You drink a health potion. your hp is now "
                  f"{self.health}/{self.max_health}")
        else:
            print("You are out of health potions.")

    def remove_item(self):
        
        if len(self.inventory) == 0:
            print("Inventory is empty. Nothing to remove.")
            return False
        
        print("\n Your Inventory:")
        items = list(self.inventory.keys())
        
        # loops through index
        i = 0
        while i < len(items):
            item = items[i]
            print(str(i + 1) + ". " + item + " (x" + str(self.inventory[item]) + ")")
            i += 1
            
        choice = input('Choose item to remove or press "q" to cancel: ')   
        if choice == 'q':
            return False
        
        try:
            index = int(choice) - 1
            item_removed = items[index]
        
            self.inventory[item_removed] = self.inventory[item_removed] - 1
        
            if self.inventory[item_removed] == 0:
                del self.inventory[item_removed]
                
            print("You dropped " + item_removed)
            return True
    
        except:
            print("What are you saying?")
            return False
        
    def loot_enemy(self, enemy):
        max_inv = 5
        
        for item in enemy.inventory:
            
            choice = input("Take " + item + "? (y/n): ")
        
            while choice != 'y' and choice != 'n':
                choice = input("Enter y for Yes or n for No: ")
                
            if choice == 'n':
                print("You leave the " + item)
                continue
            
            print("You grab " + item + "...")

            # if item already in inventory
            if item in self.inventory:
                self.inventory[item] = self.inventory[item] + 1
                print(item + " now x" + str(self.inventory[item]))
                continue
            
            # if inventory NOT full
            if len(self.inventory) < max_inv:
                self.inventory[item] = 1
                print("You picked up " + item)
                continue
            
            # if inventory is full
            print("Inventory full!")
            
            removed = self.remove_item()
            
            if removed == True:
                self.inventory[item] = 1
                print(item + " added")
            else:
                print("You leave the " + item)
                
        print("\nFinal Inventory:")
        for item_name in self.inventory:
            print(item_name + ": x" + str(self.inventory[item_name]))
            
    def __str__(self):
        weapon_name = self.weapon.weapon_name
        if self.health > 99:
            return f"You are in good shape!: \n Class: \
        {self.character_class} \n Health: {self.health} \n Weapon: \
        {weapon_name}"
        
        elif self.health > 80 and self.character_class != "Thief":
            return f"You are in okay shape!: \n Class: \
        {self.character_class} \n Health: {self.health} \n Weapon: \
        {weapon_name}"
        
        elif self.health > 80 and self.character_class == "Thief":
            return f"You are in good shape!: \n Class: \
        {self.character_class} \n Health: {self.health} \n Weapon: \
        {weapon_name}"
        
        elif self.health > 50 and self.character_class == "Thief":
            return f"You are in okay shape!: \n Class: \
        {self.character_class} \n Health: {self.health} \n Weapon: \
        {weapon_name}"
        
        else:
            return f"You are in bad shape!: \n Class: \
        {self.character_class} \n Health: {self.health} \n Weapon: \
        {weapon_name}"

class Enemy(Character):
    """
    Basic Enemy Class. Will be spawned in during combat encounters.
    Attributes:
        gold(int) the amount of gold held, will be given to player upon defeat.
        
        inventory(list) Enemy's inventory to be looted upon defeat.
        
        potion_count(int) How many health potions the enemy has
        
        damage(int) The damage that will be given to the player if the enemy 
        does an attack move
        
        block_chance(int) The enemy's chance to block the players attach. Will
        be raised if the enemy chooses to defend.
        
        name(string) The enemy's name.
    """
    def __init__(self, health):
        super().__init__(health)
        self.gold = random.randint(20, 100)
        
        self.inventory = ["Health Potion"]
        
        self.potion_count = 2
        
        self.damage = random.randint(15,30)
        
        self.dodge_chance = 0
        
        name_generator = random.randint(1,12)
        self.name = data.enemy_types[name_generator]
        
        item1 = random.randint(1,12)
        self.inventory.append(data.items[item1])
        
        item2 = random.randint(1,12)
        self.inventory.append(data.items[item2])

        note_chance = random.randint(1,10)
        if note_chance == 7:
            self.inventory.append("Mysterious Note")
        
             
class Weapon():
    def __init__(self, weapon_name, heavy_damage, light_damage, 
                heavy_miss_chance, light_miss_chance):
        self.weapon_name = weapon_name
        self.heavy_damage = heavy_damage
        self.light_damage = light_damage
        self.heavy_miss_chance = heavy_miss_chance
        self.light_miss_chance = light_miss_chance

class Aric(Character):
    def __init__(self, health):
        super().__init__(health)  
        self.max_health = health
        self.name = "Aric The Almighty"
        self.dodge_chance = 1
        self.weapon = Weapon("Staff of The Final Exception", 40, 15, 30, 10)
        self.potion_count = 3
        self.super_potion = 1
        
    def attack(self, player):
        
        attack_type = random.choice(["Heavy", "Light"])
        
        
        if attack_type == "Heavy":
        #attack hits
            if random.randint(0,100) > player.dodge_chance:
                player.health -= self.weapon.heavy_damage
                print(f"{self.name} batters you with a heavy blow!\n"
                    f"You have {player.health}/{player.max_health} health left!")
                
        elif attack_type == "Light":
            
            if random.randint(50,100) > player.dodge_chance: 
                player.health -= self.weapon.light_damage
                print(f"{self.name} stuns you with a lightning quick jab!\n"
                    f"you have {player.health}/{player.max_health} health left!")
                            
            
    def heal(self):
        if 0 < self.potion_count and self.health > 0: 
            if self.health + 50 < self.max_health: 
                self.health += 50
                print(f"{self.name} heals themselves! ")
                print(f"{self.name} has {self.health} remaining!")
            elif self.health == self.max_health:
                self.potion_count -= 1
            
        else: 
            print(f"{self.name} can no longer heal!")
        
        
    def defend(self):
        self.dodge_chance = 33
        
        
           
        
        
        
    
        
def create_player():
    
    name = input("After days following the ragged map given you "
                 "by a mysterous man in a tavern, you finally find yourself at "
                 "the entrance of a decrepit dungeon. \nWhat is your name? ")
    
    player_class = "0"
    
    while player_class not in ["1", "2", "3"]:
        player_class = input(f"Very well, {name}. What is your background?.\n"
                            "1. A warrior, veteran of the Great War.\n"
                            "2. A mage, graduate of The Arcane Institute.\n"
                            "3. A thief, legend of the underworld\n")
    
    if player_class == "1":
        player = Player(150, "Warrior", name, 10)
        player.weapon = Weapon("Battleaxe", 65, 35, 50, 20)
        
    elif player_class == "2":
        player = Player(125, "Mage", name, 20)
        player.weapon = Weapon("Grand Staff", 50, 25, 30, 10)
    else:
        player = Player(100, "Thief", name, 65)
        player.weapon = Weapon("Obsidian Dagger", 40, 15, 10, 0)
    
    print(f"After a moment of contemplation, {player.player_name} "
          f"the {player.character_class} enters the dungeon.")
    
    return player
    
#Encounter functions here
def combat(player):
    enemy = Enemy(100)
    print(f"You encounter a hostile {enemy.name}!")
    
    while player.health > 0 and enemy.health > 0:
        player_move = None
        
        while player_move not in ["1", "2", "3"]:
            player_move = input("Select your move.\n1 to Heavy Attack\n"
                  "2 to Light Attack\n3 to Heal\n")
            
        if player_move == "1":
            player.heavy_attack(enemy)
        elif player_move == "2":
            player.light_attack(enemy)
        else:
            player.heal()
        
    

def shopkeeper(player):
    #Almost done. Error when selling items, as the dict size changes during iteration..
    enter_shop = input("You happen upon a small shop with a gnome tending "
          "the stall. The gnome says he is open for business.\n"
          "Do you approach? (y/n) ")
    
    if enter_shop == "y":
        in_shop = True
        
        while in_shop:
            choice = None
            while choice not in ["1", "2", "3"]:
                choice =input("The gnome says: 'Are ye looking to sell or buy?'"
                        "\nPress 1 to Sell\nPress 2 to Buy\nPress 3 to Leave\n")
            
            if choice == "1":
                
                sellable_items = list(data.items.values())
            
                for item, quantity in list(player.inventory.items()):
                    if item in sellable_items:
                        gold = random.randint(20, 60) * quantity
                        print(f"You sold your {quantity} {item} "
                              f"for {gold} gold.")
                        player.gold += gold
                        player.inventory.pop(item)
                        
                print(f"You now have {player.gold} gold coins.")
        
            elif choice == "2":
                still_buying = True
                
                while still_buying:
                    print(f"\nYou have {player.gold} gold pieces to spend.")
                    buy_choice = input("1. Health Potion: 50 gold pieces\n"
                          "2. Upgrade Heavy Attack: 200 gold pieces.\n"
                          "3. Upgrade Light Attack: 120 gold pieces\n"
                          "4. Increase Agility: 200 gold pieces.\n"
                          "5. Exit\n")
                  
                    if buy_choice == "1":
                        if player.gold >= 50:
                            player.inventory["Health Potion"] += 1
                            player.gold -= 50
                            print("You purchase the health potion.")
                        else:
                            print("You cannot afford this!")
                            
                    elif buy_choice == "2":
                        if player.gold >= 200:
                            player.weapon.heavy_damage += 10
                            player.gold -= 200
                            print(f"You upgraded your heavy attack."
                                " It now does "
                                f"{player.weapon.heavy_damage} damage.")
                        else:
                            print("You cannot afford this!")
                            
                    elif buy_choice == "3":
                        if player.gold >= 120:
                            player.weapon.light_damage += 10
                            player.gold -= 120
                            print(f"You upgraded your light attack."
                                " It now does "
                                f"{player.weapon.light_damage} damage.")
                        else:
                            print("You cannot afford this!")
                            
                    elif buy_choice == "4":
                        if player.gold >= 200:
                            player.dodge_chance += 10
                            player.gold -= 200
                            print(f"You upgraded your agility. "
                                f"You now have a {player.dodge_chance}% chance "
                                f"to dodge an incoming attack.")
                        else:
                            print("You cannot afford this!")
                    else:
                        still_buying = False
                        

            else:
                in_shop = False
    
    
    print("You continue on your adventure.")
        
#Cole's totem of luck function. 
def totem_of_luck(player):
        print("As you enter the room, there is no trace of life. In the center "
              "lies an old stone totem, covered in years of moss.\n"
              "There is a pitch black pit in the totem's open mouth. "
              "Carvings in the stone reads 'Do you feel lucky, Punk?'\n")
        
        
        choice = input(f"{player.player_name} do you wish to interact"
                        " with the totem of luck? (y/n): ")
        
        while choice != 'y' and choice != 'n':
                choice = input("Enter 'y' for Yes or 'n' for No: ").casefold()
                
        if choice == 'n':
            print("You decide that you are not in a gambling mood.")
         
            
        
        if choice == 'y':
            print("After a moment of though, you remember that "
                  "luck favors the bold, and reach into the totem jaws.")

            luck = random.randint(1,2)
            if luck == 1: 
                print("The totem's mouth snaps closed, causing a severe wound")
                player.health = player.health * 30 // 100
                print("You lose %30 of your health.")
                print(f"Current health: {player.health}")
               
            
            if luck == 2:
                print("You reach into the mouth and grab a pouch of gold coins.")
                gold = random.randint(80,200)
                player.gold += gold 
                print(f"Congrats you've earned {gold} gold!")

                  
                
def free_roam(player):
    ###function that calls other functions
    # Only ends once you leave room
    
    # ###
    
    choice_switch = False
    
    while not choice_switch:
        
        choice = input("""You are now in free roam and are free to choose an action:
                        1: Inspect Map
                        2: Manage Inventory
                        3: Heal
                        4: Leave Room
                          """)
        if choice == '1':
            player.display_dungeon_map()
            
        if choice == '2':
            player.remove_item()
        
        if choice == '3':
            player.heal()
            
        if choice == '4':
            player.move()
            choice_switch = True
        
def reward():
    aric = Aric(100)
    print("Arric the Almighty staggers... ")
    time.sleep(2)
    print("'Impossible'...")
    time.sleep(2)
    print("He falls to one knee...")
    time.sleep(2)
    print("...'Very well.. You pass.'\n")
    time.sleep(2)
    print("---REWARDS---")
    print("-- A passing grade")
    print(f"-- {aric.weapon.weapon_name}")
    time.sleep(1)
    
    print("'One more thing before you go.. '")
    print("")
    

    



            
        
        













def boss_fight(player):
    aric = Aric(175)
    #Aric's opening monologue vvv
    time.sleep(2)
    print(f"You've made it...")
    time.sleep(2)
    print(f"You think you brought yourself here?")
    time.sleep(2)
    print(f"This dungeon.. Every rule you've followed, every path you've taken,")
    time.sleep(3)
    print("was me.")
    time.sleep(3)
    print(f"Now come. Show me what you've learned.\n")
    print("\n")
    time.sleep(3)
    
    while player.health > 0 and aric.health > 0:
        player_move = None
        
        while player_move not in ["1", "2", "3"]:
            player_move = input("Select your move.\n1 to Heavy Attack\n"
                  "2 to Light Attack\n3 to Heal\n")
            
        if player_move == "1":
            player.heavy_attack(aric)
        elif player_move == "2":
            player.light_attack(aric)
        else:
            player.heal()
        
        
        
        if aric.health <= 0 and aric.super_potion > 0: 
                aric.health = aric.max_health
                aric.super_potion -= 1
                print(f"{aric.name} resurrects using a Super Potion!")
                
        elif aric.health > 0:
            
            aric_act = aric.choose_move(player)
        
            if aric_act == "Attack":
                aric.attack(player)
                
            if aric_act == "Heal":
                aric.heal()
            
            if aric_act == "Defend":
                aric.defend()
                print(f"Dodge chance = {aric.dodge_chance}")
                aric.dodge_chance = 1
        
        else: 
            reward()
            
            break

        
    
#TESTING ZONE
player = create_player()
for i in range(5):
    player.display_dungeon_map()
    player.move()
    boss_fight(player)
    free_roam(player)
    shopkeeper(player)
    totem_of_luck(player)
