# Warrior Knock Out - 2 Players 2D Fighting Game
# Author: Le Duy An Tran 
![image](https://user-images.githubusercontent.com/114903308/193661921-ac0df15e-ca57-49c9-8776-3cb9d236a00b.png)
# About:
A 2 players 2D fighting game suits for friends or people who are looking for an arcade fast-pace game to play locally together. It is a non-story game, but takes place in a jungle land where martial arts are dominating and represent one's spirit and power. The game has 4 designed characters with different traits suit for 4 different play styles. Players will each have 3 lives and a HP bar, when an HP bar runs out, 1 live will be deducted, whoever runs out of lives first will lose. 
# Software:
Visual Studio Code, Aseprite
# Mechanic Features:
![image](https://user-images.githubusercontent.com/114903308/193673133-16a05d17-0ec7-459d-bacb-ef3c9bf11a5f.png)

1. Maps Random Generation: There are two maps - The Jungle and The Sunset. When the game starts, players will be sent to a random fighting map either The Jungle, or The Sunset.

![image](https://user-images.githubusercontent.com/114903308/193676544-4d97930c-540c-4051-908f-543923ab5ea6.png)

2. Player Controls: The players will have two different sets of keys on the keyboard to control each of their own character to move, jump and fight. Some characters will have more speed but is low on health, and some will have the attack speed to be faster than the other. Based on the traits information, players will find which characters should them the best with their play style. Jumping can provide a creative play style for the players to dodge an attack.
3. Fighting and Damage/Def Calculations: Players can be hurt - decrease in health when comes close enough and fight the other. Each punch/attack will contains different random amount of damage based on the traits of the characters - some characters have a higher attack damage, however, the actual damage passed on the player will be deducted by the fixed amount of defense the character has (sometimes player can block the others by when the attack damage is lower or equal to the defensive amount). 
# GUI Features:
![image](https://user-images.githubusercontent.com/114903308/193676893-d4946375-5455-44e0-befb-8155d8f7a850.png)

1. Player Selection Menu: The character selection menu allows the first player to choose their favor character, then the second player will be allowed to choose their second favor character. For each time a character is highlighted, their stats - HP, ATK, DEF will be shown to the players. The player can choose two of the same characters to play.
2. Player In-Game Identification: During the fight, each player's character will have an arrow above the head for the player to keep track of their character controls and movements. This helps out a lot to prevent confusions when two players selected the same character.
3. Player Lives And Health Bar: Lives of each player will be displayed below the health bar that each time the health bar drops down to zero, one lives will be deducted. Each character will have a unique visual of lives.
# Development Process: 
- The game was built based on PyGame a library used for Python visualities. At first, the fighting/damage system was developed first along with the health system. After the health bar was correctly calculated with damage and defend stats, then the lives system took place in developing. Finally are implementing all the visuals and graphics for user information. Clock is used to calculate ticks and updates for the game every frame.
- The menu screen and interfaces are the one having the most challenges as there were bugs of player 2 able to reselect the character for player 1 through double select in a short time even though player 1 has locked their selection. The other bugs can also be listed like health bar is not reseting after losing the lives and continues going backwards, players can be "behind the scene" at some points or coordinates during the battle. However, those bugs are finally debugged and it took quite some time. 
# Installations:
The game test version is released and available at: https://leduyantran.itch.io/warrior-knock-out
1. Download the zipped file
2. Unzipped the file
3. Run the .exe to play the game
4. The game can be closed.

**Notes:** The file is in .py, since Python is not mostly recommended for games Windows will prompt for permissions.
# Instructions: 
- Press Enter to start the game
- Player 1: A, D keys to move left and right, W key to jump, and Space Bar to attack
- Player 2: Left, Right arrow keys to move left and right, Up arrow key to jump, and J or L arrow keys to attack
- After the battle, press Enter to continue back with the game
