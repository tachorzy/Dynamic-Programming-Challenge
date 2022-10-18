#!/usr/bin/env python
import sys

def bestPath(matrix, row, col):
  if row == 1:
    return sumOfRow(matrix, col)
  
  lookup = [[0 for i in range(0, col)] for j in range(row)]
  
  for i in range(0, row):
    lookup[i][0] = matrix[i][0]

  for i in range(1, col):
    for j in range(0, row):
      if j == 0:
        top_left = lookup[row-1][i-1]
        bot_left = lookup[j+1][i-1]
      elif j == row-1:
        top_left = lookup[j-1][i-1]
        bot_left = lookup[0][i-1]
      else:
        top_left = lookup[j-1][i-1]
        bot_left = lookup[j+1][i-1]
      left = lookup[j][i-1]

      min_val = min(top_left, bot_left, left)
      lookup[j][i] = min_val + matrix[j][i]
      
  sum = 999999
  for i in range(0, row):
    bot = lookup[i][col-1]
    if sum > bot:
      sum = bot  
  return sum

def sumOfRow(matrix, col):
  sum = 0
  for i in range(0, col):
    sum += matrix[0][i]
  return sum

def main():
  m, n = (int(x) for x in input().split())
  matrix = [[int(x) for x in input().split()] for _ in range(m)]
  print(bestPath(matrix, m, n))


if __name__ == "__main__":
  main()