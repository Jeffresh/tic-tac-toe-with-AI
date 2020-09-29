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


### This project is a part of the following track: Python Developer from Jetbrains Academy
