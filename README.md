# n-queen
sloved n-Queen by backtracking Algorithm
## How It Works

The N-Queens solver uses a backtracking algorithm to find all possible arrangements of N queens on an N×N chessboard. The process involves the following steps:

1. **Recursive Placement**: The algorithm places queens one by one in different columns, starting from the leftmost column.

2. **Conflict Checking**: After placing a queen, it checks for conflicts with already placed queens. This includes checking the same row, column, and both diagonals.

3. **Backtracking**: If a conflict is detected, the algorithm backtracks by removing the last placed queen and tries the next position in the current column. This continues until all queens are placed or all possibilities are exhausted.

4. **Solution Collection**: Each time a valid arrangement is found (where all queens are placed without conflicts), it is stored as a solution.

5. **Output**: Finally, the solver displays all valid configurations and the total number of solutions found.

This method efficiently explores potential solutions while avoiding unnecessary checks, making it a powerful approach for solving the N-Queens problem.

Fall 2024
