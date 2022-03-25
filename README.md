# Sudoku-puzzle

## Introduction

Consider the Sudoku puzzle as pictured below. There are 81 variables in total, i.e. the tiles to be filled with digits. Each variable is named by its row and its column, and must be assigned a value from 1 to 9, subject to the constraint that no two cells in the same row, column, or box may contain the same value.

![Sudoku](https://user-images.githubusercontent.com/81757215/160066254-a60ff7e6-dba8-4320-b88a-1f85df899c92.JPG)

The Sudoku board is represented by a Python dictionary. The keys of the dictionary will be the variable names, each of which corresponds directly to a location on the board. In other words, I use the variable names Al through A9 for the top row (left to right), down to I1 through I9 for the bottom row. For example, in the example board above, the dictionary would have sudoku["B1"] = 9, and sudoku["E9"] = 8.

In this project, I implemented two algorithms for solving the sudoku puzzle namely arc consistency and backtracking algorithm. The psuedo codes for the two algorithms are as follows.

## Arc consistency algorithm

![Arc consistency](https://user-images.githubusercontent.com/81757215/160067432-64c2fe72-f3cb-43dc-97b0-217b12812bba.JPG)

## Back tracking algorithm

![Backtracking](https://user-images.githubusercontent.com/81757215/160067521-47762455-7640-4b33-81ca-d66556cb9179.JPG)

## Input data

In the sudokus_start.txt file, there are hundreds of sample Sudoku puzzles to be solved. Each Sudoku puzzle is represented as a single line of text, which starts from the top-left corner of the board, and enumerates the digits in each tile, row by row. The number zero will be used to indicate tiles that have not yet been filled. For example, the Sudoku board in the diagram shown above is represented as the string:

00302060090030005001001806400... (and so on)
