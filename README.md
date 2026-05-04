# INST326 Dungeon Game Project
## By Cole Riddlebarger, Nathan Kalinsky, Logan Torma-Kim, and Liam Murray

This program is a small dungeon crawler style RPG. The player chooses their character class and enters a 4x4 grid of dungeon rooms.
The player must traverse enemies, puzzles and other encounters before ultimately defeating the boss to complete the game.

## Files:
### data.py
This file holds dictionaries for the names of rooms, enemies and loot drops. It is imported into game.py where it is used to assign names.

### functions.py
This file holds each of our algorithms used for the check in. Nothing here is used in the game, it is just here for grading purposes.

### game.py
This is the main function for the game. It holds all classes and functions that make the game run, including the main loop.

# Running the Game
To run the game, simply enter `python3 game.py` into your shell when in the same directory as the file. 
No command line arguments needed! (Windows users remove the '3')


## Bibliography
"Daggerfall:Bestiary", *The Unofficial Elder Scrolls Wiki*, https://en.uesp.net/wiki/Daggerfall:Bestiary

# Attribution Table

|Method/Function|Primary Author|Techniques demonstrated|
|----------------|--------------|----------------------|
|Character.choose_move()|Cole Riddlebarger|List comprehension|
|Aric.__init__()|Cole Riddlebarger|Composition of two custom classes|
|shopkeep()|Liam Murray|Sequence unpacking|
|player.boss_access_attempt()|Liam Murray|Conditional expression|
|player.remove_item()|Nathan Kalinsky|Use of a key function|
|player.__str__()|Logan Torma-Kim|Magic method|

