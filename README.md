# Dominoes
Classic dominoes game against a computer.
In this project artificial intelligence can make use of simple statistics to make educated decisions. 

<h2>Rules</h2>
To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.


At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).

To start the game, players determine the starting piece. The player with the highest domino or the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.

<h2>Interface</h2>
The player is able to see the domino snake, the so-called playing field, and their own pieces.
<h4>Examples</h4>

<em>The player makes the first move (status = "player"):</em>
![1](https://user-images.githubusercontent.com/93375843/181848503-f1ed794a-68ba-4d6c-9bf0-3d48f8ff58c0.jpg)

<em>The Computer makes the first move (status = "computer"):</em>

![2](https://user-images.githubusercontent.com/93375843/181848808-e99d1951-984d-4019-be9b-2c7d7338dd45.jpg)
<h2>AI</h2>
The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. To reduce our chances of skipping a turn, we must increase the diversity of our pieces. For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. Using this logic, the AI evaluates each domino in possession, based on the rarity. Dominoes with rare numbers get lower scores, while dominoes with common numbers get higher scores.

The AI uses the following algorithm to calculate the score:

            1. Count the number of 0's, 1's, 2's, etc., in our hand, and in the snake.
            2. Each domino in our hand receives a score equal to the sum of appearances of each of its numbers.
            
The AI now attempts to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI moves down the score list and tries another domino. The AI skips the turn if it runs out of options.
<h4>Example</h4>

![3](https://user-images.githubusercontent.com/93375843/181852470-f74f2c73-7243-450d-b3a2-338239cde22f.jpg)

