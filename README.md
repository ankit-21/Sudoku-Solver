# Sudoku-Solver
## Solving Sudoku using Backtracking Algorithm

## Backtracking Algorithm
Backtracking algorithm is a technique used for solving recursive problems. In this project, I have made use of the backtracking algorithm to solve any given 3x3 sudoku.

### Sudoku
Sudoku is a very famous game that invlolves placing numbers from 1-9 in a 3x3 grid by following certain rules. 
#### Rule #1: All the columns sould have unique numbers (1-9)
#### Rule #2: All the rows sould have unique numbers (1-9)
#### Rule #3: The 3x3 boxes in the grid sould have unique numbers (1-9)

Based on these rules I have written a code using backtracking algorithm that checks for each number assignment whether it is a valid entry or not. If at any point any one of the rules is not followed for an assigned box, the algorithm goes back to deleting the assigned values until all the rules are followed for that box.  
