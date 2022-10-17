# Dynamic-Programming-Challenge
COSC 3320 HW2 Programming Challenge, Professor Wu

Given a m * n matrix, your task is to compute a path from any element on the 1 st column to any element on the last column at minimal cost. The path consists of several steps, each step is moving from column j to column j+1 in an adjacent (horizontal or diagonal) row. The first row and the last row are considered as adjacent rows. The cost of a path is the sum of visited integers.

The two slightly different matrices are shown in figure below. The minimum cost path is illustrated in the figure and the 2 nd path takes advantage of the adjacency property of the first and last row.

You'll be given two integers m and n that indicate the number of rows and columns at the first line. The next m lines will be the matrix and each line represents one row of the given matrix. You're required to output the minimum cost.

Notes: The test cases have the properties: number of rows is between 1 and 10; number of columns is between 1 and 100; number in matrix can be positive or negative; All path weights can be represented by 30-bit signed integer.

![image](https://user-images.githubusercontent.com/81454679/196077606-370b1814-e830-486c-9de6-beb9538e74f9.png)


