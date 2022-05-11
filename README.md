# Python-Adventure-Game
Classic Adventure Game programmed on Python
Project Overview
In this project, I made a simpler version of an old-fashioned text-based adventure game. The idea is to focus on some key things that we need if want to make a working game:
	•	The game gives players a description of what's happening, and then asks them to make a choice.
	•	Something different happens depending on the choice the player made.
	•	The game also includes some random factors, so that it's a little different each time.
	•	The game has conditions for winning and losing.
	•	When the game is over, it asks if the player wants to play again.

Project Instructions
1. Print descriptions of what's happening for the player
One thing the game will need to do is to print messages for the player to describe what is happening. 
2. Pausing between printing descriptions
3. Give the player some choices
To do this, you'll need to get some input from the player, and then change what happens depending on what that input is.

4. Make sure the player gives a valid input
If the player tries to respond with something invalid, your program should ask them to try again—and it should keep asking them to try again until they give valid input. 

5. Add functions and refactor your code
That way, when the player chooses to go to one of these places, you can simply call the function that displays the description and choices for that place. This is especially good if you want the player to be able to go back to the same place repeatedly, from different locations in the code.

6. Use randomness in your game
Another key feature of most games is randomness or chance. If everything always happens exactly the same way, it can become boring and predictable.

7. Create win and lose conditions
Eventually, the game should come to an end—and tell the player that they won or lost. The end result of the game should be influenced by the player's choices (and possibly some degree of randomness as well). Generally, it's a good idea to use randomness to only partially influence the outcome. If what happens to the player is completely random, the player will feel out of control and probably won't enjoy it. 
8. Check if the player wants to play again
When Python gets to the end of your script, it will exit back to the terminal. But that's not a good player experience. Instead, it would be better if the game asked the player whether they want to play again. Just like with other choices you've asked the player to make, this will need to get the player's input and then check if the input is valid.
If the player indicates that yes, they want to play again, then the game should start over.
