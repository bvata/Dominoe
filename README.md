# Dominoe
Dominoe project

## Dominoe - Instructions:

- So here we have the pieces in the field: [3, 6][6, 6] and the status is that is the player's turn (moves are 0,+int,-int) so we choose int 5 which in ""Your pieces:", is 5:[1, 6] .
- When you type a positive integer like 5 the piece you selected from "Your pieces:", the piece "[1, 6]" moves to the right (follow arrow <----)
- When we want to move the piece to the left of the snake we type -int like the example below:
- In Step 2 , we enter "-1" when is the player's turn and the piece selected from "Your pieces:" is 1:[4, 4] , so follow the arrow "---->" , to see where is placed.
- At Step 3 , we choose "0" to take from the stock.
- When is the Computer's turn, just type enter as the "Status: ..." suggests.
- The game will draw if no one has pieces anymore and this will be calculated at each step
- The Computer has AI integrated to choose the best piece to mode, so there is some level of inteligence added in order to give some chances to the Computer to win.
- Wish you the best of luck.
Example:

Step1
======================================================================
Stock pieces:  14
Computer pieces:  6

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
Stock pieces:  14
Computer pieces:  6

[3, 6][6, 6][6, 1] <----

Your pieces:
1:[4, 4]
2:[2, 2]
3:[0, 3]
4:[1, 5]
5:[2, 6]

- Status: Computer is about to make a move. Press Enter to continue...

Step 2
======================================================================
Stock pieces:  14
Computer pieces:  5

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
Stock pieces:  14
Computer pieces:  5

----> [4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]

- Status: Computer is about to make a move. Press Enter to continue...

Step 3 
======================================================================
Stock pieces:  14
Computer pieces:  4

[1, 4][4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]

- Status: It's your turn to make a move. Enter your command.
0
======================================================================
Stock pieces:  13
Computer pieces:  4

[1, 4][4, 4][4, 3][3, 6][6, 6][6, 1]

Your pieces:
1:[2, 2]
2:[0, 3]
3:[1, 5]
4:[2, 6]
