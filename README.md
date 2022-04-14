# Dominoe
Dominoe project

## Dominoe - Instructions:

This is the description of the example on how to use the game, the points below refer to some steps(ex. Step1, Step2 ...)

- So here we have the pieces in the field: [3, 6][6, 6] and the status is that is the player's turn (moves are 0,+int,-int) so we choose int 5 which in ""Your pieces:", is 5:[1, 6] .
- When you type a positive integer like 5 the piece you selected from "Your pieces:", the piece "[1, 6]" moves to the right (follow arrow <----)
- When we want to move the piece to the left of the snake we type -int like the example below:
- In Step 2 , we enter "-1" when is the player's turn and the piece selected from "Your pieces:" is 1:[4, 4] , so follow the arrow "---->" , to see where is placed.
- At Step 3 , we choose "0" to take from the stock.
- When is the Computer's turn, just type enter as the "Status: ..." suggests.
- The game will draw if no one has pieces anymore and this will be calculated at each step
- The Computer has AI integrated to choose the best piece to mode, so there is some level of inteligence added in order to give some chances to the Computer to win.
- Enjoy







## Dominoe - Example:

Description:
<index>:[x,y] , where the index in the piece index in your hand, imagine when you play, you have pieces ordered in your hand. This is what refers to this index.
[x,y] , brackets imply the dominoe piece with two sides and x,y are nr from 0 to 6 on both sides.

Your pieces:
1:[4, 4]
2:[2, 2]
3:[0, 3]
4:[1, 5]
5:[1, 6]
6:[2, 6]


Example1 : When you want to enter a piece on the right side of the snake, you need to input a positive nr, like 5 is the index(nr of the peiece 5:[1, 6] as explained in the "Description".
======================================================================
- Stock pieces:  14
- Computer pieces:  6

[3, 6][6, 6] 

Your pieces:
1:[4, 4]
2:[2, 2]
3:[0, 3]
4:[1, 5]
5:[1, 6]
6:[2, 6]

 - Status: It's your turn to make a move. Enter your command.
5
======================================================================
- Stock pieces:  14
- Computer pieces:  6

[3, 6][6, 6][6, 1] <----

Your pieces:
1:[4, 4]
2:[2, 2]
3:[0, 3]
4:[1, 5]
5:[2, 6]

- Status: Computer is about to make a move. Press Enter to continue...

Example 2 :  When you want to enter a piece on the left side of the snake, you need to input a negative nr, like -<index of the piece in the hand>,(index of the piece 1 which is in this case is 1:[4, 4] as explained in the "Description".)
======================================================================
- Stock pieces:  14
- Computer pieces:  6

[4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[4, 4]
2:[2, 2]
3:[0, 3]
4:[1, 5]
5:[2, 6]

- Status: It's your turn to make a move. Enter your command.
-1
======================================================================
- Stock pieces:  14
- Computer pieces:  6

----> [4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]

- Status: Computer is about to make a move. Press Enter to continue...

Example 3 : When you do not have pieces to submit in the field, or if you want to take extra pieces you just need to enter 0 when is players turn.
======================================================================
- Stock pieces:  14
- Computer pieces:  6
[1, 4][4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]

- Status: It's your turn to make a move. Enter your command.
0
======================================================================
- Stock pieces:  14
- Computer pieces:  6

[1, 4][4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]

The computer automatically selects a piece of takes from the stock so you just need to pres "Enter" in the keyboard
======================================================================

