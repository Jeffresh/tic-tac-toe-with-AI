# Tic tac toe with AI

### About

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

### Learning outcomes

After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, using classes and functions, handling errors, and processing user input. You will also learn to use OOP (Object-Oriented Programming) in the process.

# Stage 1/5: Initial setup

### Description

In this project, you'll write a game called Tic-TAc-Toe that you can play with your computer. the computer will have three levels of difficulty - easy, medium, hard.

But, for starters, let's write a program that knows how to work with coordinates and determine the state of the game.

Suppose the bottom left cell has the coordinates (1,1) and the top right cell has the coordinates (3,3) like in this table:

(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)

The program shoudl ask to enter the coordinates where the user wants to make a move.

Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.

But what if the user enters incorrect coordiantes? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of
that by checking a user's input and catching possible exceptions.

### Objectives

The program should work in the following way:

1. Get the 3x3 field form the first input line (it contains 9 symbols containing `x`, `o` and `_`, the latter means it's and empty cell)
2. Output this 3x3 field with cells before the user's move.
3. Then ask the user about his next move.
4. Then the user should input 2 numbers that represent the ell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the secnod line of the user input). Since the game always starts with X, if the number of X's and O's on the field isthe same, the user should make a move with X, and if X's is one more than O's, then the user should make a move with O.
5. Analyze user input and show messages in the folowing situations:
  - `This cell is occupied! Choose another one!` if the cell is not empty
  - `You should enter numbers!` If the user enters other symbols
  - `Coordinates should be from 1 to 3` If the user goes beyond the field.
6. Then output the table including the user's most recent move.
7. Then output the state of the game.

Possible states:
  - `Game not finished` When no side has a three in a row but the field has empty cells.
  - `Draw` When no side has a three in a row and the field has no empty cells
  - `X wins` When the field has three X in a row
  - `O wins` When thefield has three O in a row

If the usr input wrong coordinates, the program should keep asking until the user enters coordinate that represents an empty cell on the field and after that output
the field with that move. You should output the field only 2 times - before the move and after a legal move.


### This project is a part of the following track: Python Developer from Jetbrains Academy
