Digital World Final Programming Assignment
Victoria Yong 1004455 FO3
Video URL: https://youtu.be/CZihRbhSqQs

Goose Assault
This is a space invaders inspired game where the player is a goose and must shoot the 'aliens'.

Game Controls:

Press the left and right arrow keys to move the player. Hold down the key to keep moving.
Press the spacebar to shoot.
The player starts with 3 lives, reflected in the counter at the top right of the screen.
The purple line at the bottom of the screen reflects the boundary.
If an enemy reaches the boundary line, you lose one life.
The game ends when you lose all your lives or shoot all the 'aliens' on screen.

About the code:

This game was made using the python Turtle and Random libraries, as well as the SM class from libdw.
This code makes use of 5 classes, which includes:
1. The Player class
    - Specifies keyboard controls and graphics for the player
2. The Alien class
    - Describes the normal enemy type in the game, represented by the boy sprite
3. The GreenAlien Class
    - Which inherits from the Alien class and is an enemy type that moves twice as fast as the Alien class enemies
    - Represented by the girl sprite
4. The bullet class
    - Describes the charateristics of the player's attack
5. The PlayerHealth Class
    - Which is a state machine inheriting from the SM class in libdw.sm
    - Takes in 2 arguments, the number or lives left (global state) and the player, then changes the display on the top
      right side of the screen to the correct number of lives left
The python Random library is used to generate levels for the game by spawning a random number of each enemy type at the
start of each game.
